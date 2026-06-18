I've completed the derivation nd erifiedit byhand against the banked Cycle
23identity.Cdexecutio and file wrtingarednied in this harness(same
constraint Cycls 19–23recorded), so I deliver thanalytic audit inline
with acopy-pasteablehecker, and everyload-bearingidentity is re-deived
from he banked Cycle 12/14/20/21 multipication table.

---

⏵⏵ don't ask on (shift+tb to cycle)· c toinerrupt     86% context used

  Primary label

Primarylabel

BANKABLE_LEMMA+ROUTE_CUT

  The nonsplit-c D-kernel lane W-F1-AA-RES-T2J3-D-KERNEL-NONSPLIT-C is empty
  underitsownhypotheses.TheresultalsounifiesCycle23intoonebasis-free
  identity.

Headline

  Off R0 (kappa = u wedge b != 0), in the restricted D=F_p, B=F_p, F=F_{p^2},
  t=sigma=2,j=3window,

D=N(ell)*kappa,N(ell)=prod_{ainF_p}E(a),

  where N is the norm (determinant of multiplication) on A=F[X]/E. Hence D=0 off
  R0happensiffEhasarootinB=F_p,whichisexactlytheconditionthatE
  is not separated. The wall hypothesis "E separated" therefore makes the
stratum empty —regardlessof in Bor c notin B.

Setup(source-checked,offR0)

E=X^2+cX+d,A=F[X]/E,xi=[X]_E,xi^2=-cxi-d,

u=[W]_E,b=[Bnum]_E,ell=[X^p-X]_E=[L_D]_E(D=F_p,soL_D=X^p-X),
  kappa=u wedge b,

xwedgey=x0y1-x1y0,

P_E(x,y)=x0y0-cx0y1+dx1y1.

  The conjugate of y=y0+y1 xi over F is ybar=(y0-c y1)-y1 xi (root swap xi ->
  xi^*=-c-xi).Themasteridentity,verifiedbydirectexpansionusingxi^2=-c
  xi-d:

x*ybar=P_E(x,y)-(xwedgey)xi.(MASTER)

  Q1 — closed form of ell for c notin B

  Put s := xi + c/2 (note c/2 in F, so this is legal whether or not c in B).
  Thens^2=c^2/4-d=:winF.Tworoutestos^pmustagreeinA:

freshman:s^p=(xi+c/2)^p=xi^p+(c/2)^p=(xi+ell)+c^p/2,

scalarpow:s^p=(s^2)^((p-1)/2)s=w^((p-1)/2)s=nus,
  nu:=w^((p-1)/2).

  Equating and solving for ell (with mu := nu - 1):

ell=mu*s+(c-c^p)/2=mu*(xi+c/2)+delta_c,

delta_c:=(c-c^p)/2=(c-c^tau)/2.

  In coordinates on {1,xi}, s=(c/2,1), so

ell=(mu*c/2+delta_c,mu),i.e.ell0=(nuc-c^p)/2,ell1=mu.

  delta_c is the imaginary part of c; it vanishes exactly when c in B,
  recoveringthebankedCycle23formell=mu*s.Sotheonlynewterminthe
  nonsplit-c lane is the additive Frobenius-defect delta_c.

Q2—Dasabilinearform

  Apply (MASTER) with z=ellbar: write u*ellbar=P+Q xi and b*ellbar=R+S xi where
  P=P_E(u,ell),Q=-(uwedgeell),R=P_E(b,ell),S=-(bwedgeell).Then

D=(ellwedgeb)P_E(u,ell)+P_E(b,ell)(uwedgeell)=SP-RQ=(u*ellbar)
  wedge (b*ellbar).

  Since wedge is an alternating F-bilinear 2-form on the rank-2 module A, any
  F-linearmapTscalesitbydetT;multiplicationbyellbarhasdet=
  N(ellbar)=N(ell). Therefore

D=N(ellbar)(uwedgeb)=N(ell)*kappa,N(ell)=P_E(ell,ell)=ell0^2-c
  ell0 ell1 + d ell1^2.

  All (u,b)-dependence sits in kappa; the (c,d)-dependence is the scalar N(ell).
  PolarizingNatell=mu*s+delta_c*1(thecrosstermB(s,1)=c/2-c/2=0
  drops out) gives the explicit gate scalar

