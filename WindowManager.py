import tkinter as tk
from tkinter import BOTH, messagebox as msgbx
from tkinter import ttk
from tkinter import simpledialog

class WindowManager(tk.Toplevel):
    def __init__(self) -> None:
        super().__init__()
        self.title('Grafos Planos')
        self.geometry('700x550')
        self.config(background='sky blue')
        self.resizable(False,False)

  
        points = simpledialog.askinteger(title='Puntos', prompt='Ingrese la cantidad de puntos entre 1 y 5', minvalue=1, maxvalue=5)
    
        #------------------------------ Canvas --------------------------------

        self.__canvas = tk.Canvas(self)
        self.__canvas.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        
        #---------------- Mostrar ventana ------------------------

        self.focus()
        self.grab_set()

    
    #------------------------- Functions -------------------------

    
        