import pandas as pd

getFromIC = pd.read_csv('static/add09.csv')

#nic = "200323210433"


def taab(g_nic):
  det = getFromIC.loc[getFromIC['NIC'] == g_nic, 'hou_num']

  all_det = getFromIC.loc[getFromIC['hou_num'] == det.values[0]]
  return all_det


def House_Num(g_nic):
  det = getFromIC.loc[getFromIC['NIC'] == g_nic, 'hou_num']
  return det.values[0]
