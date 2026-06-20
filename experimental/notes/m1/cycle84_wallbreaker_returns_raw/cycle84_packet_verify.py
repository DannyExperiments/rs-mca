#!/usr/bin/env python3
"""Independent verifier for a Cycle 84 FAIL_13_packet.json certificate.

This checker deliberately ignores all discrete logarithms.  It regenerates the
48 states from the polynomial formula and checks thirteen direct products in
F_17[X]/(X^16+X^8+3), together with all color data.
"""
from __future__ import annotations
import json, sys

P=17; D=16
PCOEFF=((6,4,4,10,5,4,0,0,1),(14,13,14,12,5,9,0,0,1),(4,12,1,5,0,11,0,0,1))
SCOLOR=(15,9,12)

def norm(a):
    a=list(a)+[0]*(D-len(a)); return tuple(x%P for x in a[:D])
def add(a,b): return tuple((x+y)%P for x,y in zip(norm(a),norm(b)))
def sub(a,b): return tuple((x-y)%P for x,y in zip(norm(a),norm(b)))
def mul(a,b):
    a=norm(a);b=norm(b);t=[0]*31
    for i,x in enumerate(a):
        for j,y in enumerate(b): t[i+j]+=x*y
    for d in range(30,15,-1):
        c=t[d]%P;t[d]=0;t[d-8]-=c;t[d-16]-=3*c
    return tuple(x%P for x in t[:16])
def pw(a,e):
    r=norm((1,));a=norm(a)
    while e:
        if e&1:r=mul(r,a)
        a=mul(a,a);e//=2
    return r
def emb(c): return norm((c%P,))
def peval(i,z):
    r=norm(())
    for c in reversed(PCOEFF[i]): r=add(mul(r,z),emb(c))
    return r

ETA=norm((0,0,0,0,0,0,0,0,0,6))
BETA=norm((2,1)); N=P**D-1; XI=pw(BETA,2); ETA_INV=pw(ETA,N-1)

def state(t,k):
    i=k//16; a=k%16
    arg=mul(mul(XI,emb(pow(3,(-a)%16,P))),pw(ETA_INV,2*t))
    u=peval(i,arg)
    if a&1:u=sub((),u)
    color=(SCOLOR[i]+8*(a&1))%16
    return i+1,a,color,u

def main(path):
    d=json.load(open(path))
    assert d['decision']=='THIRTEEN_FOLD_PACKET_FOUND'
    reps=d['representations']; assert len(reps)==13
    common=norm(d['common_product_coeffs']); seen=set()
    for r in reps:
        pair=(r['left_index'],r['right_index']); assert pair not in seen; seen.add(pair)
        slots=r['slots']; assert len(slots)==7
        prod=norm((1,)); colors=[]
        for expected_t,s in enumerate(slots,1):
            assert s['slot']==expected_t
            i,a,c,u=state(expected_t,s['k'])
            assert (s['i'],s['a'],s['color'])==(i,a,c)
            assert norm(s['u_coeffs'])==u
            prod=mul(prod,u);colors.append(c)
        assert sum(colors)%16==4
        assert prod==common==norm(r['full_product_coeffs'])
        assert mul(norm(r['left_product_coeffs']),norm(r['right_product_coeffs']))==common
        assert r['left_color']==sum(colors[:3])%16
        assert r['right_color']==sum(colors[3:])%16
        assert r['total_color']==4
    print('THIRTEEN_FOLD_PACKET_VERIFIED')

if __name__=='__main__':
    if len(sys.argv)!=2: raise SystemExit(f'usage: {sys.argv[0]} FAIL_13_packet.json')
    main(sys.argv[1])
