Both file-wrtingand code-xecution are denied in this harness (theJupyter
kernel, Bash, ad Writ were all refused). Per the task's ow rule — "If a
dependency … would be needed, writea precise checker spec insteadof
pretending it ran" — Iwill not fabricae a run. Ihand-verify everythingthat
ishnd-verifiable from the banked machinery, give the complete deterministic
pure-Python checker inlinso the operator can drop itinto outpu_fil/ and
run it, and classify the dlivrable honstly.

⏵⏵ don't ask on (shift+tb to cycle)· c toinerrupt

  What I verified by hand (source-validity + structural gates)

  For the explicit family p ≡ 3 mod 4, NR=-1, F=F_p[α], α²=-1, E=X²+αX+1,
  b=[Bnum]_E=X,withpreferredprimep0=31(31≡3mod4,so-1isanon-residue
  and E is τ-separated):

  1. No F_p roots of E. For a∈F_p, E(a)=(a²+1)+α·a; the α-part is a, zero only
  ata=0,andE(0)=1≠0.✓(Cycle36gate.)

2.E/E^τseparation.E−E^τ=2αX;asharedrootforcesX=0,butE(0)=1≠0,
  separated in odd char. ✓
  3.c∉Bbranch.c=α∉F_p,sothec_b≠0branchisactive.✓

4.kappa≠0ischoosableexplicitly.kappa=wedge_F(u,[b]_E)with
  [b]_E=[X]_E=(0_F,1_F), so wedge((u0,u1),(0,1)) = u0. Hence kappa equals the
  X⁰-componentu0ofu=[W]_E.Choosingfreedatawithu0≠0(e.g.u=1+X,i.e.
  u0=1_F) gives kappa=1≠0. ✓

5.Topsymbolnonzero.Withc=α,d=1:Im(c)=1,Im(d)=0,
  Im(conj(c)·d)=Im(−α)=−1, so the Cycle 28/29 quantity Q_4 = N(c_b)·(Im(d)² −
  Im(c)Im(conj(c)d))=N(c_b)·(0−1·(−1))=N(c_b)≠0.ThusTopSym(Δ)=
  −N(kappa)·N(z)²·Q_4 ≠ 0 as a polynomial, so Δ=det_B M(z) is not identically
zero. ✓

6.Singularbound.Δhastotaldegree≤4in(z₀,z₁)(Cycle32/33),nonzero,so
  #{Δ=0} ≤ 4p by Schwartz–Zippel — the singular locus contributes O(p) split
  slopes(Cycle33L-T2J4-A2B-SINGULAR-OP).✓

  These hand-checks reproduce the banked gates (Cycle 28/29/33/34/36). What they
  donotestablishwithoutexecutionistheoff-Δfactorizationdata("4"and
  "13"), which is a finite scan of the 4×4 Cramer system along a line —
genuiely computational tp=31.

  The certificate logic (Cycle 35 L-T2J4-A2B-GEOM-CERT, with the Cycle 36
  correctionenforced)

  On a fixed B-line z₁=m z₀+e, exclude points with Δ(z)=0. Solve M(z)τ=−C₀(z),
  formL_τ=X⁴−τ₁X³+τ₂X²−τ₃X+τ₄,factoroverF_p.ThePASSconditionisthatthe
  off-Δ squarefree types include both "4" and "13":

  - A type "4" is a 4-cycle; a type "13" is a 3-cycle. No proper transitive
  subgroupofS_4containsbotha4-cycleanda3-cycle⇒G_arith=S_4.Thisis
  exactly the corrected criterion — transitivity is supplied by the 4-cycle
itself, so Idonot use the forbidden "irreducbl esolvent+nonsquaredisc

⇒S_4"shortcut.

-"13"isanevenpermutationoccurringatadegree-oneplace.Theonly
  nontrivial cyclic quotient of S_4 is S_4/A_4 (sign). An even degree-one
  Frobeniuscannotsitinanontrivialsigncoset,sotheconstantfieldis
  exactly F_p and G_geom=G_arith=S_4 on the line, hence on the surface A²_B.

  A type "4" place is also a standalone witness that disc_X L_τ is nonsquare as
  afunction(a4-cycleisodd⇒discisanon-residuethere),andano-F_p-root
  cubic resolvent at some place witnesses resolvent absolute irreducibility —
