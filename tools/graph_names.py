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
      v_color = "purple"
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
      v_color = "purple"
      v_linestyle = "-"
      v_marker = ""
      v_name = []
      plot_info.append([v_name,v_color,v_linestyle,v_marker])
      v_name.append("Total system energy STATIC")
      v_name.append("Total system potential energy STATIC")
      v_name.append("Total system kinetic energy STATIC")
      v_name.append("Total system coulomb energy STATIC")
      v_name.append("Total system momentum energy STATIC")
      v_name.append("Total system asymmetry energy STATIC")
      v_color = "purple"
      v_linestyle = "-"
      v_marker = ""
      plot_info.append([v_name,v_color,v_linestyle,v_marker])

  return plot_info

def graph_settings_static(number_of_graphs):
  plot_info = []
  for i in range(number_of_graphs) :
      g_name = []
      g_name.append("all")
      g_name.append("potential")
      g_name.append("coulomb")
      g_name.append("kinetic")
      g_name.append("asymmetry")
      g_name.append("momentum")
      v_name = []
      v_name.append("Total system energy MOMENTUM")
      v_name.append("Total system potential energy MOMENTUM")
      v_name.append("Total system kinetic energy MOMENTUM")
      v_name.append("Total system coulomb energy MOMENTUM")
      v_name.append("Total system momentum energy MOMENTUM")
      v_name.append("Total system asymmetry energy MOMENTUM")
      v_color = "purple"
      v_linestyle = "-"
      v_marker = ""
      plot_info.append([v_name,v_color,v_linestyle,v_marker,g_name])
  return plot_info

def graph_settings_momentum(number_of_graphs):
  plot_info = []
  for i in range(number_of_graphs) :
      g_name = []
      g_name.append("all")
      g_name.append("potential")
      g_name.append("coulomb")
      g_name.append("kinetic")
      g_name.append("asymmetry")
      g_name.append("momentum")
      v_name = []
      v_name.append("Total system energy MOMENTUM")
      v_name.append("Total system potential energy MOMENTUM")
      v_name.append("Total system kinetic energy MOMENTUM")
      v_name.append("Total system coulomb energy MOMENTUM")
      v_name.append("Total system momentum energy MOMENTUM")
      v_name.append("Total system asymmetry energy MOMENTUM")
      v_color = "orange"
      v_linestyle = ""
      v_marker = "o"
      plot_info.append([v_name,v_color,v_linestyle,v_marker,g_name])
  return plot_info


def graph_settings_density_static() :
  plot_info = []
  for i in range(2) :
      v_name = []
      v_name.append(r"$\rho_{p}$")
      v_name.append(r"$\rho_{t}$")
      v_color = "purple"
      v_linestyle = []
      v_linestyle.append("-")
      v_linestyle.append("--")
      v_marker = ""
      plot_info.append([v_name,v_color,v_linestyle,v_marker])
  return plot_info


def graph_settings_density_momentum() :
  plot_info = []
  for i in range(2) :
      v_name = []
      v_name.append(r"$\rho_{p}$")
      v_name.append(r"$\rho_{t}$")
      v_color = "orange"
      v_linestyle = ""
      v_marker = "o"
      plot_info.append([v_name,v_color,v_linestyle,v_marker])
  return plot_info


def graph_settings_rms_static() :
  plot_info = []
  for i in range(2) :
      v_name = []
      v_name.append(r"$rms_{p}$")
      v_name.append(r"$rms_{t}$")
      v_color = "purple"
      v_linestyle = []
      v_linestyle.append("-")
      v_linestyle.append("--")
      v_marker = ""
      plot_info.append([v_name,v_color,v_linestyle,v_marker])
  return plot_info


def graph_settings_rms_momentum() :
  plot_info = []
  for i in range(2) :
      v_name = []
      v_name.append(r"$rms_{p}$")
      v_name.append(r"$rms_{t}$")
      v_color = "orange"
      v_linestyle = ""
      v_marker = "o"
      plot_info.append([v_name,v_color,v_linestyle,v_marker])
  return plot_info












