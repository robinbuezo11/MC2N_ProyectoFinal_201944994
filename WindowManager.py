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

        if points == 1:
            self.__canvas.create_oval(345,270,355,280, fill="black")
        elif points == 2:
            self.__canvas.create_oval(245,270,255,280, fill="black")
            self.__canvas.create_oval(445,270,455,280, fill="black")
        elif points == 3:
            self.__canvas.create_oval(245,370,255,380, fill="black")
            self.__canvas.create_oval(445,370,455,380, fill="black")
            self.__canvas.create_oval(345,170,355,180, fill="black")
        elif points == 4:
            self.__canvas.create_oval(245,370,255,380, fill="black")
            self.__canvas.create_oval(445,370,455,380, fill="black")
            self.__canvas.create_oval(245,170,255,180, fill="black")
            self.__canvas.create_oval(445,170,455,180, fill="black")
        elif points == 5:
            self.__canvas.create_oval(225,440,235,450, fill="black")
            self.__canvas.create_oval(445,440,455,450, fill="black")
            self.__canvas.create_oval(225,230,235,240, fill="black")
            self.__canvas.create_oval(445,230,455,240, fill="black")
            self.__canvas.create_oval(345,70,355,80, fill="black")

        
        #---------------- Mostrar ventana ------------------------

        self.focus()
        self.grab_set()

    
    #------------------------- Functions -------------------------

    
        