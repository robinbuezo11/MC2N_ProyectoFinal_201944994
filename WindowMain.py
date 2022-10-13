import tkinter as tk
from tkinter import ttk
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

        self.__lblcurso = ttk.Label(self,text='Matemática para Computación 2',font='Arial 16 bold', 
                                    background='sky blue')
        self.__lblcurso.place(x=50, y=30)

        self.__lblstudent = ttk.Label(self,text='Robin Omar Buezo Díaz', font='Arial 16 bold', background='sky blue')
        self.__lblstudent.place(x=50, y= 70)

        self.__lblcarne = ttk.Label(self,text='201944994', font='Arial 16 bold', background='sky blue')
        self.__lblcarne.place(x=50, y=110)

        #--------------------------------- buttons --------------------------------------------

        self.__buttonfile = ttk.Button(self, text='Iniciar', width=20, command=self.__actButtonManage)
        self.__buttonfile.place(x=260, y=200)

        self.__buttonmanage = ttk.Button(self, text='Información', width=20, command=self.__actButtonInfo)
        self.__buttonmanage.place(x=260, y=300)


        self.__buttonexit = ttk.Button(self, text='Salir', width=20, command=self.__actButtonExit)
        self.__buttonexit.place(x=260, y=400)

        #--------------------------------- Style ---------------------------------------------

        self.__style = ttk.Style(self)
        self.__style.configure('TButton', font=('Arial',12,'bold'), background='sky blue')



    #----------------------- Actions -----------------------------

    def __actButtonManage(self):
        WindowManager()
    
    def __actButtonInfo(self):
        pass

    def __actButtonExit(self):
        self.destroy()