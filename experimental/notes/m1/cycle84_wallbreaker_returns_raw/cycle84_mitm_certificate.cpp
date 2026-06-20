#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <cstdio>
#include <cstring>
#include <filesystem>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <numeric>
#include <sstream>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>

namespace fs = std::filesystem;
using u128 = unsigned __int128;

static constexpr uint32_t P = 17;
static constexpr int DEG = 16;
static constexpr int SLOT_STATES = 48;
static constexpr int SHARDS = 256;
static constexpr const char* VERSION = "cycle84-dlog-fp64-v1";

// ---------------- SHA-256 (self-contained) ----------------
class Sha256 {
    uint32_t h_[8] = {0x6a09e667u,0xbb67ae85u,0x3c6ef372u,0xa54ff53au,
                      0x510e527fu,0x9b05688cu,0x1f83d9abu,0x5be0cd19u};
    uint64_t bits_ = 0;
    std::array<uint8_t,64> buf_{};
    size_t used_ = 0;
    static uint32_t rotr(uint32_t x, int n){ return (x>>n)|(x<<(32-n)); }
    void block(const uint8_t* p) {
        static constexpr uint32_t K[64] = {
          0x428a2f98u,0x71374491u,0xb5c0fbcfu,0xe9b5dba5u,0x3956c25bu,0x59f111f1u,0x923f82a4u,0xab1c5ed5u,
          0xd807aa98u,0x12835b01u,0x243185beu,0x550c7dc3u,0x72be5d74u,0x80deb1feu,0x9bdc06a7u,0xc19bf174u,
          0xe49b69c1u,0xefbe4786u,0x0fc19dc6u,0x240ca1ccu,0x2de92c6fu,0x4a7484aau,0x5cb0a9dcu,0x76f988dau,
          0x983e5152u,0xa831c66du,0xb00327c8u,0xbf597fc7u,0xc6e00bf3u,0xd5a79147u,0x06ca6351u,0x14292967u,
          0x27b70a85u,0x2e1b2138u,0x4d2c6dfcu,0x53380d13u,0x650a7354u,0x766a0abbu,0x81c2c92eu,0x92722c85u,
          0xa2bfe8a1u,0xa81a664bu,0xc24b8b70u,0xc76c51a3u,0xd192e819u,0xd6990624u,0xf40e3585u,0x106aa070u,
          0x19a4c116u,0x1e376c08u,0x2748774cu,0x34b0bcb5u,0x391c0cb3u,0x4ed8aa4au,0x5b9cca4fu,0x682e6ff3u,
          0x748f82eeu,0x78a5636fu,0x84c87814u,0x8cc70208u,0x90befffau,0xa4506cebu,0xbef9a3f7u,0xc67178f2u};
        uint32_t w[64];
        for(int i=0;i<16;i++) w[i]=(uint32_t(p[4*i])<<24)|(uint32_t(p[4*i+1])<<16)|(uint32_t(p[4*i+2])<<8)|p[4*i+3];
        for(int i=16;i<64;i++){
            uint32_t s0=rotr(w[i-15],7)^rotr(w[i-15],18)^(w[i-15]>>3);
            uint32_t s1=rotr(w[i-2],17)^rotr(w[i-2],19)^(w[i-2]>>10);
            w[i]=w[i-16]+s0+w[i-7]+s1;
        }
        uint32_t a=h_[0],b=h_[1],c=h_[2],d=h_[3],e=h_[4],f=h_[5],g=h_[6],h=h_[7];
        for(int i=0;i<64;i++){
            uint32_t S1=rotr(e,6)^rotr(e,11)^rotr(e,25);
            uint32_t ch=(e&f)^((~e)&g);
            uint32_t t1=h+S1+ch+K[i]+w[i];
            uint32_t S0=rotr(a,2)^rotr(a,13)^rotr(a,22);
            uint32_t maj=(a&b)^(a&c)^(b&c);
            uint32_t t2=S0+maj;
            h=g; g=f; f=e; e=d+t1; d=c; c=b; b=a; a=t1+t2;
        }
        h_[0]+=a;h_[1]+=b;h_[2]+=c;h_[3]+=d;h_[4]+=e;h_[5]+=f;h_[6]+=g;h_[7]+=h;
    }
public:
    void update(const void* data, size_t n){
        const uint8_t* p=static_cast<const uint8_t*>(data); bits_ += uint64_t(n)*8;
        while(n){ size_t take=std::min(n,64-used_); std::memcpy(buf_.data()+used_,p,take); used_+=take;p+=take;n-=take; if(used_==64){block(buf_.data());used_=0;} }
    }
    std::string hex(){
        uint64_t orig_bits=bits_;
        uint8_t one=0x80; update(&one,1);
        uint8_t zero=0;
        while(used_!=56) update(&zero,1);
        uint8_t len[8]; for(int i=0;i<8;i++) len[7-i]=uint8_t(orig_bits>>(8*i));
        // update changes bits_, irrelevant after finalization.
        update(len,8);
        std::ostringstream os; os<<std::hex<<std::setfill('0');
        for(uint32_t x:h_) os<<std::setw(8)<<x;
        return os.str();
    }
};

