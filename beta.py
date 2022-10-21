import numpy as np
from param import *

def delta_v(M1, T0, T1):
    a0 = (G*M1/4/np.pi**2*T0**2)**(1/3)
    a1 = a0*(T1/T0)**(2/3)
    return (G*M1/a0)**0.5 - (G*M1*(2/a0-1/a1))**0.5

def cal_beta(delta_v, M2, mD, vD):
    return delta_v*M2/mD/vD

dv = delta_v(M1, T0, T1)
beta = cal_beta(dv, M2, mD, vD)
print('{:.2e}'.format(M2*dv))
print(dv)
print(beta)
