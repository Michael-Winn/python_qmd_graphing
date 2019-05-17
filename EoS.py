import numpy as np
import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)
import matplotlib.animation as animation
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import math
#Colors
#***********************************************************************************
# These are the "Tableau 20" colors as RGB.    
tableau20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),    
                  (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),    
                  (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),    
                  (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),    
                  (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]    
  
# Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.    
for i in range(len(tableau20)):    
      r, g, b = tableau20[i]    
      tableau20[i] = (r / 255., g / 255., b / 255.)   

#***********************************************************************************



def calc_eos(rho,s_or_m,eos_type):
  energy = []
  a,b,c = set_params(s_or_m,eos_type)
  print("a = {0} , b = {1} , c = {2}".format(a,b,c))
  if(s_or_m == 'static'):
    for i in range(len(rho)):
        energy.append(0.5*a*rho[i] +(b/(c+1))*rho[i]**c + 23*rho[i]**(2./3.))
  if(s_or_m == 'momentum'):
    for i in range(len(rho)):
#    for i in range(1):
        energy.append(0.5*a*rho[i] +(b/(c+1))*rho[i]**c + 23*rho[i]**(2./3.)+optical_potential(rho[i]))
  return energy

#def optical_potential(rho):
#  opt_a = 236.326
#  opt_b = -20.7304
#  opt_c = 0.901519
#  return np.exp(-opt_c * rho) * (opt_a * rho**2 + opt_b * rho**4)
def set_params(s_or_m,eos_type):
  check = 0
  if(s_or_m == 'static'):
      if(eos_type == 'soft'):
        a = -383.5
        b = 329.5
        c = 1.15
        check = 1
      if(eos_type =='hard'):
        a = -125.3
        b = 71.0
        c = 2.0
        check = 1
      if(check ==0) : print('Error in specified EoS type')
  if(s_or_m =='momentum'): 
	a = -478.87
	b = 413.76
	c = 1.10
  return a,b,c

def fermi_momentum(rho):
  fermi_factor = np.sqrt(5./3.*2*0.938*0.023)
  return fermi_factor * rho**(1./3.)

def calc_I1(pf) :
   I1_a = -21315.53681385053
   I1_b = 22.995012747590916
   I1_c = -0.9015189773855404
   I1_d = 2.5738069719984984
   I1_e = 3.72412138374903
   I1_f = 14.16468213921409
   I1_g = -2.532037677615222
   I1_h = 6.827410027873741
   I1_j = 2.889543262260561

   I1 = I1_a + I1_b * np.exp(I1_c * pf) * (I1_d + pf)*(I1_e + pf)*(I1_f + (I1_g+pf)*pf)*(I1_h + pf * (I1_j +pf))
#   print(I1_b * np.exp(I1_c * pf)*(I1_d + pf)*(I1_e + pf)*(I1_f + (I1_g+pf)*pf)*(I1_h + pf * (I1_j +pf)))
   return I1

def calc_I2(pf):
  return (pf**3)/3.

def optical_potential(rho):
  pf = fermi_momentum(rho)
#  print(pf)
  I1 = calc_I1(pf)
  I2 = calc_I2(pf)
  return I1/I2 * 0.5 * rho 


rho = []
rho = np.arange(0.,3.,0.05)
temp = optical_potential(0.2)
print(temp)
temp_i1 = calc_I1(0.1)
temp_i2 = calc_I2(0.1)
print('I1 val : {0}'.format(temp_i1))
print('I2 val : {0}'.format(temp_i2))
soft_static_eos = calc_eos(rho,'static','soft')
hard_static_eos = calc_eos(rho,'static','hard')
soft_momentum_eos = calc_eos(rho,'momentum','')



#PLOTTING PART ************************************************************************
fig = plt.figure(figsize=(19.2,10.8), dpi=100)
plt.plot(rho,soft_static_eos,label='Soft static', color = tableau20[8],linestyle = '-')
plt.plot(rho,hard_static_eos,label='Hard static', color = tableau20[8],linestyle = '--')
plt.plot(rho,soft_momentum_eos,label='Soft momentum', color = tableau20[2],linestyle = '--',marker = 'o' , markevery = 2)
plt.grid()
plt.legend(loc='upper left')
plt.xlabel(r' $\rho$ $fm^{-3}$')
plt.ylabel(r'$E/A$ $ MeV$')
plt.title('Comparing the EoS for the different parametrisations')
# SAVE PLOT
plt.savefig('EoS.pdf')
