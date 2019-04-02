import numpy as np


def graph_settings(number_of_graphs):
  plot_info = []
  for i in range(number_of_graphs) :
      v_name = []
      v_name.append("Total system energy STATIC")
      v_name.append("Total system potential energy STATIC")
      v_name.append("Total system kinetic energy STATIC")
      v_name.append("Total system coulomb energy STATIC")
      v_name.append("Total system momentum energy STATIC")
      v_name.append("Total system asymmetry energy STATIC")
      v_color = "red"
      v_linestyle = "-"
      v_marker = ""
      v_name = []
      plot_info.append([v_name,v_color,v_linestyle,v_marker])
      v_name.append("Total system energy MOMENTUM")
      v_name.append("Total system potential energy MOMENTUM")
      v_name.append("Total system kinetic energy MOMENTUM")
      v_name.append("Total system coulomb energy MOMENTUM")
      v_name.append("Total system momentum energy MOMENTUM")
      v_name.append("Total system asymmetry energy MOMENTUM")
      v_color = "red"
      v_linestyle = ""
      v_marker = "o"
      plot_info.append([v_name,v_color,v_linestyle,v_marker])

  return plot_info



def graph_settings_2(number_of_graphs):
  plot_info = []
  for i in range(number_of_graphs) :
      v_name = []
      v_name.append("Total system energy STATIC")
      v_name.append("Total system potential energy STATIC")
      v_name.append("Total system kinetic energy STATIC")
      v_name.append("Total system coulomb energy STATIC")
      v_name.append("Total system momentum energy STATIC")
      v_name.append("Total system asymmetry energy STATIC")
      v_color = "orange"
      v_linestyle = "-"
      v_marker = ""
      v_name = []
      plot_info.append([v_name,v_color,v_linestyle,v_marker])
      v_name.append("Total system energy MOMENTUM")
      v_name.append("Total system potential energy MOMENTUM")
      v_name.append("Total system kinetic energy MOMENTUM")
      v_name.append("Total system coulomb energy MOMENTUM")
      v_name.append("Total system momentum energy MOMENTUM")
      v_name.append("Total system asymmetry energy MOMENTUM")
      v_color = "orange"
      v_linestyle = ""
      v_marker = "o"
      plot_info.append([v_name,v_color,v_linestyle,v_marker])

  return plot_info












