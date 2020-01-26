# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 16:04:41 2019

@author: Clarissa Mariño Contreras
"""

from nltk.corpus import stopwords
import numpy as np
import A4_a_Genera_fichero_palabras as palabras

def Frase():
    try:
        fichero_consumido= open("Palabras_Frecuencias.txt","r")
        print("Generando fichero ")
    except:
        print("El fichero no existe, es necesario generarlo" )
        print("Verifique su conexión a internet. Su conexión debe estar encendida")
        palabras.Palabras_Claves()
    finally:
        fichero_consumido= open("Palabras_Frecuencias.txt","r")

    
    lista_nolimpia=[]
    for linea in fichero_consumido:
        lineas=linea.split("\t")
        lista_nolimpia.append(lineas)
        
    nueva_lista_nolimpia=[]
    for linea in lista_nolimpia:
        frecuencia=linea[0]
        palabra=linea[1].strip()
        matriz=[frecuencia,palabra]
        nueva_lista_nolimpia.append(matriz)
        
    lista_palabras_eliminar=[]
    palabras_eliminar=stopwords.words('spanish')
    for palabra_original in nueva_lista_nolimpia:
        for palabra_eliminar in palabras_eliminar:
            if palabra_eliminar in palabra_original:
                lista_palabras_eliminar.append(palabra_original)
    for tupla_eliminar in lista_palabras_eliminar:
        nueva_lista_nolimpia.remove(tupla_eliminar)
    
#Delimita las palabras a un margen de 500
    #lista_delimitada=[]       
    #for tupla in nueva_lista_nolimpia:
        #while (len(lista_delimitada)) <= 500:
            #if tupla not in lista_delimitada:
                #lista_delimitada.append(tupla)
            
# Lista de palabras
    lista_frecuencias=[]
    for f in range(len(nueva_lista_nolimpia)):
        frecuencia=nueva_lista_nolimpia[f][1]
        lista_frecuencias.append(frecuencia) 
 #Codigo para encontrar la suma de frecuencias
    suma_frecuencias=0
    for f in lista_frecuencias:
        f=int(f)
        suma_frecuencias=suma_frecuencias+f
#Frecuencia relativa de cada palabra
    Lista_frecuencias_relativas=[]
    for f in lista_frecuencias:
            frecuencia_r=int(f)/suma_frecuencias
            Lista_frecuencias_relativas.append(frecuencia_r)
            
#Comprobacion de que la suma de frecuencias relativas da 1       
    suma=0        
    for x in Lista_frecuencias_relativas:
        x=float(x)
        suma=suma+x

# Lista de palabras
    lista_palabras=[]
    for p in range(len(nueva_lista_nolimpia)):
        palabra=nueva_lista_nolimpia[p][0]
        lista_palabras.append(palabra)
#Vamos a elegir de 0 a 25 palabras segun la probabilidad   
    orden=[]
    for i in range(5,25):
        p=np.random.choice(lista_palabras, p=Lista_frecuencias_relativas)
        if p not in orden:
            orden.append(p)
        
    Frase="  ".join(orden)
    
    return Frase



        
                
           
