import logging
import time
from table import *

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')


def sjf(list, n):
    procesos_completados = 0
    time = min(int(x.tiempo_llegada) for x in list)
    while procesos_completados < n:
        for i in range(len(list)):
            count = 0
            if int(list[i].tiempo_llegada) <= time and list[i].completed == False:
                for j in range(len(list)):
                    if list[i].tiempo_cpu >= list[j].tiempo_cpu and list[j].completed == False and int(list[j].tiempo_llegada) <= time and list[i].tiempo_cpu != list[j].tiempo_cpu:
                        list[i], list[j] = list[j], list[i]
                        count+= 1
                        break
                
                if count == 0:
                    tiempo_comienzo = time
                    time = time + list[i].tiempo_cpu
                    list[i].completed = True
                    procesos_completados += 1 
                    list[i].set_values(tiempo_comienzo, time)
                else:
                    break
    return list


def sjf_al(list, n, e=0):
    if e == 0:
        print("\n")
        list = sjf(list, n)
        runTable(list, "SJF")
    else:
        time.sleep(2)
        print("\n")
        list = sjf(list, n)
        logging.info("\nALGORITMO SJF")
        print("+-----------+-----------+-------+------------+-------+----------+")
        print("| Nombre    | T llegada | T CPU | T comienzo | T fin | T espera |")
        print("+-----------+-----------+-------+------------+-------+----------+")
        for proceso in list:
            nombre = proceso.nombre
            tiempo_llegada = proceso.tiempo_llegada
            tiempo_cpu = proceso.tiempo_cpu
            tiempo_comienzo = proceso.tiempo_comienzo
            tiempo_fin = proceso.tiempo_fin
            tiempo_espera = proceso.tiempo_espera
            cadena = "|{:<11}|{:>11}|{:>7}|{:>12}|{:>7}|{:>10}|".format(nombre, tiempo_llegada, tiempo_cpu, tiempo_comienzo  , tiempo_fin, tiempo_espera)
            print(cadena)
            print("+-----------+-----------+-------+------------+-------+----------+")
        
        
    
    
