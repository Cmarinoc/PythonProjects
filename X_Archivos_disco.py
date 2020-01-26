# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 15:59:03 2019

@author: Clarissa Mariño Contreras
"""

import pandas as pd
import numpy as np

def Info_Compania():
    
    """
    Función para generar los archivos de disco con la información de la compañía 
    
    Return
    ----------
    Esta función no tiene un return como el normalmente conocido si no que retorna un archivo de excel con
    múltiples hojas que contienen la información de la compañía según distitas especificaciones
        
   """
    
#-------------------------------------------------------------------------------------------------#
    
    #Archivo de Disco con la Información de la cantidad de clientes por país
    
    Codigo_pais=['A','B','C','D','E']
    Poblacion_pais=[300,100,500,250,150]
    Paises_poblacion=np.array([Codigo_pais,Poblacion_pais])
    Paises_compania=pd.DataFrame(Paises_poblacion, index=['Pais','Poblacion'])

#-------------------------------------------------------------------------------------------------#

    #Archivo de Disco con la Información de Renta per Capita
    Pais=['A','B','C','D','E']
    RentaperCapita=[10315,10315,2932,13220,24999]
    Renta=np.array([Pais,RentaperCapita])
    Renta=pd.DataFrame(Renta, index=['Pais','RentaperCapita'])   
    
#-------------------------------------------------------------------------------------------------#
    
    #Archivo de Disco con la Información del costo de llamadas por minuto entre paises
    
    PaisE=['A','B','C','D','E']
    PaisR=['A','B','C','D','E']
    LlamadasA=[0.5,1,1.2,1.5,2.3]
    LlamadasB=[1.1,0.2,1.8,2.3,3.5]
    LlamadasC=[0.9,0.8,0.1,3,2.5]
    LlamadasD=[3.5,2.4,6.5,1,4.3]
    LlamadasE=[1.7,1.9,1.6,1,0.8]
    Costo_llamadas=np.array([LlamadasA,LlamadasB,LlamadasC,LlamadasD,LlamadasE])
    Costo_llamadas=pd.DataFrame(Costo_llamadas,index=PaisE,columns=PaisR)
    
    writer = pd.ExcelWriter('Informacion_Compania.xlsx', engine='xlsxwriter')  
    Paises_compania.to_excel(writer, sheet_name='Paises_Poblacion')
    Renta.to_excel(writer, sheet_name='RentaperCapita')
    Costo_llamadas.to_excel(writer, sheet_name='Costo_Llamadas')
    writer.save()
    