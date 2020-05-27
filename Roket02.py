# -*- coding: utf-8 -*-
"""
Integrasi numerik contoh 2
Menghitung waktu tempuh
"""
import numpy as np
import matplotlib.pyplot as plt

def roket(tj):
    vj = 2000*np.log(140000/(140000-2100*tj))-9.8*tj
    return vj

def jarak(tfj):
    tf = 30
    n = 100
    dt = (tfj-ta)/n
    # Membuat array
    t = np.linspace(ta,tf,n+1)
    v = np.zeros(n+1)
    vsimp = np.zeros(n+1)
    for i in range(0,n+1):
        v[i] = roket(t[i])
        if i == 0:
            vsimp[i] = v[i]
        elif i == n:
            vsimp[i] = v[i]
        elif (-1)**i < 0:
            vsimp[i] = 4*v[i]
        else:
            vsimp[i] = 2*v[i]
    x = dt/3*sum(vsimp)
    return x

# Data
ta = 0
tf = 30
xf = jarak(tf)
while xf < 100000:
    tf += .05
    xf = jarak(tf)

print('waktu tempuh = {:.2f} detik'.format(tf))
print('jarak tempuh = {:.2f} m'.format(xf))







