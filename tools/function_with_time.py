import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D


def import_energies(fname) :

        data_set = []
	data = []
	counter = 0
	separated_data = []
	number_of_separate_particles = 394

	data = np.loadtxt(fname)
	temp_data_storage = []
	for i in range(len(data)):
		temp_data_storage.append(data[i])
	 	if ((i+1) % number_of_separate_particles == 0 and i != 0) :
			separated_data.append(temp_data_storage)
			temp_data_storage = []
	print(len(separated_data))
	time = []
	sum_total_energy = []
	sum_potential_energy =[]
	sum_kinetic_energy =[]
	sum_coulomb_energy =[]
	sum_momentum_energy=[]
	sum_longitudinal_kinetic_energy = []
	sum_transvers_kinetic_energy = []
	sum_asym_energy = []

	for i in range(len(separated_data)):
		if(i != 0):
#		  i = i*4
		  time.append(i)
		  sum_temp_total_energy=0
		  sum_temp_potential_energy=0
		  sum_temp_kinetic_energy=0
		  sum_temp_coulomb_energy=0
		  sum_temp_momentum_energy=0
		  sum_temp_longitudinal_kinetic_energy = 0
		  sum_temp_transvers_kinetic_energy = 0
		  sum_temp_asym_energy = 0

		  for j in range(number_of_separate_particles):
		  		 sum_temp_total_energy += separated_data[i][j][6]
		  		 sum_temp_potential_energy += separated_data[i][j][7]
		  		 sum_temp_kinetic_energy += separated_data[i][j][8]
		  		 sum_temp_coulomb_energy += separated_data[i][j][9]
		  		 sum_temp_momentum_energy += separated_data[i][j][10]
		  		 sum_temp_longitudinal_kinetic_energy += separated_data[i][j][11] 
		  		 sum_temp_transvers_kinetic_energy  += separated_data[i][j][12]
		  		 sum_temp_asym_energy += separated_data[i][j][13]
		  sum_total_energy.append(sum_temp_total_energy/float(number_of_separate_particles))
		  sum_potential_energy.append(sum_temp_potential_energy/float(number_of_separate_particles))
		  sum_kinetic_energy.append(sum_temp_kinetic_energy/float(number_of_separate_particles))
		  sum_coulomb_energy.append(sum_temp_coulomb_energy/float(number_of_separate_particles))
		  sum_momentum_energy.append(sum_temp_momentum_energy/float(number_of_separate_particles))
		  sum_longitudinal_kinetic_energy.append(sum_temp_longitudinal_kinetic_energy/ float(number_of_separate_particles)) 
		  sum_transvers_kinetic_energy.append(sum_temp_transvers_kinetic_energy/float(number_of_separate_particles)) 
		  sum_asym_energy.append(sum_temp_asym_energy/float(number_of_separate_particles))

	return time,sum_total_energy,sum_potential_energy,sum_kinetic_energy,sum_coulomb_energy,sum_momentum_energy,sum_longitudinal_kinetic_energy,sum_transvers_kinetic_energy,sum_asym_energy

def import_energies_alt(fname) :

	data = []
	time = []
	sum_total_energy = []
	sum_potential_energy =[]
	sum_kinetic_energy =[]
	sum_coulomb_energy =[]
	sum_momentum_energy=[]
	sum_asymmetry_energy = []

	data = np.loadtxt(fname)
	print(len(data))
	for i in range(len(data)):
	  time.append(data[i][0])
	  sum_total_energy.append(data[i][1])
	  sum_potential_energy.append(data[i][2])
	  sum_kinetic_energy.append(data[i][3])
	  sum_coulomb_energy.append(data[i][4])
	  sum_momentum_energy.append(data[i][5])
	  sum_asymmetry_energy.append(data[i][6])


	return time,sum_total_energy,sum_potential_energy,sum_kinetic_energy,sum_coulomb_energy,sum_momentum_energy,sum_asymmetry_energy

def import_rms(fname):
  time = []
  rms_p = [] 
  rms_t = []
  rms_f = []
  data = np.loadtxt(fname)
  print(len(data))
  for i in range(len(data)):
    time.append(data[i][0])
    rms_p.append(data[i][1])
    rms_t.append(data[i][2])
    rms_f.append(data[i][3])

  return time,rms_p,rms_t,rms_f

def import_density(fname) :

        data_set = []
	data = []
	counter = 0
	separated_data = []
	number_of_radius_steps = 200
	data = np.loadtxt(fname)
	temp_data_storage = []
	for i in range(len(data)):
		temp_data_storage.append(data[i])
	 	if ((i+1) % number_of_radius_steps == 0 and i != 0) :
			separated_data.append(temp_data_storage)
			temp_data_storage = []
	print(len(separated_data))
	time = []
	radius = []
	rho_p = []
	rho_t = []
	rho_f = []
	rho_pa = []
	rho_ta = []
	rho_fa = []
	
	for i in range(len(separated_data)):
		  temp_time = []
		  temp_radius = []
		  temp_rho_p = []
		  temp_rho_t = []
		  temp_rho_f = []
		  temp_rho_pa = 0
		  temp_rho_ta = 0
		  temp_rho_fa = 0
	


		  for j in range(number_of_radius_steps):
				 temp_radius.append(separated_data[i][j][0])
				 temp_rho_p.append(separated_data[i][j][1])
				 temp_rho_t.append(separated_data[i][j][2])
				 temp_rho_f.append(separated_data[i][j][3])
				 temp_time.append(separated_data[i][j][4])
				 temp_rho_pa += separated_data[i][j][1]
				 temp_rho_ta += separated_data[i][j][2]
				 temp_rho_fa += separated_data[i][j][3]
		  radius.append(temp_radius)
		  rho_p.append(temp_rho_p)
		  rho_t.append(temp_rho_t)
		  rho_f.append(temp_rho_f)
		  time.append(temp_time)
		  rho_pa.append(temp_rho_pa/float(number_of_radius_steps))
		  rho_ta.append(temp_rho_ta/float(number_of_radius_steps))
		  rho_fa.append(temp_rho_fa/float(number_of_radius_steps))        
		  
	return radius,rho_p,rho_t,rho_f,time,rho_pa,rho_ta,rho_fa

