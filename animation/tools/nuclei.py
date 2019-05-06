import numpy as np
import sys
import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)


class particle_type:
    def __init__(self):
        self.x = []
        self.y = []
        self.z = []

class nuclei:
    def __init__(self):
        self.protons = particle_type()
        self.neutrons  = particle_type()
        self.xc = 0.
        self.yc = 0.
        self.zc = 0.
        self.nucleons = 394.
        self.rms = 0.

    def calc_center(self):
        temp_x = 0.
        temp_y = 0.
        temp_z = 0.
        for i in range(len(self.protons.x)):
            temp_x += self.protons.x[i]
            temp_y += self.protons.y[i]
            temp_z += self.protons.z[i]

        for i in range(len(self.neutrons.x)):
            temp_x += self.neutrons.x[i]
            temp_y += self.neutrons.y[i]
            temp_z += self.neutrons.z[i]
        self.xc = temp_x/(self.nucleons*0.5)
        self.yc = temp_y/(self.nucleons*0.5)
        self.zc = temp_z/(self.nucleons*0.5)

    def calc_rms(self):
        tmp_rms =0.
        for i in range(len(self.protons.x)):
            tmp_rms += (self.protons.x[i] - self.xc)**2+(self.protons.y[i] - self.yc)**2+(self.protons.z[i] - self.zc)**2
        for i in range(len(self.neutrons.x)):
            tmp_rms += (self.neutrons.x[i] - self.xc)**2+(self.neutrons.y[i] - self.yc)**2+(self.neutrons.z[i] - self.zc)**2
        self.rms = 5./3.*np.sqrt(tmp_rms/(self.nucleons*0.5))
