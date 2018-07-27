import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

c=299792.458 #speed of light in km/s 
H0=70.0     #Hubble Constant in km/s.Mpc


    
def Integrand(z,omega_m,omega_lam): 

	return ((1+z)**2*(1+omega_m*z)-z*(2+z)*omega_lam)**(-0.5)





def DL(z,omega_m,omega_lam): #The luminosity distance
    
    return (1+z)*(c/H0)*quad(Integrand, 0, z, args=(omega_m,omega_lam))[0] 
    #return (1+z)*(c/H0)*quad(Integrand, 0, z, omega_m, omega_lam)[0]
    
def mu(z):  #The distance modulus
    
    return 5*np.log10(DL(z,omega_m,omega_lam))+25
    
    
    
def DLct(z): #The luminosity distance
    return (1+z)*(c/H0)*np.log(1+z)
    
def muct(z):  #The distance modulus
    
    return 5*np.log10(DLct(z))+25   


mu=np.vectorize(mu) 
z = np.linspace(0.01,1.42,100) 

omega_m=0.3
omega_lam=0.7
distmodul1 = mu(z)

omega_m=1.0
omega_lam=0.0
distmodul2 = mu(z)

omega_m=0.0
omega_lam=1.0
distmodul3 = mu(z)

omega_m=0.0
omega_lam=0.0
distmodul4 = mu(z)



a,b,c=np.genfromtxt("Union2.1_z_dm_err.txt",unpack=True)

fig=plt.figure(figsize=(8,6))

plt.errorbar(a,b,c, fmt= 'o', color='grey', markeredgewidth=0.0, zorder=0)#, ecolor='black')

plt.plot(z,distmodul1, linewidth=3, color='red')
plt.plot(z,distmodul2, linewidth=3, color='blue', linestyle='-.')
plt.plot(z,distmodul3, linewidth=3, color='green', linestyle='--')
plt.plot(z,distmodul4, linewidth=3, color='black', linestyle='dotted')

plt.legend(['$\Omega_{\Lambda}=0.7$, $\Omega_{m}=0.3$', '$\Omega_{\Lambda}=0.0$, $\Omega_{m}=1.0$', '$\Omega_{\Lambda}=1.0$, $\Omega_{m}=0.0$','$\Omega_{\Lambda}=0.0$, $\Omega_{m}=0.0$', 'Union2.1'], loc='lower right',fontsize=18)

plt.xlabel('Redshift',fontsize=18)
plt.ylabel('Distance Modulus',fontsize=18)
plt.xlim(0.0,1.5)
plt.ylim(33,46)
plt.tick_params(labelsize=18)
plt.savefig("dist_mod.jpeg")
plt.show()
