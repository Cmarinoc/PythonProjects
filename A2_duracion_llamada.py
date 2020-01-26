# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 15:12:56 2019

@author: Usuario
"""
import random 
import datetime
import numpy as np 
import matplotlib.pyplot as plt


def Duracion_llamada_uniformemente():
    segundos=random.randint(0,59)
    minutos=random.randint(0,59)
    duracion_llamada=str(datetime.time(0,minutos,segundos))
    duracion_llamada=duracion_llamada[3:8]
    

    return duracion_llamada

def Duracion_llamada_Poisson():
    segundos=random.randint(0,59)
    minutos = np.random.poisson(5, 5000)  #esto es un array 
    minutos=random.choice(minutos) #de aqui elijo un numero cualquiera del array 
    duracion_llamada_poisson=str(datetime.time(0,minutos,segundos))  #se introducen los valores random para generar una hora especifica
    duracion_llamada_poisson=duracion_llamada_poisson[3:8]
    
    #count, bins, ignored = plt.hist(minutos, 14, normed=True)
    #plt.show()
    
    return duracion_llamada_poisson