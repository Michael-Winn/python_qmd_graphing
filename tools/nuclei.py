import numpy as np
import sys
import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)


class nuclei :
  def __init__(self):
   time = []
   te = []
   tpe = []
   tke = []
   tce = []
   tme = []
   tae = []
   time_label = r'time step (fm)'
   energy_label = r'energy (MeV)'
   dt = 0.
   NUM = 0
   b_ene = 0.
   titles = []
   sup_title = 'Constant DT = ' + str(self.dt) + ' Num = ' + str(self.NUM) + r'$B_{energy} = $ ' + str(self.b_ene) 
   titles.append('Variation of the TOTAL energy')
   titles.append('Variation of the Potential energy')
   titles.append('Variation of the Kinetic energy')
   titles.append('Variation of the Coulomb energy')
   titles.append('Variation of the Momentum energy')
   titles.append('Variation of the Asymmetry energy')

   energies = []
   energies.append(te)
   energies.append(tpe)
   energies.append(tke)
   energies.append(tce)
   energies.append(tme)
   energies.append(tae)

  def attribution(self,time,te,tpe,tke,tce,tme,tae)
   self.time = time
   self.te = te 
   self.tpe = tpe
   self.tke = tke
   self.tce = tce
   self.tme = tme
   self.tae = tae