static void sha_update_u64_le(Sha256& s, uint64_t x){ uint8_t b[8]; for(int i=0;i<8;i++)b[i]=uint8_t(x>>(8*i)); s.update(b,8); }
static void sha_update_u128_9le(Sha256& s, u128 x){ uint8_t b[9]; for(int i=0;i<9;i++)b[i]=uint8_t(x>>(8*i)); s.update(b,9); }

static std::string u128_dec(u128 x){ if(x==0)return "0"; std::string s; while(x){ s.push_back(char('0'+x%10));x/=10;} std::reverse(s.begin(),s.end());return s; }
static uint64_t lo64(u128 x){ return uint64_t(x); }
static uint8_t hi2(u128 x){ return uint8_t(x>>64); }
static u128 pow17_16_minus_1(){ u128 x=1; for(int i=0;i<16;i++)x*=17; return x-1; }
static const u128 GROUP_N = pow17_16_minus_1();
static constexpr uint64_t P0_COUNT = 52747567104ULL;

// ---------------- Exact quotient-ring / field model ----------------
struct Field {
    std::array<uint8_t,DEG> c{};
    bool operator==(Field const& o) const noexcept { return c==o.c; }
    bool operator!=(Field const& o) const noexcept { return !(*this==o); }
};
struct FieldHash {
    size_t operator()(Field const& a) const noexcept {
        uint64_t h=1469598103934665603ULL;
        for(uint8_t x:a.c){h^=x;h*=1099511628211ULL;}
        return size_t(h);
    }
};
static Field fzero(){ return Field{}; }
static Field fone(){ Field a; a.c[0]=1; return a; }
static Field fconst(int x){ Field a; x%=17;if(x<0)x+=17;a.c[0]=uint8_t(x);return a; }
static Field fadd(Field a, Field const& b){ for(int i=0;i<DEG;i++)a.c[i]=uint8_t((a.c[i]+b.c[i])%17);return a; }
static Field fsub(Field a, Field const& b){ for(int i=0;i<DEG;i++)a.c[i]=uint8_t((int(a.c[i])-int(b.c[i])+17)%17);return a; }
static Field fmul(Field const& a, Field const& b){
    int64_t t[31]{};
    for(int i=0;i<16;i++) if(a.c[i]) for(int j=0;j<16;j++) if(b.c[j]) t[i+j]+=int(a.c[i])*int(b.c[j]);
    for(int d=30;d>=16;--d){ int64_t q=t[d]%17; if(q<0)q+=17; t[d]=0; t[d-8]-=q; t[d-16]-=3*q; }
    Field r; for(int i=0;i<16;i++){int64_t q=t[i]%17;if(q<0)q+=17;r.c[i]=uint8_t(q);} return r;
}
static Field fpow(Field a, u128 e){ Field r=fone(); while(e){if(e&1)r=fmul(r,a);a=fmul(a,a);e>>=1;}return r; }
static int modpow17(int a, uint64_t e){ int r=1;a%=17;while(e){if(e&1)r=r*a%17;a=a*a%17;e>>=1;}return r; }
static std::string field_json(Field const& a){ std::ostringstream o;o<<"[";for(int i=0;i<16;i++){if(i)o<<",";o<<int(a.c[i]);}o<<"]";return o.str(); }

static const int ESET[3][8]={{0,1,2,3,5,11,12,13},{0,1,2,3,4,8,9,14},{0,1,2,4,5,7,11,14}};
static const int PCOEFF[3][9]={{6,4,4,10,5,4,0,0,1},{14,13,14,12,5,9,0,0,1},{4,12,1,5,0,11,0,0,1}};
static const int SCOLOR[3]={15,9,12};

static Field peval(int type0, Field const& z){ Field r=fzero(); for(int j=8;j>=0;j--)r=fadd(fmul(r,z),fconst(PCOEFF[type0][j])); return r; }

static uint64_t inv_mod_u64(uint64_t a,uint64_t m){
    int64_t t=0,newt=1; int64_t r=int64_t(m),newr=int64_t(a%m);
    while(newr){int64_t q=r/newr;int64_t tt=t-q*newt;t=newt;newt=tt;int64_t rr=r-q*newr;r=newr;newr=rr;}
    if(r!=1)throw std::runtime_error("noninvertible CRT factor"); if(t<0)t+=m; return uint64_t(t);
}

struct State { Field u; u128 log=0; uint8_t color=0; uint8_t type=0,a=0; };
struct SideEntry { uint64_t lo=0; uint8_t hi=0; uint8_t color=0; };
static u128 side_exp(SideEntry const& x){ return u128(x.lo)|(u128(x.hi)<<64); }
static SideEntry make_side(u128 e,uint8_t c){ return SideEntry{lo64(e),hi2(e),c}; }
static u128 addmod(u128 a,u128 b){u128 s=a+b; if(s>=GROUP_N)s-=GROUP_N; return s;}

struct Model {
    Field g,eta,beta;
    std::array<std::array<State,48>,7> st{};
    std::vector<SideEntry> L,R;
    std::array<std::vector<uint32_t>,16> Rby{};
    std::string state_sha,L_sha,R_sha;

