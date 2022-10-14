import numpy as np
import matplotlib.pyplot as plt
from param import *
from beta import delta_v

def dv_p(M2, mD, vD, me):
    return (2*M2*mD*vD + np.sqrt((2*M2*mD*vD)**2 - 4*(M2*me+M2**2)*(mD**2*vD**2-me*mD*vD**2)))/(2*(M2*me+M2**2))
def dv_n(M2, mD, vD, me):
    return (2*M2*mD*vD - np.sqrt((2*M2*mD*vD)**2 - 4*(M2*me+M2**2)*(mD**2*vD**2-me*mD*vD**2)))/(2*(M2*me+M2**2))

Me = np.logspace(2,np.log10(M2*0.01),20)

print(delta_v(M1, T0, T1))
plt.loglog(Me, dv_p(M2, mD, vD, Me))
#plt.loglog(Me, dv_n(M2, mD, vD, Me))
plt.show()

