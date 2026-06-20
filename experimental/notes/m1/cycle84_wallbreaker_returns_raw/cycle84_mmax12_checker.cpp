#include <algorithm>
#include <array>
#include <atomic>
#include <cassert>
#include <cerrno>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <limits>
#include <mutex>
#include <numeric>
#include <optional>
#include <sstream>
#include <stdexcept>
#include <string>
#include <thread>
#include <unordered_map>
#include <utility>
#include <vector>
#include <sys/mman.h>
#include <unistd.h>

using u128 = unsigned __int128;
using i128 = __int128;

static u128 parse_u128(const std::string& s) {
    u128 x = 0;
    for (char c : s) {
        if (c < '0' || c > '9') throw std::runtime_error("bad decimal u128");
        x = x * 10 + static_cast<unsigned>(c - '0');
    }
    return x;
}
static std::string dec(u128 x) {
    if (x == 0) return "0";
    std::string s;
    while (x) { s.push_back(char('0' + x % 10)); x /= 10; }
    std::reverse(s.begin(), s.end());
    return s;
}

static constexpr int P = 17;
static constexpr int DEG = 16;
static const u128 GROUP_N = parse_u128("48661191875666868480");
static const u128 GROUP_HALF = GROUP_N / 2;
static const u128 EXPECTED_KAPPA = parse_u128("28612129440766144972");
static const u128 EXPECTED_DELTA = parse_u128("14306064720383072486");
static constexpr uint64_t FULL_P0 = 52747567104ULL;
static constexpr uint64_t FOLDED_P0 = 26373783552ULL;
static constexpr uint64_t HASH_SEED = 0x6a09e667f3bcc909ULL;

struct FE {
    std::array<uint8_t, DEG> a{};
    bool operator==(const FE& o) const { return a == o.a; }
    bool operator!=(const FE& o) const { return !(*this == o); }
};
static FE fe_one() { FE x; x.a[0] = 1; return x; }
static FE fe_emb(int c) { FE x; c %= P; if (c < 0) c += P; x.a[0] = uint8_t(c); return x; }
static FE fe_add(const FE& x, const FE& y) {
    FE z; for (int i=0;i<DEG;i++) z.a[i] = uint8_t((x.a[i] + y.a[i]) % P); return z;
}
static FE fe_sub(const FE& x, const FE& y) {
    FE z; for (int i=0;i<DEG;i++) z.a[i] = uint8_t((int(x.a[i]) - int(y.a[i]) + P) % P); return z;
}
static FE fe_neg(const FE& x) { return fe_sub(FE{}, x); }
static FE fe_mul(const FE& x, const FE& y) {
    int t[31]{};
    for (int i=0;i<DEG;i++) if (x.a[i])
        for (int j=0;j<DEG;j++) if (y.a[j])
            t[i+j] = (t[i+j] + int(x.a[i]) * int(y.a[j])) % P;
    for (int d=30; d>=16; --d) {
        int c = t[d] % P;
        if (c) {
            t[d-8] = (t[d-8] - c) % P; if (t[d-8] < 0) t[d-8] += P;
            t[d-16] = (t[d-16] - 3*c) % P; if (t[d-16] < 0) t[d-16] += P;
        }
        t[d] = 0;
    }
    FE z; for (int i=0;i<DEG;i++) z.a[i] = uint8_t((t[i] % P + P) % P); return z;
}
static FE fe_pow(FE a, u128 e) {
    FE r = fe_one();
    while (e) { if (e & 1) r = fe_mul(r,a); a = fe_mul(a,a); e >>= 1; }
    return r;
}
static u128 fe_pack(const FE& x) {
    u128 z=0; for (int i=DEG-1;i>=0;--i) z = z*P + x.a[i]; return z;
}
static FE beta_fe() { FE x; x.a[0]=2; x.a[1]=1; return x; }
static FE eta_fe() { FE x; x.a[9]=6; return x; }
static FE generator_fe() { FE x; x.a[0]=1; x.a[1]=1; return x; }