    Model(){ build(); }
    void build(){
        if(u128_dec(GROUP_N)!="48661191875666868480") throw std::runtime_error("N mismatch");
        g=fzero();g.c[0]=1;g.c[1]=1;
        eta=fzero();eta.c[9]=6;
        beta=fzero();beta.c[0]=2;beta.c[1]=1;
        const uint64_t primes[7]={2,3,5,29,18913,41761,184417};
        if(fpow(g,GROUP_N)!=fone())throw std::runtime_error("g^N != 1");
        for(uint64_t q:primes)if(fpow(g,GROUP_N/q)==fone())throw std::runtime_error("g not primitive");
        if(fpow(eta,256)!=fone()||fpow(eta,128)==fone()||fpow(eta,16)!=fconst(3))throw std::runtime_error("eta check failed");
        if(fpow(beta,256)==fone())throw std::runtime_error("beta inadmissible");

        Field xi=fpow(beta,2), etainv=fpow(eta,GROUP_N-1);
        std::array<Field,336> raw{};
        int z=0;
        for(int t=1;t<=7;t++){
            Field ef=fpow(etainv,2*t);
            for(int ty=0;ty<3;ty++)for(int a=0;a<16;a++){
                int p3=modpow17(3,(16-a)%16);
                Field arg=fmul(fmul(xi,fconst(p3)),ef);
                Field u=peval(ty,arg); if(a&1)u=fsub(fzero(),u);
                if(u==fzero())throw std::runtime_error("zero state");
                raw[z++]=u;
            }
        }
        // Deterministic Pohlig-Hellman by complete tables in seven coprime factors.
        const uint64_t mods[7]={256,9,5,29,18913,41761,184417};
        std::array<std::unordered_map<Field,uint32_t,FieldHash>,7> maps;
        for(int j=0;j<7;j++){
            uint64_t m=mods[j]; auto& mp=maps[j]; mp.reserve(size_t(m*1.35)+8);
            Field gm=fpow(g,GROUP_N/m),x=fone();
            for(uint32_t e=0;e<m;e++){if(!mp.emplace(x,e).second)throw std::runtime_error("DLP table repeat");x=fmul(x,gm);} if(x!=fone()||mp.size()!=m)throw std::runtime_error("DLP table order");
        }
        auto dlog=[&](Field const& h)->u128{
            u128 x=0;
            for(int j=0;j<7;j++){
                uint64_t m=mods[j]; Field hm=fpow(h,GROUP_N/m); auto it=maps[j].find(hm); if(it==maps[j].end())throw std::runtime_error("DLP lookup");
                u128 Mi=GROUP_N/m; uint64_t mi=uint64_t(Mi%m); uint64_t inv=inv_mod_u64(mi,m);
                u128 term=u128(it->second)*Mi*u128(inv); x=(x+term)%GROUP_N;
            }
            if(fpow(g,x)!=h)throw std::runtime_error("DLP verify"); return x;
        };
        z=0; Sha256 sh;
        for(int t=1;t<=7;t++)for(int k=0;k<48;k++){
            int ty=k/16,a=k%16; State s; s.u=raw[z++];s.log=dlog(s.u);s.color=uint8_t((SCOLOR[ty]+8*(a&1))%16);s.type=uint8_t(ty+1);s.a=uint8_t(a);st[t-1][k]=s;
            uint8_t pre[3]={uint8_t(t),uint8_t(k),s.color};sh.update(pre,3);sh.update(s.u.c.data(),16);sha_update_u128_9le(sh,s.log);
        }
        state_sha=sh.hex();
        if(state_sha!="4cb6ea024522568419f1e5c51d18f38bde78ca14dfdce950411a907af982b497")throw std::runtime_error("state hash mismatch");
        build_sides();
    }
    void build_sides(){
        L.reserve(48*48*48); Sha256 sl;
        std::array<uint64_t,16> lc{};
        for(int k1=0;k1<48;k1++)for(int k2=0;k2<48;k2++)for(int k3=0;k3<48;k3++){
            u128 e=(st[0][k1].log+st[1][k2].log+st[2][k3].log)%GROUP_N; uint8_t c=uint8_t((st[0][k1].color+st[1][k2].color+st[2][k3].color)%16);
            L.push_back(make_side(e,c));sha_update_u128_9le(sl,e);sl.update(&c,1);lc[c]++;
        }
        L_sha=sl.hex(); if(L_sha!="0fbb49337f20496968c07b9a62e49d1b92e304a0ec32e4d9da785181e28d2ffe")throw std::runtime_error("L hash mismatch");
        R.reserve(48ULL*48*48*48); Sha256 sr; std::array<uint64_t,16> rc{};
        for(int k4=0;k4<48;k4++)for(int k5=0;k5<48;k5++)for(int k6=0;k6<48;k6++)for(int k7=0;k7<48;k7++){
            u128 e=(st[3][k4].log+st[4][k5].log+st[5][k6].log+st[6][k7].log)%GROUP_N;uint8_t c=uint8_t((st[3][k4].color+st[4][k5].color+st[5][k6].color+st[6][k7].color)%16);
            uint32_t idx=uint32_t(R.size());R.push_back(make_side(e,c));Rby[c].push_back(idx);sha_update_u128_9le(sr,e);sr.update(&c,1);rc[c]++;
        }
        R_sha=sr.hex();if(R_sha!="27615bb17707290e43dd8d1f1496eb94889b8f66b917308a847ebb2a67466a89")throw std::runtime_error("R hash mismatch");
        uint64_t n=0;for(auto const& l:L)n+=Rby[(4-l.color)&15].size();if(n!=P0_COUNT)throw std::runtime_error("P0 count mismatch");
    }
};

