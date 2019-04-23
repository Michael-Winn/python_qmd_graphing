import numpy as np
import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)
import matplotlib.pyplot as plt
#Made modules import
from tools.function_with_time import *
from tools.graph_names import *
from tools.output_methods import *

########################################################### COMMON VARIABLES
current_working_dir = '../altered_version_v11'
output_location = []
output_location.append('constant')
output_location.append('variable')
wptp =2
number_of_files_to_import = 6
input_folders = 2
in_files = []
for i in range(1,input_folders+1):
  in_files.append(i)
###########################################################

plotting_function(1,number_of_files_to_import,in_files,current_working_dir,output_location[0])
plotting_function(1,number_of_files_to_import,in_files,current_working_dir,output_location[1])