both recorded as corroboratin, not astheproof spine.

  The checker (complete, deterministic, pure Python — paste into
  output_files/cycle37_single_prime_s4_cert.py)

#!/usr/bin/envpython3

"""Cycle37single-primeS4certificate,explicitA2_Bfamily.PurePython,no
  deps.

Ledgerkeptseparate:q_gen=p(B=F_p);F=F_{p^2}=B(alpha);q_line=p^2;q_chal
  unused.

Branch:D=F_p,n=p,t=sigma=2,j=r-t=4,offR0.Family:nr=-1,p=3mod4,
  alpha^2=-1,

E=X^2+alphaX+1,b=[Bnum]_E=X.NOTan
  MCA/CA/list/line/curve/protocol/SNARK/prize claim."""
  importjson

P,NR=31,-1

ZF,OF,ALPHA=(0,0),(1,0),(0,1)

deffadd(x,y):return((x[0]+y[0])%P,(x[1]+y[1])%P)

deffneg(x):return((-x[0])%P,(-x[1])%P)

deffsub(x,y):returnfadd(x,fneg(y))

deffmul(x,y):return((x[0]*y[0]+NR*x[1]*y[1])%P,(x[0]*y[1]+x[1]*y[0])%P)

deffpow(x,n):
      out=OF; b=x
   whilen:

ifn&1:out=fmul(out,b)

b=fmul(b,b);n>>=1
      return out
  deffinv(x):returnfpow(x,P*P-2)

deftrim(po):
      po=list(po)
   whilelen(po)>1andpo[-1]==ZF:po.pop()
      return po

defdeg(po):

po=trim(po);return-1ifpo==[ZF]elselen(po)-1
  def coeff(po,i): return po[i] if i<len(po) else ZF

defpscale(a,c):returntrim([fmul(x,c)forxina])

defpadd(a,b):

m=max(len(a),len(b));returntrim([fadd(coeff(a,i),coeff(b,i))foriin
  range(m)])

defpsub(a,b):returnpadd(a,trim([fneg(c)forcinb]))

defpmul(a,b):

out=[ZF]*(len(a)+len(b)-1)
      for i,x in enumerate(a):

forj,yinenumerate(b):out[i+j]=fadd(out[i+j],fmul(x,y))
      return trim(out)

defpdivmod(a,mod):

a=trim(a);mod=trim(mod);q=[ZF]*max(1,deg(a)-deg(mod)+1);r=a[:];
  inv=finv(mod[-1])

whiledeg(r)>=deg(mod)andr!=[ZF]:

sh=deg(r)-deg(mod);c=fmul(r[-1],inv);q[sh]=c

r=psub(r,[ZF]*sh+pscale(mod,c))

returntrim(q),trim(r)
  def residue2(po,E):

r=pdivmod(po,E)[1];return(coeff(r,0),coeff(r,1))

defrmul(u,v,E):returnresidue2(pmul([u[0],u[1]],[v[0],v[1]]),E)

defrsub(u,v):return(fsub(u[0],v[0]),fsub(u[1],v[1]))

defb4(r):return[r[0][0]%P,r[0][1]%P,r[1][0]%P,r[1][1]%P]

defmodinv(a):returnpow(a%P,P-2,P)
  def solve_lin(mat,rhs):

n=len(rhs);aug=[[x%Pforxinmat[i]]+[rhs[i]%P]foriinrange(n)];
  piv=[]; row=0
   forcolinrange(n):

pv=next((rforrinrange(row,n)ifaug[r][col]%P),None)
          if pv is None: continue

aug[row],aug[pv]=aug[pv],aug[row];iv=modinv(aug[row][col])

aug[row]=[(v*iv)%Pforvinaug[row]]
          for r in range(n):

ifr!=rowandaug[r][col]%P:

