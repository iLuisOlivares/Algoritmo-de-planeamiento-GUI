# Crear objeto proceso con los siguientes atributos, nombre o ID y  valores de tiempo.
import random
from proceso import Proceso


class Proceso_expropiativo(Proceso):
    def __init__(self, nombre, tiempo_llegada, tiempo_cpu, prioridad):
        super().__init__(nombre, tiempo_llegada, tiempo_cpu, prioridad)
        self.tiempo_transcurido = 0
        self.tiempos = []
        self.tiempo_espera = 0
    
    def set_values(self):
        lista_tiempo_final = self.tiempos.copy()
        lista_tiempo_comienzo = self.tiempos.copy()
        tamaño_lista = len(self.tiempos)
        for i in range(tamaño_lista - 1):
             if self.tiempos[i] + 1  == self.tiempos[i + 1]:
                 lista_tiempo_final.remove(self.tiempos[i])

        for i in reversed(range(tamaño_lista)): 
            if self.tiempos[i] == self.tiempos[i-1] + 1:
                lista_tiempo_comienzo.pop(i)

        self.tiempo_comienzo = lista_tiempo_comienzo
        self.tiempo_fin = [x+1 for x in lista_tiempo_final]
        

            
      
    def set_tiempo_transcurido(self, tiempo_transcurido, linea_tiempo):
        self.tiempo_transcurido  += tiempo_transcurido
        self.tiempos.append(linea_tiempo)
        