static std::array<int,3> decodeL(uint32_t x){std::array<int,3> k;for(int j=2;j>=0;j--){k[j]=x%48;x/=48;}return k;}
static std::array<int,4> decodeR(uint32_t x){std::array<int,4> k;for(int j=3;j>=0;j--){k[j]=x%48;x/=48;}return k;}
static u128 left_exp(Model const&m,uint32_t i){return side_exp(m.L[i]);}
static u128 right_exp(Model const&m,uint32_t i){return side_exp(m.R[i]);}

// ---------------- Stage 1 emit: shard by top byte of low-64 exponent; store low 56 bits in 7 bytes ----------------
struct Writer7 {
    FILE* f=nullptr; std::vector<uint8_t> b; size_t used=0;
    Writer7()=default;
    Writer7(fs::path const& p,size_t cap=1<<16):b(cap){f=std::fopen(p.string().c_str(),"wb");if(!f)throw std::runtime_error("open "+p.string());}
    Writer7(Writer7&&o)noexcept:f(o.f),b(std::move(o.b)),used(o.used){o.f=nullptr;o.used=0;}
    Writer7& operator=(Writer7&&o)noexcept{if(this!=&o){close();f=o.f;b=std::move(o.b);used=o.used;o.f=nullptr;o.used=0;}return *this;}
    Writer7(Writer7 const&)=delete;Writer7& operator=(Writer7 const&)=delete;
    void put(uint64_t low56){if(used+7>b.size())flush();for(int i=0;i<7;i++)b[used++]=uint8_t(low56>>(8*i));}
    void flush(){if(used){if(std::fwrite(b.data(),1,used,f)!=used)throw std::runtime_error("write failed");used=0;}}
    void close(){if(f){flush();std::fclose(f);f=nullptr;}}
    ~Writer7(){close();}
};
static fs::path stage1_dir(fs::path const& d){return d/"stage1";}
static fs::path part_path(fs::path const& d,int s,int w){char n[80];std::snprintf(n,sizeof(n),"shard_%03d.worker_%04d.bin",s,w);return stage1_dir(d)/n;}

static void cmd_selftest(fs::path out){Model m;std::ofstream o(out);o<<"{\n  \"version\": \""<<VERSION<<"\",\n  \"decision\": \"MODEL_AND_DLOG_SELFTEST_PASS\",\n  \"field\": {\"p\":17,\"modulus_coeffs\":[3,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],\"N\":\""<<u128_dec(GROUP_N)<<"\"},\n  \"generator_coeffs\": "<<field_json(m.g)<<",\n  \"eta_coeffs\": "<<field_json(m.eta)<<",\n  \"beta_coeffs\": "<<field_json(m.beta)<<",\n  \"state_table_sha256\": \""<<m.state_sha<<"\",\n  \"L_table_sha256\": \""<<m.L_sha<<"\",\n  \"R_table_sha256\": \""<<m.R_sha<<"\",\n  \"L_count\": "<<m.L.size()<<",\n  \"R_count\": "<<m.R.size()<<",\n  \"P0\": "<<P0_COUNT<<"\n}\n";std::cout<<"selftest PASS\n";}

static void cmd_emit(fs::path d,int worker,int workers,uint64_t max_pairs){
    if(worker<0||worker>=workers||workers<=0)throw std::runtime_error("bad worker partition");Model m;fs::create_directories(stage1_dir(d));
    std::vector<Writer7> wr;wr.reserve(SHARDS);for(int s=0;s<SHARDS;s++)wr.emplace_back(part_path(d,s,worker));
    uint32_t a=uint32_t((uint64_t(m.L.size())*worker)/workers), b=uint32_t((uint64_t(m.L.size())*(worker+1))/workers);
    uint64_t count=0;bool partial=false;
    for(uint32_t li=a;li<b&&!partial;li++){
        auto const& l=m.L[li];auto const& rs=m.Rby[(4-l.color)&15];u128 le=side_exp(l);
        for(uint32_t ri:rs){u128 e=addmod(le,right_exp(m,ri));uint64_t fp=lo64(e);wr[fp>>56].put(fp&0x00ffffffffffffffULL);count++;if(max_pairs&&count>=max_pairs){partial=true;break;}}
        if((count&((1ULL<<30)-1))==0&&count)std::cerr<<"worker "<<worker<<" emitted "<<count<<"\n";
    }
    for(auto&x:wr)x.close();
    fs::path sm=stage1_dir(d)/("worker_"+std::to_string(worker)+".summary.json");std::ofstream o(sm);o<<"{\n  \"version\": \""<<VERSION<<"\",\n  \"worker\": "<<worker<<",\n  \"workers\": "<<workers<<",\n  \"left_start\": "<<a<<",\n  \"left_end\": "<<b<<",\n  \"record_count\": "<<count<<",\n  \"partial\": "<<(partial?"true":"false")<<",\n  \"record_format\": \"shard=fp64[63:56], payload=fp64[55:0] little-endian 7 bytes\"\n}\n";
    std::cout<<"emit worker="<<worker<<" records="<<count<<(partial?" PARTIAL":" COMPLETE")<<"\n";
}