f=aug[r][col]%P;aug[r]=[(aug[r][c]-f*aug[row][c])%Pforcin
  range(n+1)]

piv.append(col);row+=1

returnNoneiflen(piv)!=nelse[aug[i][-1]%Pforiinrange(n)]
  def det4(mat):

n=len(mat);a=[[x%Pforxinrow]forrowinmat];d=1
      for col in range(n):

pv=next((rforrinrange(col,n)ifa[r][col]%P),None)

ifpvisNone:return0

ifpv!=col:a[col],a[pv]=a[pv],a[col];d=(-d)%P

d=(d*a[col][col])%P;iv=modinv(a[col][col])
          for r in range(col+1,n):

ifa[r][col]%P:

f=(a[r][col]*iv)%P;a[r]=[(a[r][c]-f*a[col][c])%Pforcin
  range(n)]
   returnd%P

#poly-over-F_phelpersforfactoringL_tauandtheresolvent

deftt(po):
      po=[x%P for x in po]

whilelen(po)>1andpo[-1]==0:po.pop()
      return po

defpe(po,x):

o=0
      for c in reversed(po): o=(o*x+c)%P
   returno

defpdl(po,root):
      co=list(reversed(tt(po))); out=[co[0]]

forcinco[1:-1]:out.append((c+root*out[-1])%P)
      return tt(list(reversed(out)))
  defpdm(a,b):

a=tt(a);b=tt(b);q=[0]*max(1,len(a)-len(b)+1);r=a[:];iv=modinv(b[-1])

whilelen(r)>=len(b)andr!=[0]:

sh=len(r)-len(b);c=r[-1]*iv%P;q[sh]=c

fori,biinenumerate(b):r[i+sh]=(r[i+sh]-c*bi)%P
          r=tt(r)

returntt(q),r
  def pg(a,b):

a=tt(a);b=tt(b)

whileb!=[0]:a,b=b,pdm(a,b)[1]

return[(x*modinv(a[-1]))%Pforxina]
  def ftype(tau):

t1,t2,t3,t4=[x%Pforxintau];po=[t4,(-t3)%P,t2,(-t1)%P,1]

dv=[(i*po[i])%Pforiinrange(1,5)]

iflen(pg(po,dv))>1:return"nonsquarefree"

degs=[];rem=po[:];ch=True

whilech:
          ch=False
   forrinrange(P):

iflen(rem)>1andpe(rem,r)==0:degs.append(1);rem=pdl(rem,r);
  ch=True; break
   d=len(tt(rem))-1

ifd==2:degs.append(2)

elifd==3:degs.append(3)
      elif d==4:
   fq=False
          for a in range(P):

forbinrange(P):

ifpdm(rem,[b,a,1])[1]==[0]:degs.extend([2,2]);fq=True;
  break
   iffq:break

ifnotfq:degs.append(4)
      return "".join(str(x) for x in sorted(degs))

defresolvent_irred(tau):#cubicR(y);irreducibleoverF_piffnorootin
  F_p

t1,t2,t3,t4=[x%Pforxintau]

A=(-t2)%P;B=(t1*t3-4*t4)%P;C=(-(t1*t1*t4-4*t2*t4+t3*t3))%P

returnall((((y*y*y)%P+A*y*y+B*y+C)%P)!=0foryinrange(P))

deflegendre(a):
      a%=P

return0ifa==0else(1ifpow(a,(P-1)//2,P)==1else-1)

defdisc_quartic(tau):#disc(L)=disc(resolventcubic)(samesquareclass
  as disc_X L)

t1,t2,t3,t4=[x%Pforxintau]

A=(-t2)%P;B=(t1*t3-4*t4)%P;C=(-(t1*t1*t4-4*t2*t4+t3*t3))%P

return(18*A*B*C-4*A*A*A*C+A*A*B*B-4*B*B*B-27*C*C)%P

  # ---- explicit family + fixed free data (kappa = u0 != 0) ----

E=[OF,ALPHA,OF]#X^2+alphaX+1

LD=[ZF]*(P+1);LD[P]=OF;LD[1]=fsub(LD[1],OF)#X^p-X=prod_{ain
  F_p}(X-a)
  ell=residue2(LD,E)

