import tkinter as tk
from tkinter import Event, ttk
from tkinter import messagebox as msgbx
from WindowManager import WindowManager

class WindowMain(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title('Proyecto Final')
        self.geometry('700x550')
        self.config(background='sky blue')
        self.resizable(False,False)

        #--------------------------------- Labels -------------------------------------------

        self.__lbltitle = ttk.Label(self,text='GRAFOS PLANOS',font='Arial 20 bold', 
                                    background='sky blue')
        self.__lbltitle.place(x=240, y=50)

        self.__lbldesc = ttk.Label(self,text='Aplicación para la simulación del manejo de grafos planos',font='Arial 14', 
                                    background='sky blue')
        self.__lbldesc.place(x=115, y=100)

        #--------------------------------- buttons --------------------------------------------

        self.__buttonfile = ttk.Button(self, text='Iniciar', width=15, command=self.__actButtonManage)
        self.__buttonfile.place(x=285, y=200)

        self.__buttonmanage = ttk.Button(self, text='Información', width=15, command=self.__actButtonInfo)
        self.__buttonmanage.place(x=285, y=300)


        self.__buttonexit = ttk.Button(self, text='Salir', width=15, command=self.__actButtonExit)
        self.__buttonexit.place(x=285, y=400)

        #--------------------------------- Style ---------------------------------------------

        self.__style = ttk.Style(self)
        self.__style.configure('TButton', font=('Arial',12,'bold'), background='sky blue')



    #----------------------- Actions -----------------------------

    def __actButtonManage(self):
        WindowManager()
    
    def __actButtonInfo(self):
        msgbx.showinfo('Información','PROYECTO FINAL\n\nDesarrollador: Robin Omar Buezo Díaz\nCarne: 201944994\nCurso: Matemática para Computación 2')

    def __actButtonExit(self):
        self.destroy()