static int mod_pow_int(int a, int e, int m) {
    int r=1; while(e){ if(e&1) r=int((1LL*r*a)%m); a=int((1LL*a*a)%m); e>>=1; } return r;
}
static int64_t egcd(int64_t a, int64_t b, int64_t& x, int64_t& y) {
    if (!b) { x=1; y=0; return a; }
    int64_t x1,y1; int64_t g=egcd(b,a%b,x1,y1); x=y1; y=x1-(a/b)*y1; return g;
}
static uint64_t inv_mod_u64(uint64_t a, uint64_t m) {
    int64_t x,y; int64_t g=egcd((int64_t)a,(int64_t)m,x,y);
    if (g!=1) throw std::runtime_error("noninvertible CRT modulus");
    int64_t r=x%(int64_t)m; if(r<0)r+=m; return (uint64_t)r;
}

static constexpr int S_COLOR[4] = {0,15,9,12};
static constexpr int PCOEFF[3][9] = {
    {6,4,4,10,5,4,0,0,1},
    {14,13,14,12,5,9,0,0,1},
    {4,12,1,5,0,11,0,0,1}
};
static FE poly_eval(int i, const FE& z) {
    FE r{}; for (int j=8;j>=0;--j) r=fe_add(fe_mul(r,z),fe_emb(PCOEFF[i-1][j])); return r;
}
static int color_of_k(int k) {
    int i=k/16+1, a=k%16; return (S_COLOR[i] + 8*(a&1)) & 15;
}
static int tau_k(int k) {
    int i=k/16+1, a=k%16;
    if(i==1) return 16 + ((a+6)&15);
    if(i==2) return ((a+10)&15);
    return 32 + ((a+8)&15);
}
static std::array<std::array<FE,48>,7> build_slot_values() {
    std::array<std::array<FE,48>,7> u{};
    FE eta=eta_fe(), beta=beta_fe(), xi=fe_pow(beta,2), einv=fe_pow(eta,GROUP_N-1);
    for(int t=1;t<=7;t++) {
        FE ef=fe_pow(einv,2*t);
        for(int k=0;k<48;k++) {
            int i=k/16+1, a=k%16;
            int scalar=mod_pow_int(3,(-a)&15,P);
            FE arg=fe_mul(fe_mul(xi,fe_emb(scalar)),ef);
            FE v=poly_eval(i,arg); if(a&1) v=fe_neg(v);
            if(v==FE{}) throw std::runtime_error("zero slot value");
            u[t-1][k]=v;
        }
    }
    return u;
}

struct DLogSolver {
    uint64_t q=0, m=0;
    FE factor{};
    std::vector<std::pair<u128,uint32_t>> baby;
};
static std::array<uint64_t,7> prime_powers() { return {256,9,5,29,18913,41761,184417}; }
static std::array<uint64_t,7> distinct_primes() { return {2,3,5,29,18913,41761,184417}; }
static std::vector<DLogSolver> build_dlog_solvers(const FE& g) {
    std::vector<DLogSolver> out;
    for(uint64_t q: prime_powers()) {
        DLogSolver s; s.q=q; s.m=(uint64_t)std::sqrt((long double)q)+1;
        FE G=fe_pow(g,GROUP_N/q), cur=fe_one();
        s.baby.reserve(s.m);
        for(uint64_t j=0;j<s.m;j++){ s.baby.push_back({fe_pack(cur),(uint32_t)j}); cur=fe_mul(cur,G); }
        std::sort(s.baby.begin(),s.baby.end(),[](auto&a,auto&b){return a.first<b.first;});
        FE invG=fe_pow(G,q-1); s.factor=fe_pow(invG,s.m); out.push_back(std::move(s));
    }
    return out;
}
static u128 dlog_ph(const FE& h, const FE& g, const std::vector<DLogSolver>& solvers) {
    std::array<uint64_t,7> residues{}; std::array<uint64_t,7> mods=prime_powers();
    for(size_t z=0;z<solvers.size();z++) {
        const auto& s=solvers[z]; FE cur=fe_pow(h,GROUP_N/s.q); bool found=false;
        for(uint64_t i=0;i<=s.m && !found;i++) {
            u128 key=fe_pack(cur);
            auto it=std::lower_bound(s.baby.begin(),s.baby.end(),key,[](auto&a,u128 b){return a.first<b;});
            if(it!=s.baby.end() && it->first==key) {
                uint64_t x=i*s.m+it->second; if(x<s.q){residues[z]=x;found=true;break;}
            }
            cur=fe_mul(cur,s.factor);
        }
        if(!found) throw std::runtime_error("Pohlig-Hellman failed");
    }
    u128 x=0, M=1;
    for(size_t i=0;i<mods.size();i++) {
        uint64_t q=mods[i], xr=(uint64_t)(x%q), Mr=(uint64_t)(M%q);
        uint64_t diff=(residues[i]+q-xr)%q;
        uint64_t t=(u128(diff)*inv_mod_u64(Mr,q))%q;
        x += M*t; M *= q;
    }
    x%=GROUP_N;
    if(fe_pow(g,x)!=h) throw std::runtime_error("dlog verification failed");
    return x;
}