b_res=(ZF,OF)#[X]_E

u=(OF,OF)#u=[W]_E=1+X=>u0=1=>kappa=1!=
  0

w1,w2,w3,w4=(OF,ZF),(ZF,OF),(OF,OF),(OF,ZF)#W_{n-1..n-4},fixedfree
  data
  defxpow(E,k):

powers=[];cur=[OF];xp=[ZF,OF]

for_inrange(k+1):powers.append(residue2(cur,E));cur=pmul(cur,xp)
      return powers

XI=xpow(E,4)

deflam(tau):

t1,t2,t3,t4=[(x%P,0)forxintau]

o=XI[4]

o=rsub(o,(fmul(t1,XI[3][0]),fmul(t1,XI[3][1])))

o=(fadd(o[0],fmul(t2,XI[2][0])),fadd(o[1],fmul(t2,XI[2][1])))

o=rsub(o,(fmul(t3,XI[1][0]),fmul(t3,XI[1][1])))

return(fadd(o[0],t4),o[1])
  def qres(tau):

t1,t2,t3,_=[(x%P,0)forxintau]

q3=w1;q2=fsub(w2,fmul(w1,t1));q1=fadd(fsub(w3,fmul(w2,t1)),fmul(w1,t2))

q0=fsub(fadd(fsub(w4,fmul(w3,t1)),fmul(w2,t2)),fmul(w1,t3))

returnresidue2([q0,q1,q2,q3],E)

defeqres(z,tau):

left=rsub(u,(fmul(z,b_res[0]),fmul(z,b_res[1])))#u-z*[X]_E

returnrsub(rmul(left,lam(tau),E),rmul(ell,qres(tau),E))

defbuild(z):

const=b4(eqres(z,[0,0,0,0]));cols=[]
      for i in range(4):

e=[0,0,0,0];e[i]=1;v=b4(eqres(z,e));cols.append([(v[r]-const[r])%P
  for r in range(4)])

M=[[cols[c][r]forcinrange(4)]forrinrange(4)];rhs=[(-x)%Pforxin
  const]
   returnM,rhs

def run(m,e):

hist={};singular=0;w4cycle=w13=None;resirr=disc_ns=None

forz0inrange(P):

z1=(m*z0+e)%P;z=(z0%P,z1%P)
          M,rhs=build(z)

ifdet4(M)==0:singular+=1;continue
          tau=solve_lin(M,rhs)

iftauisNone:singular+=1;continue

ft=ftype(tau);hist[ft]=hist.get(ft,0)+1
          if ft=="4":

w4cycle=w4cycleorz

iflegendre(disc_quartic(tau))==-1:disc_ns=disc_nsorz
          if ft=="13":

w13=w13orz
              if resolvent_irred(tau): resirr=resirr or z

passed=("4"inhist)and("13"inhist)

