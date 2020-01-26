# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 13:15:15 2019

@author: Clarissa Mariño Contreras
"""

import pandas as pd 
import numpy as np
dataset=pd.read_csv('llamadas2020.txt',sep=' # ', encoding="latin-1" )
selcols = dataset.columns[2:5]
clientes_duracion=dataset[selcols]
clientes_duracion_llamadas=np.array(clientes_duracion) 
import matplotlib.pyplot as plt

def Calculo_de_ingresos():
    #Lectura de los ficheros con la información de la compañía 
    Renta_per_capita=pd.read_excel('Informacion_Compania.xlsx','RentaperCapita')
    Paises=Renta_per_capita.iloc[0]
    Tarifa=Renta_per_capita.iloc[1]
    RentaperCapita=np.array([[Paises],[Tarifa]])
    Tarifa_llamadas=pd.read_excel('Informacion_Compania.xlsx','Costo_Llamadas')
    Tarifa_A=Tarifa_llamadas.A
    Tarifa_B=Tarifa_llamadas.B
    Tarifa_C=Tarifa_llamadas.C
    Tarifa_D=Tarifa_llamadas.D
    Tarifa_E=Tarifa_llamadas.E
    Tarifa_llamada_entre_paises=np.array([[Tarifa_A],[Tarifa_B],[Tarifa_C],[Tarifa_D],[Tarifa_E]])

    #Cálculo de la duración total del tiempo de llamadas entre cada uno de los países
    Duracion_redondeada=[]
    Paises_emisores=[]
    Paises_receptores=[]
    
    for t in range(len(clientes_duracion_llamadas)):
        secundos=int(clientes_duracion_llamadas[t][0][3:5])
        minutos=int(clientes_duracion_llamadas[t][0][0:2])
        if secundos > 1:
            minutos=minutos+1
            Duracion_redondeada.append(minutos)
        else:
            minutos=minutos
            Duracion_redondeada.append(minutos)
            
    for e in range(len(clientes_duracion_llamadas)):
        Pais_emisor=clientes_duracion_llamadas[e][1][0:1]
        Paises_emisores.append(Pais_emisor)
    for r in range(len(clientes_duracion_llamadas)):
        Pais_receptor=clientes_duracion_llamadas[r][2][0:1]
        Paises_receptores.append(Pais_receptor)
    
    data={'Emisores':Paises_emisores, 'Receptores':Paises_receptores,'Duracion':Duracion_redondeada}
    paises_llamadas=pd.DataFrame(data)
    duracion_llamadas_entre_paises=paises_llamadas.groupby(['Emisores', 'Receptores']).sum()
    

    #Calculo de los ingresos totales por país
    
    TarifasA=Tarifa_llamada_entre_paises[0][0]
    TarifasB=Tarifa_llamada_entre_paises[1][0]
    TarifasC=Tarifa_llamada_entre_paises[2][0]
    TarifasD=Tarifa_llamada_entre_paises[3][0]
    TarifasE=Tarifa_llamada_entre_paises[4][0]
    TiempoA=np.array(duracion_llamadas_entre_paises[2:7]).transpose()
    TiempoB=np.array(duracion_llamadas_entre_paises[7:12]).transpose()
    TiempoC=np.array(duracion_llamadas_entre_paises[12:17]).transpose()
    TiempoD=np.array(duracion_llamadas_entre_paises[17:22]).transpose()
    TiempoE=np.array(duracion_llamadas_entre_paises[22:27]).transpose()
    Ingresos_paisA=TarifasA*TiempoA
    Ingresos_paisB=TarifasB*TiempoB
    Ingresos_paisC=TarifasC*TiempoC
    Ingresos_paisD=TarifasD*TiempoD
    Ingresos_paisE=TarifasE*TiempoE
    IngresosP=np.concatenate((Ingresos_paisA,Ingresos_paisB,Ingresos_paisC,Ingresos_paisD,Ingresos_paisE))
    IngresosPM=pd.DataFrame(IngresosP, index=['A','B','C','D','E'], columns=['A','B','C','D','E'])
    
    
    #Calculo del Flujo total de llamadas en minutos por país
    TiempoA1=TiempoA.tolist()
    TiempoB1=TiempoB.tolist()
    TiempoC1=TiempoC.tolist()
    TiempoD1=TiempoD.tolist()
    TiempoE1=TiempoE.tolist()
    Llamadas_tiempo=[TiempoA1[0], TiempoB1[0], TiempoC1[0], TiempoD1[0], TiempoE1[0]]
    IngresosT=pd.DataFrame(Llamadas_tiempo, index=['A','B','C','D','E'], columns=['A','B','C','D','E'])
    sumaLateral=[IngresosT.iloc[0].sum(),IngresosT.iloc[1].sum(),IngresosT.iloc[2].sum(),IngresosT.iloc[3].sum(),IngresosT.iloc[4].sum(),'']
    sumaC=[IngresosT['A'].sum(),IngresosT['B'].sum(),IngresosT['C'].sum(),IngresosT['D'].sum(),IngresosT['E'].sum()]
    IngresosT.loc['Total']=sumaC
    IngresosT['SumaTotal']=sumaLateral
    
    #Calculo del Flujo de ingresos por país según las llamadas por minutos
    Flujos=IngresosPM.copy()
    SumaColumnas=[Flujos['A'].sum(),Flujos['B'].sum(),Flujos['C'].sum(),Flujos['D'].sum(),Flujos['E'].sum()]
    Flujos.loc['TotalF']=SumaColumnas
    SumaFilas=[Flujos.iloc[0].sum(),Flujos.iloc[1].sum(),Flujos.iloc[2].sum(),Flujos.iloc[3].sum(),Flujos.iloc[4].sum(),'']
    Flujos['TotalC']=SumaFilas
    
    
    #Escritura en consola de los datos más importantes de la compañía
    print("Resumen de datos de la compañía"+"\n")
    
    print("Cálculo del total de minutos de llamadas por país y sus respectivos flujos")
    print(IngresosT)
    print("#----------------------------------------------------------------------------------#")
    
    print("Ingresos por país según las llamadas por minuto con sus respectivos Flujos")
    print(Flujos)
    print("#----------------------------------------------------------------------------------#")
    
    
    #Creación de un Archivo de excel que sumariza las ganancias de la compañía
    
    writer = pd.ExcelWriter('Ganancias_Compania.xlsx', engine='xlsxwriter') 
    IngresosT.to_excel(writer, sheet_name='Minutos_por_Pais_y_Flujos')
    IngresosPM.to_excel(writer, sheet_name='Ingresos_por_llamada')
    Flujos.to_excel(writer, sheet_name='Flujo_Ingresos')
    writer.save()

def Visualizacion_Compañia():
    
    #Muestreo del porcentaje de clientes en la companía según el país al que pertenecen
    Clientes=pd.read_excel('Informacion_Compania.xlsx', sheet_name='Paises_Poblacion')
    poblacion=Clientes.iloc[1][1:6]
    N=[]
    for p in poblacion:
        p=int(p)
        N.append(p)
    labels = Clientes.iloc[0][1:6]
    sizes = N
    fig1, clientesp = plt.subplots()
    clientesp.pie(sizes, labels=labels, autopct='%1.2f%%',shadow=True, startangle=50)
    clientesp.axis('equal')
    plt.savefig('Porcentaje_clientes.png')
    plt.show()
    
 
    #Flujo de muestreo de los costos de llamada por minuto entre los países 
    IngresosPr=pd.read_excel('Ganancias_Compania.xlsx', sheet_name='Ingresos_por_llamada')
    IngresosPr.plot( kind='bar',stacked=True)
    
    plt.xlabel('País Emisor de llamadas')
    plt.ylabel('Ingresos')
    plt.title('Ingresos por país según las llamadas con otros paises')
    plt.show()
    plt.savefig('Ingresos_por_minuto.png')
    
    #Renta per Capita según el país
    RentaP= pd.read_excel('Informacion_Compania.xlsx',sheet_name='RentaperCapita')  
    Rent=RentaP.iloc[1][1:6]
    R=Rent.astype('int')
    P=RentaP.iloc[0][1:6]
    print(P)
    R.plot(kind='barh')
    plt.xlabel('Renta per Capita')
    plt.ylabel('País')
    plt.title('Renta per Capita según País')
    plt.show()
    plt.savefig('RentaperCapita.png')
    
    #Proporción de ingresos para el país con mayor y menor población
    RentaP= pd.read_excel('Ganancias_Compania.xlsx',sheet_name='Flujo_Ingresos')
    fig=plt.figure()
    ax1=fig.add_subplot(121)
    RentaP['C'].plot.hist(title='Proporción de los Ingresos por país', colormap='rainbow')
    plt.legend()
    plt.xlabel('Ingresos')
    ax2=fig.add_subplot(122)
    RentaP['B'].plot.hist(colormap='prism')
    plt.legend()
    plt.xlabel('Ingresos')
    plt.savefig('ProporciónIngresosPaisMayorYMenor.png')
    plt.show()