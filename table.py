from tkinter import ttk
import tkinter as tk

  
class Table(ttk.Frame): 
      
    def __init__(self,root,lst,name): 
        super().__init__(root)
        root.title(name)
        self.treeview = ttk.Treeview(self, columns=("Tllegada","Tcpu","Tprio","Tcomienzo","Tfin","Tespera"))
        self.treeview.heading("#0", text="Nombre proceso")
        self.treeview.heading("Tllegada", text="Tiempo de llegada")
        self.treeview.heading("Tcpu", text="Tiempo de CPU")
        self.treeview.heading("Tprio", text="Prioridad")
        self.treeview.heading("Tcomienzo", text="Tiempo de comienzo")
        self.treeview.heading("Tfin", text="Tiempo de fin")
        self.treeview.heading("Tespera", text="Tiempo de espera")
        for proceso in lst:
            nombre = proceso.nombre
            tiempo_llegada = proceso.tiempo_llegada
            tiempo_cpu = proceso.tiempo_cpu
            prioridad = proceso.prioridad
            tiempo_comienzo = proceso.tiempo_comienzo
            tiempo_fin = proceso.tiempo_fin
            tiempo_espera = proceso.tiempo_espera
            self.treeview.insert(  
                "",
                tk.END,
                text= nombre,
                values=(tiempo_llegada, tiempo_cpu,prioridad, tiempo_comienzo, tiempo_fin, tiempo_espera)
             )
        self.treeview.pack()
        self.pack()

def runTable(list,name):
    root = tk.Tk() 
    root.resizable(0, 0) 
    t = Table(root, list, name) 
    t.mainloop()