static void radix_sort56(std::vector<uint64_t>& a){
    if(a.empty())return;std::vector<uint64_t> b(a.size());constexpr uint32_t B=1u<<14,M=B-1;std::vector<uint64_t> cnt(B),pos(B);
    for(int pass=0;pass<4;pass++){int sh=14*pass;std::fill(cnt.begin(),cnt.end(),0);for(uint64_t x:a)cnt[(x>>sh)&M]++;uint64_t s=0;for(uint32_t i=0;i<B;i++){pos[i]=s;s+=cnt[i];}for(uint64_t x:a)b[pos[(x>>sh)&M]++]=x;a.swap(b);}
}
static uint64_t file_size_checked(fs::path const&p){std::error_code ec;auto n=fs::file_size(p,ec);if(ec)throw std::runtime_error("stat "+p.string());return n;}
static void write_u64_le(std::ostream&o,uint64_t x){char b[8];for(int i=0;i<8;i++)b[i]=char(x>>(8*i));o.write(b,8);}
static uint64_t read_u64_le(std::istream&i){uint8_t b[8];i.read(reinterpret_cast<char*>(b),8);if(!i)throw std::runtime_error("read u64");uint64_t x=0;for(int j=0;j<8;j++)x|=uint64_t(b[j])<<(8*j);return x;}

static fs::path reduce_dir(fs::path const&d){return d/"reduce";}
static void cmd_reduce_shard(fs::path d,int shard,int workers){
    if(shard<0||shard>=256)throw std::runtime_error("bad shard");fs::create_directories(reduce_dir(d));uint64_t total=0;
    for(int w=0;w<workers;w++){auto p=part_path(d,shard,w);uint64_t n=file_size_checked(p);if(n%7)throw std::runtime_error("bad 7-byte file");total+=n/7;}
    std::vector<uint64_t>a; a.reserve(size_t(total));
    std::vector<uint8_t> buf(7*(1<<20));
    for(int w=0;w<workers;w++){auto p=part_path(d,shard,w);std::ifstream in(p,std::ios::binary);while(in){in.read(reinterpret_cast<char*>(buf.data()),buf.size());size_t n=size_t(in.gcount());if(n%7)throw std::runtime_error("truncated payload");for(size_t off=0;off<n;off+=7){uint64_t x=0;for(int j=0;j<7;j++)x|=uint64_t(buf[off+j])<<(8*j);a.push_back(x);}}}
    if(a.size()!=total)throw std::runtime_error("record total mismatch");radix_sort56(a);
    char cn[64];std::snprintf(cn,sizeof(cn),"shard_%03d.candidates.bin",shard);std::ofstream co(reduce_dir(d)/cn,std::ios::binary);
    Sha256 sha;uint64_t distinct=0,repeated=0,maxrun=0,candrecs=0;
    size_t i=0;while(i<a.size()){size_t j=i+1;while(j<a.size()&&a[j]==a[i])j++;uint64_t run=j-i;uint64_t fp=(uint64_t(shard)<<56)|a[i];for(uint64_t z=0;z<run;z++)sha_update_u64_le(sha,fp);distinct++;maxrun=std::max(maxrun,run);if(run>=2){repeated++;write_u64_le(co,fp);write_u64_le(co,run);candrecs++;}i=j;}
    std::string hh=sha.hex();char sn[64];std::snprintf(sn,sizeof(sn),"shard_%03d.summary.tsv",shard);std::ofstream so(reduce_dir(d)/sn);so<<shard<<"\t"<<total<<"\t"<<distinct<<"\t"<<repeated<<"\t"<<maxrun<<"\t"<<candrecs<<"\t"<<hh<<"\n";
    std::cout<<"reduce shard="<<shard<<" records="<<total<<" repeated_fps="<<repeated<<" max="<<maxrun<<" sha256="<<hh<<"\n";
}

