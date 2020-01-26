# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 13:10:59 2019

@author: Usuario
"""

from bs4 import BeautifulSoup
import requests

#Generacion de Palabras claves a partir de una página web
def Palabras_Claves():
    palabras_frecuencias = open("Palabras_Frecuencias.txt","w")
    url = "https://es.wiktionary.org/wiki/Wikcionario:Frecuentes-(1-1000)-Subt%C3%ADtulos_de_pel%C3%ADculas"
    
    codigo_html = requests.get(url).text
    extrae_pag_web = BeautifulSoup(codigo_html, "lxml")
    tabla_palabras_frecuencias=extrae_pag_web.find("table")
    contenido_tabla=[td.get_text() for td in tabla_palabras_frecuencias.find_all("td")[0:]]
     
    filas=[]
    palabras=[]
    frecuencias=[]
    frecuencias_limpias =[]
    palabras_limpias=[]
    fichero_palabras_frecuencia = []
    for palabra in range(0,len(contenido_tabla),3):
        filas.append(contenido_tabla[palabra:palabra+3])
    for fila in filas:
        palabra=fila[1]
        frecuencia=fila[2]
        palabras.append(palabra)
        frecuencias.append(frecuencia)
    for palabra in palabras:
        palabra_limpia=palabra.strip()
        palabras_limpias.append(palabra_limpia)
    for frecuencia in frecuencias:
        frecuencia_limpia=str(frecuencia.strip())
        frecuencia_limpia=int(frecuencia)
        frecuencias_limpias.append(str(frecuencia_limpia))
        
#Creacion de las lineas para el fichero de llamadas y frecuencias      
    for x in range (1000):
        fichero_palabras_frecuencia.append(str(palabras_limpias[x])+"\t"+str(frecuencias_limpias[x])+"\n")
        
    
    for linea in fichero_palabras_frecuencia:
        x=str(linea)
        palabras_frecuencias.write(x)
    palabras_frecuencias.close()