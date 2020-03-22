import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

#valuess

k_mLb = 0.0082
k_mTb = 0.0149
k_mLa = 1.0
k_mTa = 0.3865
theta_L = 600
theta_T = 500
n_L = 4.0
n_T = 4.0
gamma_mL = 0.04
gamma_mT = 0.04
k_pT = 0.1
k_pL = 0.1
gamma_pL = 0.002
gamma_pT = 0.002

mL = 0
mT = 0
pL = 0
pT = 0

arguments = [mL,mT,pL,pT]
params = [k_mLb, k_mTb, k_mLa, k_mTa, theta_L, theta_T, n_L, n_T, gamma_mL, gamma_mT, k_pT, k_pL, gamma_pL, gamma_pT]


def toggle_derivative (y,t,args):
    
    k_mLb, k_mTb, k_mLa, k_mTa, theta_L, theta_T, n_L, n_T, gamma_mL, gamma_mT, k_pT, k_pL, gamma_pL, gamma_pT = args
    
    mL, mT, pL, pT = y
    
    dmLdt = k_mLb + k_mLa * 1/(1+((pT/theta_T)**n_T)) - gamma_mL * mL 
    
    dpLdt = k_pL * mL - gamma_pL * pL
    
    dmTdt = k_mTb + k_mTa * 1/(1+((pL/theta_L)**n_L)) - gamma_mT * mT
    
    dpTdt = k_pT * mT - gamma_pT * pT
    
    return [dmLdt, dmTdt, dpLdt, dpTdt]


time = np.linspace(0,3000,3001)

solutions = odeint( toggle_derivative, arguments, time, args=(params,))
   

plt.plot(time,solutions[:,0], label = 'mRNA1')
plt.plot(time,solutions[:,1], label = 'protein1')
plt.plot(time,solutions[:,2], label = 'mRNA2')
plt.plot(time,solutions[:,3], label = 'protein2')

plt.legend()
plt.title('Evolution of the mRNA and protein concentrations as a function of  time')

plt.xlabel('Time')
plt.ylabel('Evolution of the mRNA and protein concentrations')
    
plt.show()
