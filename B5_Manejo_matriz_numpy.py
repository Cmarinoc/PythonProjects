# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 12:39:17 2019

@author: Clarissa Marino
"""

import pandas
import numpy as np

def Leer_fichero():
    """Esta función no será utilizada en ningún momento durante la práctica es solamente como fin ilustrativo"""
    #Lectura y alamacenamiento de la Renta per Capita
    Renta_per_capita=pandas.read_excel('Informacion_Compania.xlsx','RentaperCapita')
    Paises=Renta_per_capita.iloc[0]
    Renta=Renta_per_capita.iloc[1]
    RentaperCapita=np.array([[Paises],[Renta]])
    #Lectura y almacenamiento del Costo de llamadas por minuto
    Tarifa_llamadas=pandas.read_excel('Informacion_Compania.xlsx','Costo_Llamadas')
    Tarifa_A=Tarifa_llamadas.A
    Tarifa_B=Tarifa_llamadas.B
    Tarifa_C=Tarifa_llamadas.C
    Tarifa_D=Tarifa_llamadas.D
    Tarifa_E=Tarifa_llamadas.E
    Tarifa_llamada_entre_paises=np.array([[Tarifa_A],[Tarifa_B],[Tarifa_C],[Tarifa_D],[Tarifa_E]])
    return RentaperCapita,Tarifa_llamada_entre_paises