N(ell)=delta_c^2-mu^2w,w=c^2/4-d.(LAMBDA)

  For c in B, delta_c=0 and N(ell)=-mu^2 w = -mu^2(c^2/4-d), so
  D=-mu^2(c^2/4-d)kappa—exactlythebankedCycle23identity,nowobtainedas
  a special case.

  The norm-as-resultant form is the decisive one. Since ell = prod_{a in
  F_p}[X-a]_EandNismultiplicative,N([X-a]_E)=E(a),so

N(ell)=prod_{ainF_p}E(a).(RES)

  (Cross-check of (LAMBDA)=(RES) for c in B: prod_{a}(a^2+ca+d)=prod_{t in
  F_p}(t^2-w)=-(beta-beta^p)^2=-w(w^{(p-1)/2}-1)^2=-mu^2w.Matches.)

  Q3 — joint solvability of {D=0, Delta1==0, off R0, c notin B}

  Not solvable when E is separated; the stratum is empty.

  From (RES), off R0:

D=0<=>N(ell)=0<=>prod_{ainF_p}E(a)=0<=>EhasarootainB=F_p.

  If E(a)=0 with a in F_p, then a^p=a and E^tau(a)=E^tau(a^p)=E(a)^p=0, so (X-a)
  |gcd(E,E^tau)andEisnotseparated.Contrapositive:

  E separated  ==>  E has no root in F_p  ==>  N(ell) != 0  ==>  D != 0   (off
  R0).

  So {D=0, off R0, E separated} is empty, and a fortiori its c notin B slice is
  empty.TheauxiliaryconditionsDelta1==0,c_b=-Q_E(b)/kappa!=0,W_{n-1}!=
  0 are never reached — emptiness is forced by D=0 + separated + off R0 alone.

  Within the c notin B lane this is sharp: for c notin B, a shared root of
  E,E^tauisforcedintoF_p(otherwisethesharedrootanditsFrobeniusimage
  would form a full Galois orbit, putting E^tau, hence c,d, in B[X] —
contradicting cnotn B). Thus on c notin B:

D=0(offR0)<=>Enotseparated<=>EhasarootinF_p.

  The D-kernel D=0 locus in the nonsplit-c lane is exactly the non-separated
  locusthewallexcludes.

  Q4 — split-cubic slope set on this lane

  Vacuous. Because {D=0, off R0, E separated, c notin B} has no source-valid
  point,thereisnoco-supportfamilytocount:theO(p)vs
  Omega(p^2)=Omega(q_line) dichotomy does not arise on this lane and no
Theta(q_line) counterpacket can be seedd here. Off theD=0lane (D!=0), the

controllinginvariantrevertstotheCycle16determinantQ(z_0,z_1),notD;D

contributesnonewdanger.

  Net banked implication

OffR0,restrictedD=F_p,t=sigma=2,j=3:

D=N(ell)*kappa,N(ell)=prod_{ainF_p}E(a)=delta_c^2-mu^2w,
    ell = mu*(xi+c/2)+delta_c,  mu=w^{(p-1)/2}-1,  w=c^2/4-d,
  delta_c=(c-c^p)/2.

Eseparated==>D!=0==>{D=0,offR0,Eseparated}empty,incl.cnotin
  B.

  This closes W-F1-AA-RES-T2J3-D-KERNEL-NONSPLIT-C as ROUTE_CUT and supersedes
  theCycle23cinBemptinessasacorollaryofoneidentity.

Banked vs not

  Bank (proven, exact, off R0, restricted window): (MASTER); the basis-free
  D=N(ell)*kappa;theclosedformell=mu*(xi+c/2)+delta_c;thegatescalar
  N(ell)=delta_c^2-mu^2 w; the resultant form N(ell)=prod_{a in F_p}E(a); the
equivalence D=0off R0 <=>E has a root inF_p <=> E notseparated; mptinss

of{D=0,offR0,Eseparated}anditscnotinBslice.

  Do not bank: any nonemptiness or split-count statement for a c notin B lane
  (nonesurvives);anyC2boundforthefullD=0branchbeyondthiswindow;any
  Theta(q_line) counterpacket; any corrected-reserve, q_gen, protocol,
list-/line-/curve-decoding, CA, MCA,or SNARKconseqence.The recovred

Delta1==0landingcriteriondelta_zinQR(F_p)isstillnotbanked.

Forbidden-upgradecompliance

  No Prize solve/disproof; eta=2/n stays sub-reserve; q_gen/q_line kept
  separate;noprotocoldenominatorsaving;nolist/line/CA/MCA/SNARKupgrade;
  no internet; no finite scan cited as proof.

  New live wall

  With both c in B (Cycle 23) and c notin B (this cycle) D-kernel lanes cut, the
  survivingD=0routeisgoneforseparatedE.Theoff-R0separatedwall
  returns to the Cycle 16 line:

