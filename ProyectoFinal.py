# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 08:08:34 2019

@author: Clarissa Marino
"""
import A_generador_fichero_llamadas as fichero
import X_Archivos_disco as archivos

def main(): 
    #Se cargarán los archivos de disco de la compañía
    print("Leyendo archivos de información de la compañía")
    archivos.Info_Compania()
    #Se genera el fichero con la información de 5000 llamadas
    print("Estamos generando los archivos de llamadas de la compañía de los últimos tres meses")
    print("Por Favor Espere")
    fichero.Generacion_fichero_llamadas()
    print("Calculando los ingresos de la compañía en el último trimestre")
    #Se calculan los ingresos de la compañía según las llamadas
    import B6_Calculo_ingresos as ingresos
    ingresos.Calculo_de_ingresos()
    #print("Puede consultar datos extras de ingresos y su visualización en la carpeta de ejecución de este programa")
    ingresos.Visualizacion_Compañia()
if __name__ == "__main__":
     main()