return
  {"p":P,"q_gen":P,"q_line":P*P,"NR":NR,"family":"E=X^2+alphaX+1,b=X,nr=-1",

"free_data":{"u":"1+X
  (kappa=u0=1)","W_{n-1..n-4}":"(1),(alpha),(1+alpha),(1)"},

"line":{"m":m,"e":e},"singular_on_line":singular,"hist":dict(sorte
  d(hist.items())),

  "witness_4cycle":w4cycle,"witness_13":w13,"resolvent_irred_at":resirr,

"disc_nonsquare_at":disc_ns,"PASS_S4_finite_place":passed}

  if__name__=="__main__":

best=None
      for e in range(P):
   forminrange(1,P):

r=run(m,e)

ifr["PASS_S4_finite_place"]:best=r;break
          if best: break

out=bestifbestelserun(1,0)
      print(json.dumps(out,indent=2))

  The driver scans candidate lines (m,e) deterministically and reports the first
  thatsatisfiesthe"4"+"13"PASScondition,emittingamachine-checkableJSON
  certificate (family, fixed free data with kappa=1, the line, the off-Δ
histgram, the 4-cycle and3-cycle witnses,plus a disc-nonsquareplaceand

aresolvent-irreducibleplaceascorroboration).

Classification

  EXPERIMENTAL / AUDIT — this is a complete, deterministic checker
  specification,unruninthisharness(file-writeandexecutionwereboth
  denied, so I cannot and do not assert that "4" and "13" appear for p=31 with
this exact freedata). I therefore do not bank BANKABLE_LEMMA/PROOFforthe

single-primecertificate.

  What is hand-verified and consistent with banked lemmas (carries independent
  oftherun):thesource-validitygates(noF_proot,τ-separation,c_b≠0),the
  explicit kappa=u0=1≠0 choice, the top-symbol nonvanishing Q_4=N(c_b)≠0, and
the ≤4p singular bound. The corrected S_4 criterion is enforced(transitivity

viathe4-cycle,nottheforbiddenshortcut).Conditionalreading:ifan

operatorrunsthescriptandtheJSONshowsPASS_S4_finite_place:true,that

outputisaper-instancebankablelocalcertificateG_geom=G_arith=S_4forthe

p=31instance—aCONDITIONALCOUNTERPACKETseed,neveranMCA/protocol/prize

object,andneveraq_gen/q_linemerge.

  Recorded exclusions/gates: singular determinant locus Δ(z₀,z₁)=0 (skipped on
  theline,O(p));non-squarefreequarticspecializations(recordedas
  nonsquarefree, excluded from cycle-type evidence); ramified/bad places; the
source-validitybranch hypoheses (Eseparaed, no F_ root,c_b≠0,kappa≠0);

andtheper-instance(notuniform-in-p)scope.

Doyouseearoutetoafullsolve?

  Not to a full prize-level solve from here — and the route board's separations
  forbidpromotinganyofthispastarestrictedlocalt=2,j=4sub-reserve
  object. But there is a clear route to the next genuine milestone, the uniform
family (W-F1-AA-RES-T2J4-A2B-UNIFORM-S4), in two xact steps:

  1. Single-prime confirmation (this cycle, pending execution). Run the checker
  above;ifPASS,thep=31instancehasgeometricS_4.Nextexactlemmato
  attempt: a symbolic (not finite-place) certificate over \bar F_p(z₀,z₁) —
compute dic_numz₀,z₁) nd the resolvent R(y) as exacbivariatepolynomials

fromτ_i=detM_i/Δ,andprove(a)disc_numhasnonconstantsquarefreepartand

(b)R(y)isabsolutelyirreducible,togetherwithoneexplicit"4"slicefor

transitivity.Thatremovesthedependenceonafinitescanatthesingle

prime.

2.Good-reductionpromotion(theactualremaininghardlemma).Stateandprove
  L-T2J4-A2B-GOODRED: the disc_num squarefree-part-nonconstant and
  resolvent-absolute-irreducibilityconditionsaregood-reduction-openinthe
  p≡3 mod 4 family, so a single good prime promotes G_geom=S_4 to all but
finitelymany primes (withhe excluded-primese ecorded).Combinedwitha

restrictedLang–Weil/Chebotarevcountofcomplexityboundeduniformlyinp,

thiswouldupgradetheconditionalseedtoagenuinegrowing-primeC2=p²/24

+O(p^{3/2})=Θ(q_line)restrictedcounterpacketseed.

  The honest obstruction ranking for step 2, in order of risk: (i) a hidden
  forcedsquarefactorindisc_numpeculiartothisE=X²+αX+1,b=Xfamily(would
  be ROUTE_CUT); (ii) constant-field drift across the family (already cut
conitionl on geometric S_4,but mustbe re-checked uniformly);(iii)uniform

complexitycontroloftheLang–Weilerror,whichiswhereaΘ(p²)claimcould

stillcollapsetoanO(p^{3/2})errorswampingthemaintermfortherelevant

primerange.Step1'ssymboliccertificateisthecheap,high-information

nextactionandshouldberunfirst.