W-F1-AA-RES-T2J3-RANK-DET-SPLIT(Q==0branch,distinctD-splitcubics
  retained).

  Since separated E forces D!=0, the rank/determinant analysis must proceed via
  Q(z_0,z_1)withdetM=(c_b/kappa^2)D!=0;thenextexacttaskiswhether
  Q==0 is compatible with det M != 0 on source-valid distinct-split data, or
whether thattoo collapsesO(p).

Checker(harnessdeniedWrite/execute—copytooutput_files/CHECKER.py)

Experimentalconsistencyharnessonly,notaproof.

#!/usr/bin/envpython3

"""Cycle24:W-F1-AA-RES-T2J3-D-KERNEL-NONSPLIT-Cconsistencychecker(NOTa
  proof).

Verifies,forB=F_p,F=F_{p^2},A=F[X]/(X^2+cX+d):

(1)ell=[X^p-X]_E=mu*(xi+c/2)+delta_c,mu=w^((p-1)/2)-1,w=c^2/4-d,
  delta_c=(c-c^p)/2;

(2)D=(ell^b)P_E(u,ell)+P_E(b,ell)(u^ell)=N(ell)*kappa;

(3)N(ell)=prod_{ainF_p}E(a)=delta_c^2-mu^2w;

(4)Eseparated(gcd(E,E^tau)=1)andkappa!=0=>D!=0(stratumempty),

andD=0offR0occursonlywhereEhasarootinF_p(non-separated).
  """
  from__future__importannotations

  def find_nonresidue(p):
   sq={(i*i)%pforiinrange(p)}
      for a in range(2,p):
       if anot in sq: return a

raiseValueError(p)

  # F=F_{p^2}=F_p[t]/(t^2-nr); element (x,y)=x+y t

deffadd(p,X,Y):return((X[0]+Y[0])%p,(X[1]+Y[1])%p)

deffsub(p,X,Y):return((X[0]-Y[0])%p,(X[1]-Y[1])%p)

deffmul(p,nr,X,Y):return
  ((X[0]*Y[0]+nr*X[1]*Y[1])%p,(X[0]*Y[1]+X[1]*Y[0])%p)
  deffpow(p,nr,X,e):

out=(1,0)
      while e:

ife&1:out=fmul(p,nr,out,X)

X=fmul(p,nr,X,X);e>>=1
      return out

defftau(p,X):return(X[0]%p,(-X[1])%p)#x->x^p
  def finv(p,nr,X):

n=(X[0]*X[0]-nr*X[1]*X[1])%p;ni=pow(n,p-2,p)

return((X[0]*ni)%p,((-X[1])*ni)%p)

  # A=F[X]/(X^2+cX+d); element (z0,z1)=z0+z1 xi, c,d,z0,z1 in F

defamul(p,nr,c,d,X,Y):

M=lambdaA,B:fmul(p,nr,A,B)

c0=fsub(p,M(X[0],Y[0]),M(d,M(X[1],Y[1])))

c1=fsub(p,fadd(p,M(X[0],Y[1]),M(X[1],Y[0])),M(c,M(X[1],Y[1])))

return(c0,c1)

defaxipow(p,nr,c,d,e):#[X^e]_E

out=((1,0),(0,0));base=((0,0),(1,0))
      while e:

ife&1:out=amul(p,nr,c,d,out,base)
          base=amul(p,nr,c,d,base,base); e>>=1

returnout

  def wedge(p,nr,X,Y): return fsub(p,fmul(p,nr,X[0],Y[1]),fmul(p,nr,X[1],Y[0]))

defPE(p,nr,c,d,X,Y):

M=lambdaA,B:fmul(p,nr,A,B)

returnfadd(p,fsub(p,M(X[0],Y[0]),M(c,M(X[0],Y[1]))),M(d,M(X[1],Y[1])))

  defseparated(p,nr,c,d):

ct,dt=ftau(p,c),ftau(p,d)

ifc==ctandd==dt:returnFalse#EinB[X],E=E^tau

ifc==ct:returnTrue#E-E^tau=d-d^pconst
  !=0

r=fmul(p,nr,fsub(p,dt,d),finv(p,nr,fsub(p,c,ct)))#uniquecommon-root
  candidate

