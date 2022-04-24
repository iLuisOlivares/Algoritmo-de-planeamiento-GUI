from cProfile import run
import time
import logging
from table import *    

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def bubblesort(list):
    intercambio = True
    while intercambio:
        intercambio = False
        for i in range(len(list) - 1):
            if list[i].tiempo_llegada > list[i+1].tiempo_llegada:
                list[i], list[i+1] = list[i+1], list[i]
                intercambio = True
    return list

def fifo2(list):
    
    print("\n")
    # lista_ordenada = sorted(list, key=lambda x: x.tiempo_llegada)
    lista_ordenada = bubblesort(list)
    time = time = min(int(x.tiempo_llegada) for x in list)
    logging.info("\nALGORITMO FIFO")
    print("+-----------+-----------+-------+------------+-------+----------+")
    print("| Nombre    | T llegada | T CPU | T comienzo | T fin | T espera |")
    print("+-----------+-----------+-------+------------+-------+----------+")
    for lista in list:
        tiempo_comienzo = time
        time = time + lista.tiempo_cpu
        lista.set_values(tiempo_comienzo, time)
    list = sorted(list, key=lambda x: x.tiempo_comienzo)
    
    runTable(list, "FIFO")

    # for proceso in list:
    #     nombre = f"proceso {proceso.nombre}"
    #     tiempo_llegada = proceso.tiempo_llegada
    #     tiempo_cpu = proceso.tiempo_cpu
    #     tiempo_comienzo = proceso.tiempo_comienzo
    #     tiempo_fin = proceso.tiempo_fin
    #     tiempo_espera = proceso.tiempo_espera
    #     cadena = "|{:<11}|{:>11}|{:>7}|{:>12}|{:>7}|{:>10}|".format(nombre, tiempo_llegada, tiempo_cpu, tiempo_comienzo  , tiempo_fin, tiempo_espera)
    #     print(cadena)
    #     print("+-----------+-----------+-------+------------+-------+----------+")

def fifo3(list,n):
    procesos_completados = 0
    time = min(int(x.tiempo_llegada) for x in list)
    while procesos_completados < n:
        for i in range(len(list)):
            count = 0
            if int(list[i].tiempo_llegada) <= time and list[i].completed == False:
                for j in range(len(list)):
                    if list[i].tiempo_llegada >= list[j].tiempo_llegada and list[j].completed == False and int(list[j].tiempo_llegada) <= time and list[i].tiempo_llegada != list[j].tiempo_llegada:
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


def fifo(list, n, e=0):
    if e == 0:
        print("\n")
        list = fifo3(list, n)
        runTable(list, "FIFO")
    else:
        time.sleep(1)
        print("\n")
        list = fifo3(list, n)
        logging.info("\nALGORITMO FIFO")
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
        
        

        
       

    