struct Candidate{uint64_t fp,count;};
static fs::path candidate_file(fs::path const&d){return reduce_dir(d)/"candidates.bin";}
static void cmd_merge_reduce(fs::path d,int workers){
    (void)workers;uint64_t C=0,total=0,distinct=0,repeated=0,maxrun=0;std::vector<std::string> hashes(256);std::vector<uint64_t> rc(256),dc(256),rr(256),mr(256),cc(256);
    for(int s=0;s<256;s++){char sn[64];std::snprintf(sn,sizeof(sn),"shard_%03d.summary.tsv",s);std::ifstream in(reduce_dir(d)/sn);int sid;in>>sid>>rc[s]>>dc[s]>>rr[s]>>mr[s]>>cc[s]>>hashes[s];if(!in||sid!=s)throw std::runtime_error("bad shard summary");C+=cc[s];total+=rc[s];distinct+=dc[s];repeated+=rr[s];maxrun=std::max(maxrun,mr[s]);}
    if(total!=P0_COUNT)throw std::runtime_error("stage1 total is not P0 (partial or missing emit)");
    std::ofstream out(candidate_file(d),std::ios::binary);out.write("C84CND1\0",8);write_u64_le(out,C);Sha256 csha;
    for(int s=0;s<256;s++){char cn[64];std::snprintf(cn,sizeof(cn),"shard_%03d.candidates.bin",s);std::ifstream in(reduce_dir(d)/cn,std::ios::binary);for(uint64_t z=0;z<cc[s];z++){uint64_t fp=read_u64_le(in),n=read_u64_le(in);write_u64_le(out,fp);write_u64_le(out,n);sha_update_u64_le(csha,fp);sha_update_u64_le(csha,n);}char extra;if(in.read(&extra,1))throw std::runtime_error("extra candidate bytes");}
    std::string ch=csha.hex();std::ofstream m(reduce_dir(d)/"manifest.json");m<<"{\n  \"version\": \""<<VERSION<<"\",\n  \"P0\": "<<total<<",\n  \"fingerprint\": \"canonical exponent E in [0,N), low 64 bits\",\n  \"candidate_rule\": \"all fingerprint runs of length >=2\",\n  \"candidate_count\": "<<C<<",\n  \"candidate_records_sha256\": \""<<ch<<"\",\n  \"distinct_fingerprints\": "<<distinct<<",\n  \"repeated_fingerprints\": "<<repeated<<",\n  \"max_projected_count\": "<<maxrun<<",\n  \"shards\": [\n";
    for(int s=0;s<256;s++){m<<"    {\"id\":"<<s<<",\"records\":"<<rc[s]<<",\"distinct\":"<<dc[s]<<",\"repeated\":"<<rr[s]<<",\"max_run\":"<<mr[s]<<",\"sorted_fp64_sha256\":\""<<hashes[s]<<"\"}"<<(s==255?"\n":",\n");}
    m<<"  ]\n}\n";std::cout<<"merge reduce candidates="<<C<<" max_projected="<<maxrun<<" sha256="<<ch<<"\n";
}

static std::vector<Candidate> load_candidates(fs::path const&d){std::ifstream in(candidate_file(d),std::ios::binary);char magic[8];in.read(magic,8);if(std::memcmp(magic,"C84CND1\0",8))throw std::runtime_error("bad candidates magic");uint64_t C=read_u64_le(in);std::vector<Candidate>v;v.reserve(C);for(uint64_t i=0;i<C;i++)v.push_back({read_u64_le(in),read_u64_le(in)});char x;if(in.read(&x,1))throw std::runtime_error("extra candidates bytes");return v;}
struct FixedHash{size_t operator()(uint64_t x)const noexcept{x^=x>>30;x*=0xbf58476d1ce4e5b9ULL;x^=x>>27;x*=0x94d049bb133111ebULL;x^=x>>31;return size_t(x);}};
struct Cell{uint64_t count=0;uint8_t nw=0;std::array<uint64_t,13>w{};};
static fs::path replay_dir(fs::path const&d){return d/"replay";}
static fs::path replay_file(fs::path const&d,int w){char n[64];std::snprintf(n,sizeof(n),"worker_%04d.bin",w);return replay_dir(d)/n;}
static void cmd_replay(fs::path d,int worker,int workers,uint64_t max_pairs){
    if(worker<0||worker>=workers)throw std::runtime_error("bad worker");Model m;auto cand=load_candidates(d);std::unordered_map<uint64_t,uint32_t,FixedHash> mp;mp.reserve(cand.size()*2+8);for(uint32_t i=0;i<cand.size();i++)if(!mp.emplace(cand[i].fp,i).second)throw std::runtime_error("duplicate candidate");std::vector<Cell> cells(cand.size()*3);
    uint32_t a=uint32_t(uint64_t(m.L.size())*worker/workers),b=uint32_t(uint64_t(m.L.size())*(worker+1)/workers);uint64_t scanned=0,hits=0;bool partial=false;
    for(uint32_t li=a;li<b&&!partial;li++){auto const&l=m.L[li];u128 le=side_exp(l);for(uint32_t ri:m.Rby[(4-l.color)&15]){u128 e=addmod(le,right_exp(m,ri));auto it=mp.find(lo64(e));if(it!=mp.end()){uint8_t h=hi2(e);if(h>2)throw std::runtime_error("bad exponent high bits");Cell&c=cells[3ULL*it->second+h];c.count++;if(c.nw<13)c.w[c.nw++]=(uint64_t(li)<<23)|ri;hits++;}scanned++;if(max_pairs&&scanned>=max_pairs){partial=true;break;}}}
    fs::create_directories(replay_dir(d));std::ofstream out(replay_file(d,worker),std::ios::binary);out.write("C84RPL1\0",8);write_u64_le(out,cand.size());write_u64_le(out,worker);write_u64_le(out,workers);write_u64_le(out,scanned);uint8_t p=partial;out.write(reinterpret_cast<char*>(&p),1);uint8_t pad[7]{};out.write(reinterpret_cast<char*>(pad),7);
    for(auto const&c:cells){write_u64_le(out,c.count);out.put(char(c.nw));out.write(reinterpret_cast<char*>(pad),7);for(uint64_t x:c.w)write_u64_le(out,x);}std::cout<<"replay worker="<<worker<<" scanned="<<scanned<<" candidate_hits="<<hits<<(partial?" PARTIAL":" COMPLETE")<<"\n";
}
static std::vector<Cell> load_replay(fs::path const&d,int worker,uint64_t C,int workers,uint64_t&scanned,bool&partial){std::ifstream in(replay_file(d,worker),std::ios::binary);char magic[8];in.read(magic,8);if(std::memcmp(magic,"C84RPL1\0",8))throw std::runtime_error("bad replay magic");uint64_t c=read_u64_le(in),w=read_u64_le(in),ws=read_u64_le(in);scanned=read_u64_le(in);char pp;in.get(pp);partial=pp;char pad[7];in.read(pad,7);if(c!=C||w!=uint64_t(worker)||ws!=uint64_t(workers))throw std::runtime_error("replay header mismatch");std::vector<Cell>v(C*3);for(auto&x:v){x.count=read_u64_le(in);char n;in.get(n);x.nw=uint8_t(n);in.read(pad,7);for(auto&q:x.w)q=read_u64_le(in);if(x.nw>13)throw std::runtime_error("bad witnesses");}char extra;if(in.read(&extra,1))throw std::runtime_error("extra replay bytes");return v;}