Er=fadd(p,fadd(p,fmul(p,nr,r,r),fmul(p,nr,c,r)),d)

returnEr!=(0,0)

  defrun(p):

nr=find_nonresidue(p);inv2=pow(2,p-2,p);inv4=pow(4,p-2,p)

samples=[((1,0),(0,1)),((0,1),(1,0)),((1,1),(2,3)),((2,1),(1,4)),((3,2),(5
  ,1))]

checked=0;sep_off_R0=0;D0_offR0=0;D0_with_Fp_root=0

xi=((0,0),(1,0))

forc0inrange(p):

forc1inrange(p):#c1!=0=>cnotinB

c=(c0,c1);half_c=fmul(p,nr,c,(inv2,0));s=(half_c,(1,0))

ctau=ftau(p,c);delta_c=fmul(p,nr,fsub(p,c,ctau),(inv2,0))
          for d0 in range(p):
   ford1inrange(p):

d=(d0,d1)
              w=fsub(p,fmul(p,nr,fmul(p,nr,c,c),(inv4,0)),d)

ifw==(0,0):continue#doubleroot:
  separable-via-w edge, skip

nu=fpow(p,nr,w,(p-1)//2);mu=fsub(p,nu,(1,0))

ell_cf=(fadd(p,fmul(p,nr,mu,s[0]),delta_c),fmul(p,nr,mu,s[1]))

xip=axipow(p,nr,c,d,p);
  ell=(fsub(p,xip[0],xi[0]),fsub(p,xip[1],xi[1]))

assertell==ell_cf,(p,c,d,ell,ell_cf)#(1)

Nell=PE(p,nr,c,d,ell,ell)

prodE=(1,0)
              for a in range(p):

Ea=fadd(p,fadd(p,fmul(p,nr,(a,0),(a,0)),fmul(p,nr,c,(a,0))),d)

prodE=fmul(p,nr,prodE,Ea)

assertNell==prodE,(p,c,d,Nell,prodE)#(3)

  lam=fsub(p,fmul(p,nr,delta_c,delta_c),fmul(p,nr,fmul(p,nr,mu,mu),w))

assertlam==Nell,(p,c,d,lam,Nell)#
  (LAMBDA)

sep=separated(p,nr,c,d)

has_root=any(fadd(p,fadd(p,fmul(p,nr,(a,0),(a,0)),
                                         fmul(p,nr,c,(a,0))),d)==(0,0) for a in
  range(p))

for(u0,u1),(b0,b1)insamples:

u=((u0,u1%p),(u1,(u0+1)%p));b=((b0,(b1+1)%p),(b1,b0%p))

kappa=wedge(p,nr,u,b)

ifkappa==(0,0):continue

g1=wedge(p,nr,ell,b);g2=PE(p,nr,c,d,b,ell)

h1=wedge(p,nr,u,ell);h2=PE(p,nr,c,d,u,ell)

D=fadd(p,fmul(p,nr,g1,h2),fmul(p,nr,g2,h1))

assertD==fmul(p,nr,Nell,kappa),(p,c,d,u,b,D)#(2)

checked+=1
                  if sep:

assertD!=(0,0),(p,c,d,u,b)#(4)
  emptiness

sep_off_R0+=1
                  if D==(0,0):

D0_offR0+=1

ifhas_root:D0_with_Fp_root+=1

returndict(p=p,checked=checked,separated_off_R0=sep_off_R0,

  D0_offR0=D0_offR0,D0_all_have_Fp_root=(D0_offR0==D0_with_Fp_root))

  if __name__=="__main__":

forpin(3,5,7,11):

r=run(p)

print(f"p={r['p']}:checked={r['checked']},separated-off-R0samples
  (all D!=0)="

f"{r['separated_off_R0']},D=0-off-R0samples={r['D0_offR0']},"

f"everyD=0hasanF_p-root
  (non-separated)={r['D0_all_have_Fp_root']}")
   print("PASS:ellclosedform,D=N(ell)*kappa,N(ell)=prodE(a),and"

"separated=>D!=0verified;D=0offR0onlyonnon-separatedE.")

  Expected behavior: all assertions pass; for every prime, separated-off-R0
  samplesallhaveD!=0,andeveryD=0off-R0samplesitsonanon-separatedE
  with a root in F_p — the experimental shadow of the proof that the nonsplit-c
D-kerelstratum is empy.

✻Churnedfor18m41s

  Aut-updating…

92%contextused

92% cntext used
