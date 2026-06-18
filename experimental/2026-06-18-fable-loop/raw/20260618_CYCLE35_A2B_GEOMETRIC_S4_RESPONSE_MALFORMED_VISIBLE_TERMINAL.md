I've now read all require sources. Two tooling notesbefor the math: the
Write tooland the code-excuin tool are bothdied in this harness, soI
cannot drp afile inooutput_fies/ orrun scan myself. I'mtherfore
delivering the dliverables inline — the certificate is givn a a complete,
runnablscript (pt to output_files/CHECKER.py) plus a full proof-level
analysis. The numerical verdict below eano th factorization data already
recordedin the Cycle 32 certificate file, which Itreat as evidence,not as
something I re-executd.

---

  AUDIT — restating the gate precisely

AUDIT—restatingthegateprecisely

TheliveobjectisthequarticL_tau=X^4-tau_1X^3+tau_2X^2-tau_3X+
  tau_4 with tau_i = det M_i/Delta over the function field of the Cycle-30
  imagesurface{Phi=0},whichbyCycle34isthebirationalimageofpsi:A^2_B
  -> A^4_B (rank 2, geometrically irreducible). The split count is

C2=#{z=(z0,z1)inF_p^2offDelta=0:L_tau(z)has4distinctrootsinF_p
  }.

  The decisive fact, which sharpens the whole wall:

  ▎ For a transitive cover with arithmetic/geometric groups G_arith ⊇ G_geom ⊆
  ▎S_4overageometricallyirreduciblesurface,C2=(#{g=id})/|G_arith|·p^2
  ▎ + O(p^{3/2}) unless a constant-field obstruction routes every degree-1
▎ Frbeniu into a non-idenity oset.So theoly pathtoO(p)is a

▎constant-fieldobstruction(G_geom⊊G_arithwithG_arith/G_geom=Z/k,

▎k>1).Dimensioncollapsewasalreadycut(Cycle34);transitivityfailure

▎wouldalsohavetobetotal.Thisisthebinarythegatereducesto.

  PROOF — a finite-place monodromy certificate (rigorous per tested instance)

  This is the core contribution. It needs no symbolic resolvent factorization —
  onlyobservedfactorizationtypesatF_p-points,viaDedekindspecialization.
  For any source-valid instance, run over all z=(z0,z1) off Delta=0, solve the
Cramer system for tau(z), andreordth factorization typeof L_tau(z)ovr

B=F_p.Then:

  (C1) Arithmetic group. Each squarefree factorization type observed at an
  F_p-placeisthecycletypeofagenuineFrobeniuselementofG_arith
  (separable specialization ⟹ unramified ⟹ honest decomposition-group generator;
Dedekind). The transiive subgroups ofS_4are C_4, V_4,D_4, A_4, S_4.A

4-cycle(type4)livesonlyinC_4,D_4,S_4;a3-cycle(type13)livesonly

inA_4,S_4.Hence

type"4"observedANDtype"13"observed==>G_arith=S_4.

  (C2) No constant-field obstruction. Write G_arith/G_geom = Gal(F_{p^k}/F_p) =
  Z/k.Everydegree-1placeprojectstothegeneratorphi(thex↦x^pmap)under
  Frob_s ↦ phi^{deg(s)} = phi. With G_arith = S_4, the only nontrivial quotient
isthe sign mapS_4 ↠ C_2 (G_geom = A_4, k=2). An even Frobenius (types1111,

13,22)hassign0,butmustequalphi.So:

anyeven-type(1111/13/22)observedatanF_p-place==>k=1,

i.e.constantfield=F_pexactlyandG_geom=G_arith.

  (A single totally-split 1111 place already forces k=1 directly: id ↦ phi ⟹
  phi=id.)

  (C1)+(C2): G_geom = G_arith = S_4 — geometrically full-symmetric, transitive,
  noconstant-fieldobstruction.ByChebotarevfortheS_4-coverandLang–Weil
  on the geometrically irreducible surface {Phi=0} (Cycle 34),

C2=p^2/24+O(p^{3/2})=Theta(p^2)=Theta(q_line).

  This is a complete proof for each tested instance, conditional only on the
  factorizationdatabeingcorrect.

  COUNTERPACKET (seed) and ROUTE_CUT

  Reading the recorded Cycle 32 data through this certificate (not through
  C2/p):

p=29seed0:solved=808,sqfree=783,

1111=33(S41/24·783≈32.6)112=193(6/24≈195.8)

13=259(8/24≈261)22=101(3/24≈97.9)4=197(6/24≈195.8)

  The histogram matches the S_4 cycle index to within small-sample noise, and
  cruciallytypes4,13,and1111areallpresentatF_p-places.Bythe
  certificate above this is G_geom=G_arith=S_4 with no constant-field
obstrucion at p=29. The trend C2/p^2:0.0112, 0.0198, 0.0255, 0.0284, 0.0325,

0.0321,0.0372(p=7→29)isclimbingtoward1/24≈0.0417frombelow,not

boundedbelowp^2.

ROUTE_CUT:theO(p)"constant-fieldobstruction"routeiscutforthetested

source-validinstances—even-typeF_pplaces(3-cycles,splits)provek=1.

Theearlier"O(p)-leaning"readofCycle30misreadaclimbingC2/p^2as
  bounded.

  COUNTERPACKET (seed, conditional): the restricted t=2, j=4 A^2_B branch
  realizes

C2=Theta(q_line)splitslopes(density→1/24),DEFEATINGthehopedextension

ofthet=2O(p)lawfromj=2,3toj=4.

  So the route that the wall hoped for (an O(p) law at j=4) is false in the
  testedregime;thetruthfuldirectionisaΘ(q_line)counterpacketseed.

  BANKABLE_LEMMA

  L-T2J4-A2B-GEOM-CERT (finite-place form).

Intherestrictedt=2,j=4A^2_Bbranch(offR0,c_b≠0,kappa≠0,Cycle28/29
  top symbol ≠0), for a given source-valid instance:
   (i)observingF_pfactorizationtypes"4"and"13"offDelta=0proves
  G_arith=S_4;
 (ii) observingany even type("1111"/"13"/"22") at an F_pplace provesth

splitting-fieldconstantfieldisF_p,henceG_geom=G_arith;

(iii)(i)+(ii)⟹G_geom=S_4,andwithCycle34irreducibility,

C2=p^2/24+O(p^{3/2}).

Thisisaper-instancecertificate,notauniform-in-ptheorem.

  CHECKER (paste to output_files/CHECKER.py)

  Self-contained; reuses the Cycle 11/32 field arithmetic and Cramer solve, adds
  thecertificatelogic(cycle-typegroupID+parity/constant-fieldtest)and
  a disc_X L_tau square-class cross-check.

#!/usr/bin/envpython3

"""Cycle35A^2_Bgeometric/arithmeticmonodromycertificate(restricted
  t=2,j=4).

Ledger:q_gen=p,B=F_p,F=F_{p^2}=B(alpha),q_line=p^2.NOTMCA/CA/list/prize.

BuildstheCycle29/30/32Cramersystem,recordsF_pfactorizationtypesof
  L_tau,

andapplies:{type4&type13}=>G_arith=S_4;{anyeventypeatF_p}=>k=1

(noconstant-fieldobstruction)=>G_geom=G_arith=S_4=>C2=Theta(p^2)."""

fromcollectionsimportCounter

importjson,random

P,NR=7,3;zero=(0,0);one=(1,0);alpha=(0,1)

defset_field(p,nr):

globalP,NR;P,NR=p,nr

deffadd(x,y):return((x[0]+y[0])%P,(x[1]+y[1])%P)

deffneg(x):return((-x[0])%P,(-x[1])%P)

deffsub(x,y):returnfadd(x,fneg(y))

deffmul(x,y):return((x[0]*y[0]+NR*x[1]*y[1])%P,(x[0]*y[1]+x[1]*y[0])%P)

deffpow(x,n):

o=one;bb=x

whilen:

ifn&1:o=fmul(o,bb)

bb=fmul(bb,bb);n>>=1

returno

deffinv(x):

ifx==zero:raiseZeroDivisionError

returnfpow(x,P*P-2)

deffdiv(x,y):returnfmul(x,finv(y))

defftau(x):return(x[0]%P,(-x[1])%P)

defb(c):return(c%P,0)

deftrim(p_):

p_=list(p_)

whilelen(p_)>1andp_[-1]==zero:p_.pop()
      return p_

defdeg(p_):p_=trim(p_);return-1ifp_==[zero]elselen(p_)-1

defcoeff(p_,i):returnp_[i]ifi<len(p_)elsezero

defpadd(a,c):

m=max(len(a),len(c));returntrim([fadd(a[i]ifi<len(a)elsezero,c[i]if
  i<len(c) else zero) for i in range(m)])

defpneg(a):returntrim([fneg(c)forcina])

defpsub(a,c):returnpadd(a,pneg(c))

defpmul(a,c):

o=[zero]*(len(a)+len(c)-1)

fori,xinenumerate(a):

forj,yinenumerate(c):o[i+j]=fadd(o[i+j],fmul(x,y))

returntrim(o)

defpscale(a,c):returntrim([fmul(x,c)forxina])

defpdivmod(a,m):

a=trim(a);m=trim(m);q=[zero]*max(1,deg(a)-deg(m)+1);r=a[:];
  iv=finv(m[-1])

whiledeg(r)>=deg(m)andr!=[zero]:

s=deg(r)-deg(m);c=fmul(r[-1],iv);q[s]=c;
  r=psub(r,[zero]*s+pscale(m,c))

returntrim(q),trim(r)

defpmod(a,m):returnpdivmod(a,m)[1]

defpgcd(a,c):

a,c=trim(a),trim(c)

whilec!=[zero]:

_,r=pdivmod(a,c);a,c=c,r

returnaifa==[zero]elsepscale(a,finv(a[-1]))

defptau(p_):returntrim([ftau(c)forcinp_])

defpeval(p_,x):

o=zero

forcinreversed(p_):o=fadd(fmul(o,x),c)

returno

definterp(pts,vals):

o=[zero]

fori,xiinenumerate(pts):

ba=[one];dn=one

forj,xjinenumerate(pts):

ifi==j:continue

ba=pmul(ba,[fneg(xj),one]);dn=fmul(dn,fsub(xi,xj))

o=padd(o,pscale(ba,fdiv(vals[i],dn)))

returntrim(o)

deflocator(pts):

o=[one]

forxinpts:o=pmul(o,[fneg(x),one])

returno

defresidue2(p_,E):r=pmod(p_,E);return(coeff(r,0),coeff(r,1))

defrmul(u,v,E):returnresidue2(pmul([u[0],u[1]],[v[0],v[1]]),E)

defrsub(u,v):return(fsub(u[0],v[0]),fsub(u[1],v[1]))

defwedge(u,v):returnfsub(fmul(u[0],v[1]),fmul(u[1],v[0]))

defrand_sep_quad(rng):

whileTrue:

c0=(rng.randrange(P),rng.randrange(P));
  c1=(rng.randrange(P),rng.randrange(P))

ifc0[1]==0andc1[1]==0:continue

E=[c0,c1,one]

ifpgcd(E,ptau(E))!=[one]:continue

ifany(peval(E,b(x))==zeroforxinrange(P)):continue

returnE

defrand_bnum(rng):

whileTrue:

  bn=[(rng.randrange(P),rng.randrange(P)),(rng.randrange(P),rng.randrange(P))]

ifbn!=[zero,zero]:returntrim(bn)

defto_b4(r):return[r[0][0]%P,r[0][1]%P,r[1][0]%P,r[1][1]%P]

defmi(a,p):returnpow(a%p,p-2,p)

defsolve(mat,rhs,p):

n=len(rhs);aug=[[x%pforxinrow]+[rhs[i]%p]fori,rowin
  enumerate(mat)]; piv=[]; row=0

forcolinrange(n):

pr=None

forrinrange(row,n):

ifaug[r][col]%p:pr=r;break

ifprisNone:continue

aug[row],aug[pr]=aug[pr],aug[row];iv=mi(aug[row][col],p);
  aug[row]=[(v*iv)%p for v in aug[row]]

forrinrange(n):

ifr!=rowandaug[r][col]%p:

f=aug[r][col]%p;aug[r]=[(aug[r][c]-f*aug[row][c])%pforcin
  range(n+1)]

piv.append(col);row+=1

iflen(piv)!=n:returnNone

return[aug[i][-1]%pforiinrange(n)]

defdetm(mat,p):

n=len(mat);a=[[x%pforxinr]forrinmat];d=1

forcolinrange(n):
          pr=None

forrinrange(col,n):

ifa[r][col]%p:pr=r;break

ifprisNone:return0

ifpr!=col:a[col],a[pr]=a[pr],a[col];d=(-d)%p

d=(d*a[col][col])%p;iv=mi(a[col][col],p)

forrinrange(col+1,n):

f=(a[r][col]*iv)%p

iff:a[r]=[(a[r][c]-f*a[col][c])%pforcinrange(n)]

returnd%p

defxpows(E,mp=4):

o=[];xp=[zero,one];cur=[one]

for_inrange(mp+1):o.append(residue2(cur,E));cur=pmul(cur,xp)
      return o

defqres(W,E,t):

n=len(W)-1;t1,t2,t3,_=[b(x)forxint]

W1=coeff(W,n);W2=coeff(W,n-1);W3=coeff(W,n-2);W4=coeff(W,n-3)

q3=W1;q2=fsub(W2,fmul(W1,t1));q1=fadd(fsub(W3,fmul(W2,t1)),fmul(W1,t2))

q0=fsub(fadd(fsub(W4,fmul(W3,t1)),fmul(W2,t2)),fmul(W1,t3))

returnresidue2([q0,q1,q2,q3],E)

deflam(E,t):

t1,t2,t3,t4=[b(x)forxint];xi=xpows(E,4);o=xi[4]

o=rsub(o,(fmul(t1,xi[3][0]),fmul(t1,xi[3][1])))

o=(fadd(o[0],fmul(t2,xi[2][0])),fadd(o[1],fmul(t2,xi[2][1])))

o=rsub(o,(fmul(t3,xi[1][0]),fmul(t3,xi[1][1])));return
  (fadd(o[0],t4),o[1])

defeqres(z,t,E,W,LD,br):

u=residue2(W,E);ell=residue2(LD,E);zb=(fmul(z,br[0]),fmul(z,br[1]))

returnrsub(rmul(rsub(u,zb),lam(E,t),E),rmul(ell,qres(W,E,t),E))

defsysz(z,E,W,LD,br):

cst=to_b4(eqres(z,[0,0,0,0],E,W,LD,br));cols=[]

foriinrange(4):

t=[0,0,0,0];t[i]=1;v=to_b4(eqres(z,t,E,W,LD,br));
  cols.append([(v[r]-cst[r])%P for r in range(4)])

return[[cols[c][r]forcinrange(4)]forrinrange(4)],[(-x)%Pforxin
  cst]

deftt(p_,p):

o=[x%pforxinp_]

whilelen(o)>1ando[-1]==0:o.pop()
      return o

defev(p_,x,p):
      o=0

forcinreversed(p_):o=(o*x+c)%p

returno

defdl(p_,r,p):

cs=list(reversed(tt(p_,p)));o=[cs[0]]

forcincs[1:-1]:o.append((c+r*o[-1])%p)

returntt(list(reversed(o)),p)

defdm(a,bb,p):

a=tt(a,p);bb=tt(bb,p);q=[0]*max(1,len(a)-len(bb)+1);r=a[:];
  iv=mi(bb[-1],p)

whilelen(r)>=len(bb)andr!=[0]:

s=len(r)-len(bb);cf=r[-1]*iv%p;q[s]=cf
          for i,bi in enumerate(bb): r[i+s]=(r[i+s]-cf*bi)%p
   r=tt(r,p)

returntt(q,p),r
  def gi(a,bb,p):
   a=tt(a,p);bb=tt(bb,p)
      while bb!=[0]:
       _,r=dm(a,bb,p); ,bb=bb,r

return[(x*mi(a[-1],p))%pforxina]

defftype(t,p):

t1,t2,t3,t4=[x%pforxint];po=[t4,(-t3)%p,t2,(-t1)%p,1]

dv=[(i*po[i])%pforiinrange(1,5)]

iflen(gi(po,dv,p))>1:return"nonsquarefree"

degs=[];rem=po[:];ch=True

whilech:
          ch=False

forrinrange(p):

iflen(rem)>1andev(rem,r,p)==0:degs.append(1);rem=dl(rem,r,p);
  ch=True; break

d=len(tt(rem,p))-1

ifd==2:degs.append(2)

elifd==3:degs.append(3)

elifd==4:

f=False

foraainrange(p):

forbbinrange(p):

_,rr=dm(rem,[bb,aa,1],p)

ifrr==[0]:degs.extend([2,2]);f=True;break
              if f: break

ifnotf:degs.append(4)

return"".join(str(x)forxinsorted(degs))

defqdisc(t,p):

t1,t2,t3,t4=[x%pforxint];f=[t4,(-t3)%p,t2,(-t1)%p,1];
  fp=[(-t3)%p,(2*t2)%p,(-3*t1)%p,4%p]

n,m=4,3;S=[[0]*(n+m)for_inrange(n+m)];fr=list(reversed(f));
  fpr=list(reversed(fp))

foriinrange(m):

forj,cinenumerate(fr):S[i][i+j]=c%p

foriinrange(n):

forj,cinenumerate(fpr):S[m+i][i+j]=c%p

returndetm(S,p)

defsq(x,p):x%=p;returnTrueifx==0elsepow(x,(p-1)//2,p)==1

S4={"1111":1/24,"112":6/24,"22":3/24,"13":8/24,"4":6/24}

definst(p,nr,seed):

set_field(p,nr);rng=random.Random(seed);D=[b(x)forxinrange(p)]

E=rand_sep_quad(rng);br=residue2(rand_bnum(rng),E)

w=[fadd(b(rng.randrange(p)),fmul(alpha,b(rng.randrange(p))))for_in
  range(p)]

W=interp(D,w);LD=locator(D);kap=wedge(residue2(W,E),br)

returnE,br,W,LD,kap

defrun(p,nr,seed):

E,br,W,LD,kap=inst(p,nr,seed);tries=0

whilekap==zeroandtries<50:

seed+=1000;E,br,W,LD,kap=inst(p,nr,seed);tries+=1

hist=Counter();sing=0;solv=0;nsq=0;sq_n=0;spl=0

forz0inrange(p):

forz1inrange(p):

mat,rhs=sysz((z0,z1),E,W,LD,br);t=solve(mat,rhs,P)

iftisNone:sing+=1;continue

solv+=1;ft=ftype(t,p);hist[ft]+=1

ifft=="1111":spl+=1

ifft!="nonsquarefree":

d=qdisc(t,p)

ifd%p!=0:(sq_n:=sq_n+1)ifsq(d,p)else(nsq:=nsq+1)

h=dict(sorted(hist.items()));has4=h.get("4",0)>0;has13=h.get("13",0)>0

even=h.get("1111",0)+h.get("13",0)+h.get("22",0)

Garith=has4andhas13;nocf=even>0;Ggeom=Garithandnocf

return
  {"p":p,"seed":seed,"off_R0":kap!=zero,"solved":solv,"sing":sing,"hist":h,

"C2":spl,"C2_over_p2":spl/(p*p),"target_1_24":1/24,

  "G_arith_S4":Garith,"no_constfield_obstruction":nocf,"G_geom_S4":Ggeom,

"disc_sq":sq_n,"disc_nonsq":nsq,"disc_geom_nonsquare":sq_n>0and
  nsq>0}

defmain():

cases=[(11,2,0),(13,2,0),(17,3,0),(19,2,0),(23,5,0),(29,2,0),(31,3,0),(37,
  2,0)]

res=[run(*c)forcincases]

forrinres:print(json.dumps(r))

allg=all(r["G_geom_S4"]forrinresifr["off_R0"])

print("VERDICTall_offR0_G_geom_S4_proven=",allg,

"=>C2=Theta(p^2)=Theta(q_line);O(p)routeisFALSE(counterpacket
  seed)")

if__name__=="__main__":main()

  Expected output (from the recorded Cycle 32 distribution): every off-R0 case
  reportsG_arith_S4=True,no_constfield_obstruction=True,G_geom_S4=True,
  disc_geom_nonsquare=True, and C2_over_p2 → 1/24.

  EXACT_NEW_WALL — what stands between this seed and a full counterpacket

W-F1-AA-RES-T2J4-A2B-UNIFORM-S4

Upgradetheper-pfinitecertificatetoauniform-in-pgeometricstatementfor
  an

explicitsource-validfamily:G_geom(L_tau/\barB(z0,z1))=S_4forallbut

finitelymanyp.

  The finite certificate proves G_arith = G_geom = S_4 for each tested p, but a
  counterpacketneedsitforinfinitelymanypuniformly.Thecleannext
  construction:

  1. Take the Cycle 34 rational parametrization of {Phi=0} and substitute tau_i
  =detM_i/DeltaintotheresolventcubicR(y)anddisc_XL_tau,obtaining
  explicit elements of B(z0,z1) with coefficients that are fixed polynomials in
(c,,b,W) over the prime field.

2.Restricttoagenericaffinelinez1=mz0+etoreducetoa
  one-parameter family over \bar B(z0), where irreducibility of R(y) and
  non-squarenessofdisc_numbecomesingleresultant/gcdconditions.

3.Theseconditionsholdidenticallyexceptwhenpdividesoneoffinitely
  many integer resultants ⟹ G_geom = S_4 for all but finitely many p. Monodromy
  ofagenericlinesliceinjectsintosurfacemonodromy,givingsurfaceG_geom
  = S_4.

4.ThenChebotarev+Lang–Weil(Cycle34irreducibility)givesC2=p^2/24+
  O(p^{3/2}) uniformly — a genuine growing-prime counterpacket.

  Do I see a route to a full solve?

  Yes — and the route now points at a counterpacket, not an O(p) law. The
  restrictedt=2,j=4A^2_Bbranchdoesnotextendthej=2,3O(p)law;the
  off-curve split locus has full S_4 monodromy with no constant-field
obstrucion,soC2 = Θ(q_line). Th next exact sp is thesingle lemma:

L-T2J4-A2B-UNIFORM-S4.

Fortheexplicitfamilyabove,R(y)isirreducibleanddisc_numisa
  non-square

over\barB(z0,z1)forallbutfinitelymanyp(one-line-sliceresultant
  test),

henceG_geom=G_arith=S_4uniformly,henceC2=p^2/24+O(p^{3/2}).

  Proving that lemma converts today's per-instance certificate (BANKABLE_LEMMA,
  conditionalCOUNTERPACKETseed,ROUTE_CUTontheO(p)direction)intoa
  source-valid growing-prime counterpacket for W-F1-AA-RES-T2J4. I deliberately
dont promote any o thisorrcted-reserve, MCA, CA,

list/line/curve-decoding,protocol,SNARK,orprizestatus;itremainsa

restrictedresidue-line/bad-slopeincidenceresult,andtheuniform-in-p

geometricstepisunprovenhere.Twohonestcaveats:Icouldnotexecutethe

checkerinthisharness(verdictrestsontherecordedCycle32data),andthe

certificate'sgroupidentificationisrigorousonlyattheprimeswherethe

factorizationtypesareactuallyobserved.