static Field direct_prod(Model const&m,std::array<int,7> const&k){Field x=fone();for(int t=0;t<7;t++)x=fmul(x,m.st[t][k[t]].u);return x;}
static void emit_rep_json(std::ostream&o,Model const&m,uint64_t code,int indent){
    uint32_t li=uint32_t(code>>23),ri=uint32_t(code&((1u<<23)-1));auto kl=decodeL(li);auto kr=decodeR(ri);std::array<int,7>k={kl[0],kl[1],kl[2],kr[0],kr[1],kr[2],kr[3]};u128 le=left_exp(m,li),re=right_exp(m,ri),e=addmod(le,re);Field lp=fpow(m.g,le),rp=fpow(m.g,re),full=fpow(m.g,e);if(fmul(lp,rp)!=full||direct_prod(m,k)!=full)throw std::runtime_error("packet direct product mismatch");int lc=m.L[li].color,rc=m.R[ri].color;if((lc+rc)%16!=4)throw std::runtime_error("packet color mismatch");std::string sp(indent,' ');
    o<<sp<<"{\"left_index\":"<<li<<",\"right_index\":"<<ri<<",\"left_exponent\":\""<<u128_dec(le)<<"\",\"right_exponent\":\""<<u128_dec(re)<<"\",\"left_product_coeffs\":"<<field_json(lp)<<",\"right_product_coeffs\":"<<field_json(rp)<<",\"full_product_coeffs\":"<<field_json(full)<<",\"left_color\":"<<lc<<",\"right_color\":"<<rc<<",\"total_color\":4,\"slots\":[";
    for(int t=0;t<7;t++){auto const&s=m.st[t][k[t]];if(t)o<<",";o<<"{\"slot\":"<<(t+1)<<",\"k\":"<<k[t]<<",\"i\":"<<int(s.type)<<",\"a\":"<<int(s.a)<<",\"color\":"<<int(s.color)<<",\"u_coeffs\":"<<field_json(s.u)<<",\"u_dlog\":\""<<u128_dec(s.log)<<"\"}";}o<<"]}";
}