struct Model {
    FE g{};
    std::array<std::array<FE,48>,7> u{};
    std::array<std::array<u128,48>,7> elog{};
    std::array<u128,7> tau_const{};
    u128 kappa=0, delta=0;
};
static Model build_model() {
    Model m; m.g=generator_fe(); m.u=build_slot_values();
    for(uint64_t p: distinct_primes()) if(fe_pow(m.g,GROUP_N/p)==fe_one()) throw std::runtime_error("g is not primitive");
    auto solvers=build_dlog_solvers(m.g);
    for(int t=0;t<7;t++) for(int k=0;k<48;k++) m.elog[t][k]=dlog_ph(m.u[t][k],m.g,solvers);
    for(int t=0;t<7;t++) {
        u128 c=(m.elog[t][0]+m.elog[t][tau_k(0)])%GROUP_N;
        for(int k=0;k<48;k++) if((m.elog[t][k]+m.elog[t][tau_k(k)])%GROUP_N!=c)
            throw std::runtime_error("tau slot constant mismatch");
        m.tau_const[t]=c; m.kappa=(m.kappa+c)%GROUP_N;
    }
    if(m.kappa!=EXPECTED_KAPPA || (m.kappa&1)) throw std::runtime_error("unexpected kappa");
    m.delta=m.kappa/2; if(m.delta!=EXPECTED_DELTA) throw std::runtime_error("unexpected delta");
    return m;
}

static inline u128 add_mod(u128 a,u128 b){u128 z=a+b; if(z>=GROUP_N)z-=GROUP_N; return z;}
static inline u128 sub_mod(u128 a,u128 b){return a>=b?a-b:a+GROUP_N-b;}
static inline uint64_t mix64(uint64_t z){z^=z>>30;z*=0xbf58476d1ce4e5b9ULL;z^=z>>27;z*=0x94d049bb133111ebULL;return z^(z>>31);}
static inline uint64_t hash_key(u128 q){uint64_t lo=(uint64_t)q,hi=(uint64_t)(q>>64);return mix64(lo^(hi*0x9e3779b97f4a7c15ULL)^HASH_SEED);}
static inline uint64_t mulhi_range(uint64_t h,uint64_t n){return (uint64_t)((u128(h)*n)>>64);}

