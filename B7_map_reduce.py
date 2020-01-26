# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 20:12:48 2019

@author: Clarissa Mariño
"""
from mrjob.job import MRJob

class MRCharCount(MRJob):

    def mapper(self, _, line):
        """
    Función que se ejecuta desde la consola de anaconda de la siguiente forma:
        1. Se accesa al path donde se encuentre el archivo de python 
        2. Se hace el llamado al archivo de python y al archivo de texto que se quiere consumir:
            Por ejemplo:
                python B7_map_reduce.py llamadas2020.txt
    
        """
    #Separamos línea por línea del archivo de llamadas
        l=line.split()
    #Juntamos la clave del país del emisor y del receptor
        emisor=l[6][0]
        receptor=l[8][0]
        llamada=emisor+receptor
    #Rendondeamos los minutos a partir de un segundo extra en la duración
        segundos=int(l[4][3:5])
        minutos=int(l[4][0:2])
        if segundos >= 1:
            minutos=minutos+1
    #Pedimos mapear el emisor y el receptor, con los minutos de duración de las llamadas

        yield llamada,minutos
                
    def reducer(self, key, values):
    
    #Nuestro key tiene la forma "Llamada entre paises, minutos habladas"
    
        yield key, sum(values)

if __name__ == '__main__':
    MRCharCount.run()
