# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 17:32:21 2019

@author: Clarissa Mariño Contreras
"""

import A1_generador_fecha_hora as h
import A2_duracion_llamada as d
import A3_generador_claves_clientes as c
import A4_lista_palabras_clave as p

def Generacion_fichero_llamadas(): 
    """
    Función que genera el fichero con 5000 llamadas a partir de las otras funciones anteriormente creadas

    """
    lineas=[]
    #Se crean 5000 líneas de información y se almacenan para luego ser escritas en el fichero
    for x in range(5000):
        fecha=h.Generacion_fecha_hora()
        hora=h.Hora_llamada()
        #Se utilizará la funciñón que genera el tiempo de llamada a partir de la distribución Poisson
        duracion=d.Duracion_llamada_Poisson()
        #Se utilizará la función que genera la clave de los clientes tomando en cuenta la población por país
        claves=c.Clientes_Probabilidad_no_uniforme()
        #Se realizará la creación del mensaje durante la llamada con la función que no posee conexión a internet
        frase=p.Frase()
        #Se concatenan todas las funciones antes llamadas
        linea_final=str(fecha)+" "+"#"+" "+str(hora)+" "+"#"+" "+str(duracion)+" "+"#"+" "+str(claves)+" "+"#"+" "+str(frase)+"\n"
        lineas.append(linea_final)
    
    #Apertura del fichero para escritura
    fichero_llamadas= open("llamadas2020.txt","w")
    for linea in lineas:
        
        fichero_llamadas.write(linea)
    fichero_llamadas.close()