struct LeftRec { u128 shifted; uint32_t id; uint8_t color; };
struct RightRec { u128 e; uint32_t id; };
struct Sides { std::vector<LeftRec> L; std::array<std::vector<RightRec>,16> R; std::array<uint64_t,16> lc{},rc{}; };
static Sides build_sides(const Model& m) {
    Sides s;
    for(int k1=0;k1<48;k1++) if(k1<tau_k(k1)) for(int k2=0;k2<48;k2++) for(int k3=0;k3<48;k3++) {
        u128 e=add_mod(add_mod(m.elog[0][k1],m.elog[1][k2]),m.elog[2][k3]);
        uint8_t c=(color_of_k(k1)+color_of_k(k2)+color_of_k(k3))&15;
        uint32_t id=(k1*48+k2)*48+k3;
        s.L.push_back({sub_mod(e,m.delta),id,c}); s.lc[c]++;
    }
    for(int k4=0;k4<48;k4++) for(int k5=0;k5<48;k5++) for(int k6=0;k6<48;k6++) for(int k7=0;k7<48;k7++) {
        u128 e=add_mod(add_mod(m.elog[3][k4],m.elog[4][k5]),add_mod(m.elog[5][k6],m.elog[6][k7]));
        uint8_t c=(color_of_k(k4)+color_of_k(k5)+color_of_k(k6)+color_of_k(k7))&15;
        uint32_t id=(((k4*48+k5)*48+k6)*48+k7);
        s.R[c].push_back({e,id}); s.rc[c]++;
    }
    if(s.L.size()!=55296) throw std::runtime_error("left size mismatch");
    uint64_t rn=0,pairs=0; for(int c=0;c<16;c++){rn+=s.R[c].size();pairs+=s.lc[c]*s.rc[(4-c)&15];}
    if(rn!=5308416 || pairs!=FOLDED_P0) throw std::runtime_error("side/pair count mismatch");
    return s;
}

static inline uint64_t pair_id(uint32_t l,uint32_t r){return (uint64_t(l)<<23)|r;}
static inline void decode_pair(uint64_t p,std::array<int,7>& k){
    uint32_t r=p&((1u<<23)-1), l=p>>23;
    k[3]=r/(48*48*48); r%=48*48*48; k[4]=r/(48*48);r%=48*48;k[5]=r/48;k[6]=r%48;
    k[0]=l/(48*48);l%=48*48;k[1]=l/48;k[2]=l%48;
}
static u128 tuple_exp(const Model&m,const std::array<int,7>&k){u128 e=0;for(int t=0;t<7;t++)e=add_mod(e,m.elog[t][k[t]]);return e;}
static int tuple_color(const std::array<int,7>&k){int c=0;for(int x:k)c=(c+color_of_k(x))&15;return c;}
static std::array<int,7> tau_tuple(std::array<int,7> k){for(int&i:k)i=tau_k(i);return k;}

struct Screen {
    uint8_t* mem=nullptr; uint64_t bytes=0,buckets=0; bool compacted=false;
    explicit Screen(uint64_t nbytes):bytes(nbytes),buckets(nbytes*2) {
        mem=(uint8_t*)mmap(nullptr,bytes,PROT_READ|PROT_WRITE,MAP_PRIVATE|MAP_ANONYMOUS,-1,0);
        if(mem==MAP_FAILED){mem=nullptr;throw std::runtime_error("mmap screen failed");}
#ifdef MADV_HUGEPAGE
        madvise(mem,bytes,MADV_HUGEPAGE);
#endif
    }
    ~Screen(){if(mem)munmap(mem,bytes);}
    void increment(uint64_t b){
        uint8_t* p=mem+(b>>1); unsigned sh=(b&1)?4:0; uint8_t old=__atomic_load_n(p,__ATOMIC_RELAXED);
        for(;;){unsigned v=(old>>sh)&15; if(v>=13)return;uint8_t neu=(old&~(uint8_t(15)<<sh))|uint8_t((v+1)<<sh);
            if(__atomic_compare_exchange_n(p,&old,neu,true,__ATOMIC_RELAXED,__ATOMIC_RELAXED))return;}
    }
    uint64_t compact_to_saturated_bits(){
        if(compacted)throw std::runtime_error("double compact"); uint64_t outbytes=(buckets+7)/8,sat=0;
        for(uint64_t o=0;o<outbytes;o++){
            uint8_t z=0; uint64_t base=o*4;
            for(int j=0;j<4;j++){uint8_t x=mem[base+j];if((x&15)>=13){z|=uint8_t(1u<<(2*j));sat++;}if((x>>4)>=13){z|=uint8_t(1u<<(2*j+1));sat++;}}
            mem[o]=z;
        }
        uint64_t page=(uint64_t)sysconf(_SC_PAGESIZE),keep=((outbytes+page-1)/page)*page;
        if(keep<bytes){munmap(mem+keep,bytes-keep);bytes=keep;}
        compacted=true; return sat;
    }
    bool saturated(uint64_t b)const{return (mem[b>>3]>>(b&7))&1;}
};

