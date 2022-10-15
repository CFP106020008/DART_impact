from matplotlib.lines import lineStyles
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from param import *
from beta import delta_v

rcParams['font.family'] = 'Times New Roman'
rcParams["mathtext.fontset"] = 'cm'
rcParams["font.size"] = 15

def dv_p(M2, mD, vD, me):
    return (2*M2*mD*vD + np.sqrt((2*M2*mD*vD)**2 - 4*(M2*me+M2**2)*(mD**2*vD**2-me*mD*vD**2)))/(2*(M2*me+M2**2))
def dv_n(M2, mD, vD, me):
    return (2*M2*mD*vD - np.sqrt((2*M2*mD*vD)**2 - 4*(M2*me+M2**2)*(mD**2*vD**2-me*mD*vD**2)))/(2*(M2*me+M2**2))

Me = np.logspace(2,np.log10(M2*1e0),20)

#print(delta_v(M1, T0, T1))
DVP = dv_p(M2, mD, vD, Me)
fig, ax = plt.subplots(figsize=(6,4))
ax.loglog(Me, DVP, color='C0', label='$\Delta v - m_e ~\mathrm{relation}$')
ax.axhline(delta_v(M1, T0, T1), color='C1', linestyle='dashed', label='Estimated $\Delta v$')
ax.axvline(M2*1e-2, color='gray', linestyle='dashed', label=r'$0.01M_2$')
ax.axvline(mD, color='silver', linestyle='dashed', label=r'DART mass')
#plt.hlines()
ax.set_xlabel('$m_e~\mathrm{(kg)}$')
ax.set_ylabel('$\Delta v ~\mathrm{(m/s)}$')
ax.set_xlim(np.min(Me), np.max(Me))
ax.set_ylim(np.min(DVP), np.max(DVP))
plt.legend()
plt.tight_layout()
plt.savefig('dv_me.png', dpi=300)
plt.show()

