
import logging
import time
from table import runTable
import logging

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def prio_ex(list, n):
    procesos_completados = 0
    time = min(int(x.tiempo_llegada) for x in list)
    i = 0
    while procesos_completados < n:
        while i < len(list):
            count = 0
            if int(list[i].tiempo_llegada) <= time and list[i].completed == False:
              
                for j in range(len(list)):
                    if list[i].nombre != list[j].nombre and list[j].completed == False:
                        if list[i].prioridad < list[j].prioridad or list[j].tiempo_llegada > time:
                            count += 1
                        elif list[i].prioridad > list[j].prioridad and list[j].tiempo_llegada <= time:
                            i+=1
                    else:    
                        count +=1

                if count > 0:
                    list[i].set_tiempo_transcurido(1,time)
                    time += 1
                    
                    if list[i].tiempo_transcurido == list[i].tiempo_cpu:
                        list[i].completed = True
                        list[i].set_values()
                        procesos_completados += 1 
                        i=0
                else:
                    i+=1
            else: 
                i+=1    
            
                
    return list


def prioridad_ex(list, n, e = 0):
    if e == 0:
        print("\n")
        list = prio_ex(list, n)
        runTable(list, "Prioridad Expriopiativo")
    else:
        time.sleep(4)
        print("\n")
        list = prio_ex(list, n)
        logging.info("\nALGORITMO PRIORIDAD EXPROPIATIVO")
        print("+-----------+-----------+-------+-----------+------------+-------+")
        print("| Nombre    | T llegada | T CPU | Prioridad | T comienzo | T fin |")
        print("+-----------+-----------+-------+-----------+------------+-------+")
        for proceso in list:
            nombre = proceso.nombre
            tiempo_llegada = proceso.tiempo_llegada
            tiempo_cpu = proceso.tiempo_cpu
            prioridad = proceso.prioridad 
            tiempo_comienzo = proceso.tiempo_comienzo
            tiempo_fin = proceso.tiempo_fin
            cadena = "|{:<11}|{:>11}|{:>7}|{:>11}|{:>12}|{:>7}|".format(nombre, tiempo_llegada, tiempo_cpu, prioridad, " ,".join(map(str, tiempo_comienzo)), " ,".join(map(str, tiempo_fin)))
            print(cadena)
            print("+-----------+-----------+-------+-----------+------------+-------+")

            
        
        