struct Entry { uint8_t count=0; uint64_t first=0; uint32_t tail=std::numeric_limits<uint32_t>::max(); };
struct Node { uint64_t pair=0; uint32_t prev=std::numeric_limits<uint32_t>::max(); };
struct MapShard { std::mutex mu; std::unordered_map<uint64_t,Entry> map; std::vector<Node> nodes; };
struct Failure { bool found=false; u128 q=0; bool selfdual=false; std::vector<uint64_t> pairs; };

struct RunStats { uint64_t pairs=0; uint64_t hsum=0,hxor=0,candidate_records=0; };
static void merge_stats(RunStats& a,const RunStats&b){a.pairs+=b.pairs;a.hsum+=b.hsum;a.hxor^=b.hxor;a.candidate_records+=b.candidate_records;}

struct Options { bool full=false,setup_only=true; unsigned threads=std::max(1u,std::thread::hardware_concurrency()); uint64_t screen_mib=3072; uint64_t left_limit=0; uint64_t map_cap=60000000; };
static Options parse_args(int argc,char**argv){Options o;for(int i=1;i<argc;i++){std::string a=argv[i];auto need=[&](){if(++i>=argc)throw std::runtime_error("missing argument");return std::string(argv[i]);};
    if(a=="--full"){o.full=true;o.setup_only=false;}else if(a=="--setup-only"){o.setup_only=true;}else if(a=="--threads")o.threads=std::stoul(need());
    else if(a=="--screen-mib")o.screen_mib=std::stoull(need());else if(a=="--left-limit"){o.left_limit=std::stoull(need());o.full=false;o.setup_only=false;}
    else if(a=="--map-cap")o.map_cap=std::stoull(need());else throw std::runtime_error("unknown arg "+a);}return o;}

static void print_model_json(const Model&m,const Sides&s,const std::string&decision){
    std::cout<<"{\n  \"decision\": \""<<decision<<"\",\n  \"field\": {\"p\":17,\"degree\":16,\"modulus\":[3,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],\"eta\":[0,0,0,0,0,0,0,0,0,6],\"beta\":[2,1]},\n";
    std::cout<<"  \"group_order\": \""<<dec(GROUP_N)<<"\",\n  \"generator\": [1,1],\n  \"kappa\": \""<<dec(m.kappa)<<"\",\n  \"delta\": \""<<dec(m.delta)<<"\",\n";
    std::cout<<"  \"left_records\": "<<s.L.size()<<",\n  \"right_records\": 5308416,\n  \"folded_compatible_records\": "<<FOLDED_P0<<"\n}\n";
}