static void cmd_finalize(fs::path d,int workers){
    Model m;auto cand=load_candidates(d);std::vector<Cell>sum(cand.size()*3);uint64_t total_scanned=0;
    for(int w=0;w<workers;w++){uint64_t sc;bool part;auto v=load_replay(d,w,cand.size(),workers,sc,part);if(part)throw std::runtime_error("partial replay cannot certify");total_scanned+=sc;for(size_t i=0;i<v.size();i++){sum[i].count+=v[i].count;for(int j=0;j<v[i].nw&&sum[i].nw<13;j++)sum[i].w[sum[i].nw++]=v[i].w[j];}}
    if(total_scanned!=P0_COUNT)throw std::runtime_error("replay total != P0");uint64_t mmax=1;u128 failE=0;size_t failcell=std::numeric_limits<size_t>::max();
    struct Fiber{u128 e;uint64_t n;};std::vector<Fiber>fib;
    for(size_t i=0;i<cand.size();i++){uint64_t proj=0;for(int h=0;h<3;h++){Cell const&c=sum[3*i+h];proj+=c.count;if(c.count>=2){u128 e=u128(cand[i].fp)+(u128(h)<<64);if(e>=GROUP_N)throw std::runtime_error("count on invalid exponent");fib.push_back({e,c.count});}if(c.count>mmax)mmax=c.count;if(c.count>=13&&(failcell==std::numeric_limits<size_t>::max()||u128(cand[i].fp)+(u128(h)<<64)<failE)){failcell=3*i+h;failE=u128(cand[i].fp)+(u128(h)<<64);}}
        if(proj!=cand[i].count)throw std::runtime_error("candidate replay count != projected run count");
    }
    std::sort(fib.begin(),fib.end(),[](Fiber const&a,Fiber const&b){return a.e<b.e;});Sha256 fsha;fs::create_directories(d/"certificate");std::ofstream fb(d/"certificate"/"nontrivial_fibers.bin",std::ios::binary);for(auto const&x:fib){uint8_t e9[9];for(int i=0;i<9;i++)e9[i]=uint8_t(x.e>>(8*i));fb.write(reinterpret_cast<char*>(e9),9);write_u64_le(fb,x.n);fsha.update(e9,9);sha_update_u64_le(fsha,x.n);}std::string fh=fsha.hex();
    if(failcell!=std::numeric_limits<size_t>::max()){
        Cell&c=sum[failcell];if(c.nw<13)throw std::runtime_error("missing 13 witnesses");std::vector<uint64_t>w(c.w.begin(),c.w.begin()+13);std::sort(w.begin(),w.end());Field common=fpow(m.g,failE);std::ofstream o(d/"certificate"/"FAIL_13_packet.json");o<<"{\n  \"version\": \""<<VERSION<<"\",\n  \"decision\": \"THIRTEEN_FOLD_PACKET_FOUND\",\n  \"common_exponent\": \""<<u128_dec(failE)<<"\",\n  \"common_exponent_low64\": "<<lo64(failE)<<",\n  \"common_exponent_high2\": "<<int(hi2(failE))<<",\n  \"common_product_coeffs\": "<<field_json(common)<<",\n  \"representations\": [\n";for(int j=0;j<13;j++){emit_rep_json(o,m,w[j],4);o<<(j==12?"\n":",\n");}o<<"  ]\n}\n";std::cout<<"FAIL 13-fold packet exponent="<<u128_dec(failE)<<"\n";return;
    }
    std::ofstream o(d/"certificate"/"PASS_mmax.json");o<<"{\n  \"version\": \""<<VERSION<<"\",\n  \"decision\": \"MMAX_LE_12_CERTIFIED\",\n  \"m_max_exact\": "<<mmax<<",\n  \"threshold\": 13,\n  \"P0\": "<<P0_COUNT<<",\n  \"field_N\": \""<<u128_dec(GROUP_N)<<"\",\n  \"generator_coeffs\": "<<field_json(m.g)<<",\n  \"eta_coeffs\": "<<field_json(m.eta)<<",\n  \"beta_coeffs\": "<<field_json(m.beta)<<",\n  \"state_table_sha256\": \""<<m.state_sha<<"\",\n  \"L_table_sha256\": \""<<m.L_sha<<"\",\n  \"R_table_sha256\": \""<<m.R_sha<<"\",\n  \"fingerprint_definition\": \"low 64 bits of the unique exponent E in [0,N)\",\n  \"repeated_fingerprint_count\": "<<cand.size()<<",\n  \"nontrivial_exact_fiber_count\": "<<fib.size()<<",\n  \"nontrivial_fibers_sha256\": \""<<fh<<"\",\n  \"reduce_manifest\": \"../reduce/manifest.json\",\n  \"proof_obligation\": \"every exact repeated exponent has a repeated low64 fingerprint; all repeated fingerprints were replayed exactly and their projected counts reconciled\"\n}\n";std::cout<<"PASS exact m_max="<<mmax<<"\n";
}

static void usage(){std::cerr<<"Usage:\n  cycle84 selftest OUT.json\n  cycle84 emit DIR WORKER WORKERS [MAX_PAIRS=0]\n  cycle84 reduce-shard DIR SHARD WORKERS\n  cycle84 merge-reduce DIR WORKERS\n  cycle84 replay DIR WORKER WORKERS [MAX_PAIRS=0]\n  cycle84 finalize DIR WORKERS\n";}
int main(int argc,char**argv){try{if(argc<2){usage();return 2;}std::string cmd=argv[1];if(cmd=="selftest"&&argc==3)cmd_selftest(argv[2]);else if(cmd=="emit"&&(argc==5||argc==6))cmd_emit(argv[2],std::stoi(argv[3]),std::stoi(argv[4]),argc==6?std::stoull(argv[5]):0);else if(cmd=="reduce-shard"&&argc==5)cmd_reduce_shard(argv[2],std::stoi(argv[3]),std::stoi(argv[4]));else if(cmd=="merge-reduce"&&argc==4)cmd_merge_reduce(argv[2],std::stoi(argv[3]));else if(cmd=="replay"&&(argc==5||argc==6))cmd_replay(argv[2],std::stoi(argv[3]),std::stoi(argv[4]),argc==6?std::stoull(argv[5]):0);else if(cmd=="finalize"&&argc==4)cmd_finalize(argv[2],std::stoi(argv[3]));else{usage();return 2;}return 0;}catch(std::exception const&e){std::cerr<<"ERROR: "<<e.what()<<"\n";return 1;}}
