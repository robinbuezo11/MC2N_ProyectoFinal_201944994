import tkinter as tk
from tkinter import simpledialog
import turtle as tt

class WindowManager(tk.Toplevel):
    def __init__(self) -> None:
        super().__init__()
        self.title('Grafos Planos')
        self.geometry('600x600')
        self.config(background='sky blue')
        self.resizable(False,False)

  
        points = simpledialog.askinteger(title='Puntos', prompt='Ingrese la cantidad de puntos entre 1 y 5', minvalue=1, maxvalue=5)
    
        #------------------------------ Canvas --------------------------------

        self.__canvas = tk.Canvas(self, width=600, height=600)
        self.__canvas.pack()
        self.__screen = tt.TurtleScreen(self.__canvas)

        #---------------- Mostrar ventana ------------------------

        self.focus()
        self.transient(self.master)
        self.grab_set()

        vertexs = self.__createPoints(points)
        for vertex in vertexs:
            vertex.onclick(self.drawLine)

    #------------------------- Functions -------------------------

    def __createPoints(self, points):
        self.line = tt.RawTurtle(canvas=self.__canvas)
        self.line.hideturtle()
        self.line.penup()
        self.line.setpos(-255,255)
        self.line.onclick(self.drawLine)
        if points == 1:
            vertex1 = tt.RawTurtle(canvas=self.__canvas, shape='circle')
            vertex1.penup()
            return [vertex1]
        elif points == 2:
            vertex1 = tt.RawTurtle(canvas=self.__canvas, shape='circle')
            vertex1.penup()
            vertex1.setpos(-150,0)
            vertex2 = tt.RawTurtle(canvas=self.__canvas, shape='circle')
            vertex2.penup()
            vertex2.setpos(150,0)
            return [vertex1, vertex2]
        elif points == 3:
            vertex1 = tt.RawTurtle(canvas=self.__canvas, shape='circle')
            vertex1.penup()
            vertex1.setpos(0,150)
            vertex2 = tt.RawTurtle(canvas=self.__canvas, shape='circle')
            vertex2.penup()
            vertex2.setpos(-150,-150)
            vertex3 = tt.RawTurtle(canvas=self.__canvas, shape='circle')
            vertex3.penup()
            vertex3.setpos(150,-150)
            return [vertex1, vertex2, vertex3]
        elif points == 4:
            vertex1 = tt.RawTurtle(canvas=self.__canvas, shape='circle')
            vertex1.penup()
            vertex1.setpos(-150,150)
            vertex2 = tt.RawTurtle(canvas=self.__canvas, shape='circle')
            vertex2.penup()
            vertex2.setpos(150,150)
            vertex3 = tt.RawTurtle(canvas=self.__canvas, shape='circle')
            vertex3.penup()
            vertex3.setpos(-150,-150)
            vertex4 = tt.RawTurtle(canvas=self.__canvas, shape='circle')
            vertex4.penup()
            vertex4.setpos(150,-150)
            return [vertex1, vertex2, vertex3, vertex4]
        elif points == 5:
            vertex1 = tt.RawTurtle(canvas=self.__canvas, shape='circle')
            vertex1.penup()
            vertex1.setpos(-150,0)
            vertex2 = tt.RawTurtle(canvas=self.__canvas, shape='circle')
            vertex2.penup()
            vertex2.setpos(150,0)
            vertex3 = tt.RawTurtle(canvas=self.__canvas, shape='circle')
            vertex3.penup()
            vertex3.setpos(-150,-200)
            vertex4 = tt.RawTurtle(canvas=self.__canvas, shape='circle')
            vertex4.penup()
            vertex4.setpos(150,-200)
            vertex5 = tt.RawTurtle(canvas=self.__canvas, shape='circle')
            vertex5.penup()
            vertex5.setpos(0,200)
            return [vertex1, vertex2, vertex3, vertex4, vertex5]

    def drawLine(self,x,y):
        self.line.setpos(x,y)
        if self.line.isdown():
            self.line.penup()
        else:
            self.line.pendown()


        
    