static void emit_failure(const Model&m,const Failure&f){
    u128 target=add_mod(m.delta,f.q); std::vector<std::array<int,7>> out;
    if(!f.selfdual){
        for(uint64_t pid:f.pairs){std::array<int,7>k;decode_pair(pid,k);u128 x=sub_mod(tuple_exp(m,k),m.delta);if(x!=f.q)k=tau_tuple(k);if(tuple_exp(m,k)!=target)throw std::runtime_error("normalization failed");out.push_back(k);}
    }else{
        for(uint64_t pid:f.pairs){std::array<int,7>k;decode_pair(pid,k);out.push_back(k);if(out.size()<13)out.push_back(tau_tuple(k));if(out.size()>=13)break;}
    }
    if(out.size()<13)throw std::runtime_error("insufficient failure witnesses");out.resize(13);FE prod=fe_pow(m.g,target);
    std::cout<<"{\n  \"decision\": \"THIRTEEN_FOLD_PACKET_FOUND\",\n  \"folded_key\": \""<<dec(f.q)<<"\",\n  \"common_product_log\": \""<<dec(target)<<"\",\n  \"common_product_coefficients\": [";
    for(int i=0;i<16;i++){if(i)std::cout<<",";std::cout<<int(prod.a[i]);}std::cout<<"],\n  \"witnesses\": [\n";
    for(size_t j=0;j<out.size();j++){auto&k=out[j];if(tuple_color(k)!=4||tuple_exp(m,k)!=target)throw std::runtime_error("bad emitted witness");std::cout<<"    {\"k\":[";for(int t=0;t<7;t++){if(t)std::cout<<",";std::cout<<k[t];}std::cout<<"],\"ia\":[";for(int t=0;t<7;t++){if(t)std::cout<<",";std::cout<<"["<<(k[t]/16+1)<<","<<(k[t]%16)<<"]";}std::cout<<"],\"slot_colors\":[";for(int t=0;t<7;t++){if(t)std::cout<<",";std::cout<<color_of_k(k[t]);}std::cout<<"]}"<<(j+1==out.size()?"\n":",\n");}
    std::cout<<"  ]\n}\n";
}

