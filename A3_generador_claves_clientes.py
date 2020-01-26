#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 19:33:38 2019

@author: Clarissa Mariño Contreras
"""
import random 
import pandas as pd
import numpy as np
import X_Archivos_disco as a
a.Info_Compania()
f_clientes=pd.read_excel('Informacion_Compania.xlsx', sheet_name='Paises_Poblacion')
Pais=f_clientes.iloc[0]
Poblacion=f_clientes.iloc[1]

def Clientes_aleatoria_uniformemente():
    
    """
    Función que genera un código de cliente según las Letras de los paises y un número aleatorio de 001 a 999.
    
    Parameters
    ----------
    Letra : str
        Letra elegida aleatoriamente que representa el pais que emite y recibe la llamada
    Numero : str
        Numero aleatorio elegido para completar el codigo de la clave
        
    Return
    ------
    Codigo_aleatorio: str
        Retorna un str aleatorio que representa la clave donde la Letra representa el pais emisor de la llamada y el
        número es el código identificador
    
    Example
    -------
    >>> Clientes_aleatoria_uniformemente()
    'A-439'
    """
    Letra=random.choice(Pais)
    Numero=str(random.randint(000,999))
    Codigo_aleatorio=Letra+"-"+Numero
    return Codigo_aleatorio

#-------------------------------------------------------------------------------------------------#

def Clientes_Probabilidad_no_uniforme():
       
    """
    Función que genera un código de cliente para el país emisor y el país receptor según las Letras de los paises
    y un número aleatorio de 001 a 999. 

    Parameters
    ----------
    
    Esta función no recibe parámetros, sin embargo si depende de la lectura del fichero que posee la información 
    de los clientes que hay por país en la compañía
        
        
    Return
    ------
    Clave_clientes: str
        Retorna dos str con la clave de los clientes del país emisor y el país receptor de las llamadas
    
    Example
    -------
    >>> Clientes_Probabilidad()
    'A-458 # A-412'
    """
    Clientes=[]
    for i in range(len(Poblacion)-1):
        cliente=int(Poblacion[i])
        Clientes.append(cliente)
     
    Numero_Clientes = [Pais[0]] * Clientes[0] + ['B'] * Clientes[1]+ ['C'] * Clientes[2]+ ['D'] * Clientes[3]+ ['E'] * Clientes[4]   
    Codigo_Cliente=random.choice(Numero_Clientes)
    Codigo_ClienteR=random.choice(Numero_Clientes)
    Codigo_Numero_Cliente = str(random.randint(000,999))
    Codigo_Numero_ClienteR = str(random.randint(000,999))
    
    while len(Codigo_Numero_Cliente) <= 2:
        Codigo_Numero_Cliente='0'+Codigo_Numero_Cliente 
    while len(Codigo_Numero_ClienteR) <=2:
        Codigo_Numero_ClienteR='0'+Codigo_Numero_ClienteR
            
    Codigo_Final_Cliente=Codigo_Cliente+'-'+str(Codigo_Numero_Cliente)
    Cliente_Recibe_llamada=Codigo_ClienteR+'-'+str(Codigo_Numero_ClienteR)
     
    if Codigo_Final_Cliente == Cliente_Recibe_llamada:
        Codigo_ClienteR=random.choice(Numero_Clientes)
        Codigo_Numero_ClienteR = random.randint(000,999)
        Cliente_Recibe_llamada=Codigo_ClienteR+'-'+str(Codigo_Numero_ClienteR)
        return Codigo_Final_Cliente, Cliente_Recibe_llamada
         
    else:
        Codigo_Final_Cliente
        Cliente_Recibe_llamada
        Clave_clientes= str(Codigo_Final_Cliente)+" "+"#"+" "+str(Cliente_Recibe_llamada)
        return Clave_clientes