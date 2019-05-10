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
   self.rhom = []
   self.rhom_t = []
   self.rhom_p = []
   self.energies = []
   self.densities = []
   self.time_label = r'time step (fm)'
   self.energy_label = r'energy (MeV)'
   self.density_label = r'$\rho (fm^{-3})$'
   self.plot_aspect = info_for_plotting(sm_type)
   self.dt = 0.
   self.NUM = 0
   self.b_ene = 0.
   self.titles = []
   self.sup_title = '' 
   self.titles.append('Variation of the TOTAL energy')
   self.titles.append('Variation of the Potential energy')
   self.titles.append('Variation of the Kinetic energy')
   self.titles.append('Variation of the Coulomb energy')
   self.titles.append('Variation of the Momentum energy')
   self.titles.append('Variation of the Asymmetry energy')


  def attribution(self,time,te,tpe,tke,tce,tme,tae,rhom_t,rhom_p) :
   self.time = time
   self.te = te 
   self.tpe = tpe
   self.tke = tke
   self.tce = tce
   self.tme = tme
   self.tae = tae
   self.rhom_t = rhom_t
   self.rhom_p = rhom_p
   self.energies.append(te)
   self.energies.append(tpe)
   self.energies.append(tke)
   self.energies.append(tce)
   self.energies.append(tme)
   self.energies.append(tae)
   for i in range(len(rhom_t)):
     self.rhom.append(rhom_t[i]+rhom_p[i])
   self.densities.append(rhom_t) 
   self.densities.append(rhom_p) 

  def set_global_attributes(self,dt,NUM,b_ene):
    self.dt = dt
    self.NUM = NUM
    self.b_ene = b_ene
    self.update_title()

  def update_title(self):
   self.sup_title = 'Constant DT = ' + str(self.dt) + ' Num = ' + str(self.NUM) + r' $B_{energy} = $ ' + str(self.b_ene)+'MeV' 

class info_for_plotting:
  def __init__(self,sm_type):
    self.color = 0  
    self.markeredgecolor = 0
    self.linestyle = 0
    self.marker = 0
    self.mfc = 0
    self.label = 0
    self.markevery = 0

    self.dcolor = []  
    self.dmarkeredgecolor = []
    self.dlinestyle = []
    self.dmarker = []
    self.dmfc = []
    self.dlabel = []
    self.dmarkevery = []

    if(sm_type == 'static'):
	self.label = 'static'
	self.color = 'purple'
    	self.markeredgecolor = 'black'
    	self.linestyle = '-'
    	self.marker = ''
    	self.mfc = 'purple'
	self.markevery = 15

	self.dlabel.append(r'target static')
	self.dcolor.append('purple')
    	self.dmarkeredgecolor.append('black')
    	self.dlinestyle.append('-')
    	self.dmarker.append('')
    	self.dmfc.append('purple')
	self.dmarkevery.append(15)

	self.dlabel.append(r'projectile static')
	self.dcolor.append('purple')
    	self.dmarkeredgecolor.append('black')
    	self.dlinestyle.append('--')
    	self.dmarker.append('')
    	self.dmfc.append('purple')
	self.dmarkevery.append(15)

    if(sm_type == 'momentum'):
        self.label = 'momentum'
	self.color = 'orange'
    	self.markeredgecolor = 'black'
    	self.linestyle = ''
    	self.marker = 'o'
    	self.mfc = 'orange'
	self.markevery = 15

        self.dlabel.append(r'target momentum')
	self.dcolor.append('orange')
    	self.dmarkeredgecolor.append('black')
    	self.dlinestyle.append('')
    	self.dmarker.append('o')
    	self.dmfc.append('orange')
	self.dmarkevery.append(15)

        self.dlabel.append(r'projectile momentum')
	self.dcolor.append('orange')
    	self.dmarkeredgecolor.append('orange')
    	self.dlinestyle.append('')
    	self.dmarker.append('o')
    	self.dmfc.append('none')
	self.dmarkevery.append(15)
class run:
  def __init__(self) : 
    self.runs = [] 
    self.names = []
    self.names.append('all')
    self.names.append('potential')
    self.names.append('coulomb')
    self.names.append('kinetic')
    self.names.append('asymmetry')
    self.names.append('momentum_old')
    self.names.append('momentum_optical')
