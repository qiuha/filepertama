# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 12:01:24 2020

@author: QOFIYYU HUDA (18/425167/TK/46862)
"""

import numpy as np
import matplotlib.pyplot as plt

#Data
cpa, cpb, cpc=4, 5.5, 7 # dalam cal/(gmol.K)
dHR=2000 # panas reaksi dalam cal/gmol
Tr=298
Tin=1200
Fa0=10
R=0.082
P=2
n=40
T0guess=200
eps=0.1
Nr=9
tol=1e-2
x1in=0
X1out=x2in
x1span=np.linspace(x1in,x1out,Nr)
w1=np.array([50,100,150,200,250,300,350,400,450])
w2=np.array([450,400,350,300,250,200,150,100,50])

def fun(k,x1out,T):
    T=Tr-(((1-x1in)*cpa+x1in*(cpb+cpa))*(Tr-Tin)+(x1out-x1in)*dHR)/((1-x1out)*cpa+x1out*(cpb+cpc))
    k=2,5*10**(6)*np.exp(-33000/T)
    rA=(k*P/R/T)*((1-x1out)/(1+x1out))
    return 1/rA

def fun2(k,x1out):
    T=Tr-(((1-x1in)*cpa+x1in*(cpb+cpa))*(Tr-Tin)+(x1out-x1in)*dHR)/((1-x1out)*cpa+x1out*(cpb+cpc))
    k=2,5*10**(6)*np.exp(-33000/T)
    xispan=np.linspace(0,xout,n+1)
    dx=xispan[1]-xispan[0]
    f=np.zeros(n+1)
    fsim=np.zeros(n+1)
    for i in range(n+1):
        f[i]=fun(k,xispan[i],T)
        if i==1 or i==n:
            fsim[i]=f[i]
        elif (-1)**i<0:
            fsim[i]=4*f[i]
        else:
            fsim[i]=2*f[i]
    Wcalc=Fa0*dr/3*sum(fsim)
    return (W-Wcalc)

def fun3(x1out):
    Told=T0guess
    eror=1
    while eror>tol:
        fold=fun2(Told,xout)
        dfold=(fun2(Told+eps,xout)-fun2(Told-eps,xout))/2/eps
        Tnew=Told-fold/dfold
        eror=np.abs((Told-Tnew)/Told)
        Told=Tnew
    return Tnew

Tstore=np.zeros(Nr)
Fx=np.zeros(Nr)
for i in range(Nr):
    Tstore[i]=fun3(xspan[i])
    Fx[i]=fun2(Tstore[i],xspan[i])

tabel=np.zeros([Nr,4])
tabel[:,0],tabel[:,1],tabel[:,2],tabel[:,3]=W1,x1span,W2,x2span
garis='='*40
print(garis)
header=(['W1 (kg)','x1','W2 (kg)','x2'])
print('{:^12s}{:^15s}{:^15s}{:^15s}'.format(*header))
print(garis)
for baris in tabel:
    print('{:^12.0f}{:^15.2f}{:^15.2f}{:^15.0f}'.format(*baris))
print(garis)
