import numpy as np
import sys
import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)


class nuclei :
  def __init__(self,sm_type):
   self.time = []
   self.te = []
   self.tpe = []
   self.tke = []
   self.tce = []
   self.tme = []
   self.tae = []
   self.energies = []
   self.time_label = r'time step (fm)'
   self.energy_label = r'energy (MeV)'
   self.density_label = r'$\rho (fm^{-3})$'
   self.plot_aspect = info_for_plotting(sm_type)
   self.dt = 0.
   self.NUM = 0
   self.b_ene = 0.
   self.titles = []
   self.sup_title = 'Constant DT = ' + str(self.dt) + ' Num = ' + str(self.NUM) + r'$B_{energy} = $ ' + str(self.b_ene)+'MeV' 
   self.titles.append('Variation of the TOTAL energy')
   self.titles.append('Variation of the Potential energy')
   self.titles.append('Variation of the Kinetic energy')
   self.titles.append('Variation of the Coulomb energy')
   self.titles.append('Variation of the Momentum energy')
   self.titles.append('Variation of the Asymmetry energy')


  def attribution(self,time,te,tpe,tke,tce,tme,tae) :
   self.time = time
   self.te = te 
   self.tpe = tpe
   self.tke = tke
   self.tce = tce
   self.tme = tme
   self.tae = tae
   self.energies.append(te)
   self.energies.append(tpe)
   self.energies.append(tke)
   self.energies.append(tce)
   self.energies.append(tme)
   self.energies.append(tae)
   
  def set_global_attributes(self,dt,NUM,b_ene):
    self.det = dt
    self.NUM = NUM
    self.b_ene = b_ene



class info_for_plotting:
  def __init__(self,sm_type):
    self.color = 0  
    self.markeredgecolor = 0
    self.linestyle = 0
    self.marker = 0
    self.mfc = 0
    self.label = 0
    if(sm_type == 'static'):
	self.label = 'static'
	self.color = 'purple'
    	self.markeredgecolor = 'black'
    	self.linestyle = '-'
    	self.marker = ''
    	self.mfc = 'purple'

    if(sm_type == 'momentum'):
        self.label = 'momentum'
	self.color = 'orange'
    	self.markeredgecolor = 'black'
    	self.linestyle = ''
    	self.marker = 'o'
    	self.mfc = 'orange'
