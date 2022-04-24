

from concurrent.futures import ThreadPoolExecutor
import copy
from tkinter import ttk
import tkinter as tk
from proceso import *
from fifo import *
from sjf import *
from prioridad import *
from prioridad_expropiativo import *
from proceso_expropiativo import *
import logging

list_procesos1 = []
list_procesos2 = []
list_procesos3 = []
list_procesos4 = []
numero_procesos = 0

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')
 
class MainGui(tk.Frame):

    def __init__(self, root):
        super().__init__(root, width=320, height=170)
        self.root = root
        self.root.title("Planificador de procesos")
        self.countt = tk.IntVar()
        self.create_widgets()

    def create_widgets(self):
        
        self.frame = tk.Frame(root)
        self.frame.pack(expand=True,fill='both')
        
        self.label_proceso = tk.Label(self.frame, text="Numero de procesos")
        self.label_proceso.pack(expand=True,fill='both')

        self.n_procesos = tk.Label(self.frame, textvariable=self.countt)
        self.n_procesos.pack(expand=True,fill='both')


        self.simular = tk.Button(self.frame, text="Simular", command=self.simular, state=tk.DISABLED)
        self.simular.pack(expand=True,fill='both')

         
        self.nombre_proceso = tk.StringVar()
        self.nombre_proceso.set("Proceso #0")
        self.tiempo_llegada = tk.IntVar()
        self.tiempo_cpu = tk.IntVar()
        self.prioridad = tk.IntVar()

        frame2 = tk.Frame(self.root)
        frame2.pack(expand=True,fill='both')

        self.combo = ttk.Combobox(frame2, 
                            state="readonly",
                            values=[
                                    "FIFO", 
                                    "SJF",
                                    "Prioridad",
                                    "Prioridad Expropiativo",
                                    "Hilos"])

        self.combo.pack(expand=True,fill='both')
        self.combo.current(0)

        self.l_nombre_proceso = tk.Label(frame2, text="Digitar el nombre del proceso:")
        self.l_nombre_proceso.pack(expand=True,fill='both')

        self.insert_nombre = tk.Entry(frame2, width=30, textvariable=self.nombre_proceso)
        self.insert_nombre.pack(expand=True,fill='both')

        self.l_tiempo_llegada = tk.Label(frame2, text=f"Digitar el tiempo de llegada")
        self.l_tiempo_llegada.pack(expand=True,fill='both')

        self.insert_tiempo_llegada = ttk.Spinbox(frame2, state="readonly", from_=0, to=30, width=30, textvariable=self.tiempo_llegada)
        self.insert_tiempo_llegada.pack(expand=True,fill='both')

        self.l_tiempo_cpu = tk.Label(frame2, text=f"Digitar el tiempo de cpu")
        self.l_tiempo_cpu.pack(expand=True,fill='both')

        self.insert_tiempo_cpu = ttk.Spinbox(frame2, state="readonly", from_=0, to=30, width=30, textvariable=self.tiempo_cpu)
        self.insert_tiempo_cpu.pack(expand=True,fill='both')

        self.l_prioridad = tk.Label(frame2, text=f"Digitar la prioridad del proceso")
        self.l_prioridad.pack(expand=True,fill='both')

        self.insert_prioridad = ttk.Spinbox(frame2, state="readonly", from_=0, to=30, width=30, textvariable=self.prioridad)
        self.insert_prioridad.pack(expand=True,fill='both')

        self.agregar = tk.Button(frame2, text="Agregar Proceso", command=self.imprimir)
        self.agregar.pack(expand=True,fill='both')

        self.reset = tk.Button(frame2, text="Reset procesos", command=self.reset)
        self.reset.pack(expand=True,fill='both')

    def reset(self):
        list_procesos1.clear()
        list_procesos4.clear()
        self.countt.set(0)
        self.simular["state"] = tk.DISABLED
        self.insert_tiempo_cpu.set(0)
        self.insert_tiempo_llegada.set(0)
        self.insert_prioridad.set(0)

        self.insert_nombre.delete(0,"end")
        self.insert_nombre.insert(0,f"Proceso #{self.countt.get()}")


    def imprimir(self):
        self.countt.set(self.countt.get() + 1)
        nombre_proceso = self.nombre_proceso.get()
        tiempo_llegada = self.tiempo_llegada.get()
        tiempo_cpu = self.tiempo_cpu.get()
        prioridad = self.prioridad.get()
        list_procesos1.append(Proceso(nombre_proceso,tiempo_llegada,tiempo_cpu,prioridad))
        list_procesos4.append(Proceso_expropiativo(nombre_proceso,tiempo_llegada,tiempo_cpu,prioridad))
        

        if self.countt.get() > 8:
            self.simular["state"] = tk.DISABLED
        elif self.countt.get() > 3:
            self.simular["state"] = tk.NORMAL
        

        self.insert_tiempo_cpu.set(0)
        self.insert_tiempo_llegada.set(0)
        self.insert_prioridad.set(0)

        self.insert_nombre.delete(0,"end")
        self.insert_nombre.insert(0,f"Proceso #{self.countt.get()}")

     
        print(list_procesos1)
    
    def simular(self):
        print(self.combo.get())
        print(self.countt.get())
        if(self.combo.get() == "FIFO"):
            fifo(copy.deepcopy(list_procesos1), self.countt.get())
        elif(self.combo.get() == "SJF"):
            sjf_al(copy.deepcopy(list_procesos1), self.countt.get())
        elif(self.combo.get() == "Prioridad"):
            prioridad_al(copy.deepcopy(list_procesos1), self.countt.get())
        elif(self.combo.get() == "Prioridad Expropiativo"):
            d = copy.deepcopy(list_procesos4)
            prioridad_ex(d, self.countt.get())

        elif(self.combo.get() == "Hilos"):
            executor = ThreadPoolExecutor(max_workers=2)

            executor.submit(fifo,  copy.deepcopy(list_procesos1), self.countt.get(),1)
            executor.submit(sjf_al,  copy.deepcopy(list_procesos1), self.countt.get(),1)
            executor.submit(prioridad_al,  copy.deepcopy(list_procesos1), self.countt.get(),1)
            executor.submit(prioridad_ex,  copy.deepcopy(list_procesos4), self.countt.get(),1)



if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("420x420")
    app = MainGui(root)
    app.mainloop()