int main(int argc,char**argv){
    try{
        Options opt=parse_args(argc,argv);Model model=build_model();Sides sides=build_sides(model);
        if(opt.setup_only){print_model_json(model,sides,"SETUP_VERIFIED");return 0;}
        uint64_t Luse=opt.left_limit?std::min<uint64_t>(opt.left_limit,sides.L.size()):sides.L.size();
        bool theorem_run=opt.full&&Luse==sides.L.size();
        uint64_t screen_bytes=opt.screen_mib<<20; if(screen_bytes<4096||screen_bytes>=(1ULL<<63))throw std::runtime_error("bad screen size");
        Screen screen(screen_bytes);std::atomic<uint64_t> next{0};std::atomic<bool> stop{false};std::mutex self_mu;std::array<std::vector<uint64_t>,2> self_pairs;std::vector<RunStats> ts(opt.threads);
        auto pass1=[&](unsigned tid){RunStats st;for(;;){uint64_t li=next.fetch_add(1);if(li>=Luse||stop.load())break;const auto&l=sides.L[li];const auto&rv=sides.R[(4-l.color)&15];for(const auto&r:rv){if(stop.load(std::memory_order_relaxed))break;u128 x=add_mod(l.shifted,r.e);u128 q=x<=GROUP_HALF?x:GROUP_N-x;uint64_t pid=pair_id(l.id,r.id);st.pairs++;uint64_t hh=hash_key(q);st.hsum+=hh;st.hxor^=hh;
                    if(q==0||q==GROUP_HALF){int z=q==0?0:1;std::lock_guard<std::mutex>g(self_mu);if(self_pairs[z].size()<7)self_pairs[z].push_back(pid);if(self_pairs[z].size()>=7)stop.store(true);}
                    else {uint64_t b=mulhi_range(hh,screen.buckets);screen.increment(b);} }}ts[tid]=st;};
        std::vector<std::thread> pool;for(unsigned t=0;t<opt.threads;t++)pool.emplace_back(pass1,t);for(auto&t:pool)t.join();RunStats s1;for(auto&x:ts)merge_stats(s1,x);
        if(stop.load()){Failure f;f.found=true;f.selfdual=true;int z=self_pairs[0].size()>=7?0:1;f.q=z==0?0:GROUP_HALF;f.pairs=self_pairs[z];emit_failure(model,f);return 1;}
        if(theorem_run&&s1.pairs!=FOLDED_P0)throw std::runtime_error("pass1 pair count mismatch");
        uint64_t saturated=screen.compact_to_saturated_bits();
        std::array<MapShard,256> shards;std::atomic<uint64_t> map_size{0};next.store(0);stop.store(false);std::mutex fail_mu;Failure failure;ts.assign(opt.threads,{});
        auto pass2=[&](unsigned tid){RunStats st;for(;;){uint64_t li=next.fetch_add(1);if(li>=Luse||stop.load())break;const auto&l=sides.L[li];const auto&rv=sides.R[(4-l.color)&15];for(const auto&r:rv){if(stop.load(std::memory_order_relaxed))break;u128 x=add_mod(l.shifted,r.e);u128 q=x<=GROUP_HALF?x:GROUP_N-x;st.pairs++;uint64_t hh=hash_key(q);st.hsum+=hh;st.hxor^=hh;if(q==0||q==GROUP_HALF)continue;uint64_t b=mulhi_range(hh,screen.buckets);if(!screen.saturated(b))continue;st.candidate_records++;uint8_t sh=(uint8_t)(q>>57);uint64_t key=(uint64_t)q&((1ULL<<57)-1);auto&ms=shards[sh];std::lock_guard<std::mutex>g(ms.mu);auto[it,ins]=ms.map.try_emplace(key,Entry{1,pair_id(l.id,r.id),std::numeric_limits<uint32_t>::max()});if(ins){uint64_t n=map_size.fetch_add(1)+1;if(n>opt.map_cap){stop.store(true);continue;}}else{Entry&e=it->second;if(e.count<13){ms.nodes.push_back({pair_id(l.id,r.id),e.tail});e.tail=(uint32_t)(ms.nodes.size()-1);e.count++;if(e.count==13){std::vector<uint64_t> ps;ps.push_back(e.first);uint32_t at=e.tail;while(at!=std::numeric_limits<uint32_t>::max()){ps.push_back(ms.nodes[at].pair);at=ms.nodes[at].prev;}std::lock_guard<std::mutex>fg(fail_mu);if(!failure.found){failure.found=true;failure.q=(u128(sh)<<57)|key;failure.pairs=std::move(ps);stop.store(true);}}}} }}ts[tid]=st;};
        pool.clear();for(unsigned t=0;t<opt.threads;t++)pool.emplace_back(pass2,t);for(auto&t:pool)t.join();RunStats s2;for(auto&x:ts)merge_stats(s2,x);
        if(failure.found){emit_failure(model,failure);return 1;}
        if(map_size.load()>opt.map_cap){std::cout<<"{\"decision\":\"RESOURCE_EXHAUSTED_NO_CLAIM\",\"exact_key_cap\":"<<opt.map_cap<<"}\n";return 2;}
        if(theorem_run&&(s2.pairs!=FOLDED_P0||s1.hsum!=s2.hsum||s1.hxor!=s2.hxor))throw std::runtime_error("pass digest mismatch");
        uint8_t mx=0;uint64_t exact_keys=0;for(auto&ms:shards){exact_keys+=ms.map.size();for(auto&kv:ms.map)mx=std::max(mx,kv.second.count);}
        std::cout<<"{\n  \"decision\": \""<<(theorem_run?"MMAX_LE_12_CERTIFIED":"SMOKE_ONLY_NO_THEOREM_CLAIM")<<"\",\n";
        std::cout<<"  \"full_domain\": "<<(theorem_run?"true":"false")<<",\n  \"folded_records_per_pass\": "<<s1.pairs<<",\n  \"screen_bytes\": "<<screen_bytes<<",\n  \"screen_buckets\": "<<screen.buckets<<",\n  \"saturated_buckets\": "<<saturated<<",\n";
        std::cout<<"  \"refined_records\": "<<s2.candidate_records<<",\n  \"refined_exact_keys\": "<<exact_keys<<",\n  \"refined_max_count\": "<<int(mx)<<",\n  \"selfdual_orbit_counts\": ["<<self_pairs[0].size()<<","<<self_pairs[1].size()<<"],\n";
        std::cout<<"  \"hash_seed\": \"0x6a09e667f3bcc909\",\n  \"pass_hash_sum\": \"0x"<<std::hex<<s1.hsum<<"\",\n  \"pass_hash_xor\": \"0x"<<s1.hxor<<std::dec<<"\"\n}\n";
        return 0;
    }catch(const std::exception&e){std::cerr<<"ERROR: "<<e.what()<<"\n";return 3;}
}
