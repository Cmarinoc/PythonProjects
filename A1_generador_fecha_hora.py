# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 15:56:35 2019

@author: Clarissa

Generacion de fecha_hora y duracion de llamada
"""
import random 
import datetime

    
def Generacion_fecha_hora():
    Fecha_inicio=datetime.date(2020,1,1)
    Fecha_fin=datetime.date(2020,3,30)
    Fecha_Aleatoria= Fecha_inicio + (Fecha_fin - Fecha_inicio) * random.random()
                
    return Fecha_Aleatoria

def Hora_llamada():
    segundos=random.randint(0,59)
    minutos=random.randint(0,59)
    horas=random.randint(0,23)
    hora_llamada=str(datetime.time(horas,minutos,segundos))
    
    return hora_llamada


