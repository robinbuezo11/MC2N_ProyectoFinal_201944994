import tkinter as tk
from tkinter import messagebox as msg
from tkinter import simpledialog
import turtle as tt
import sympy as sp

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

        self.vertexs = self.__createPoints(points)
        for vertex in self.vertexs:
            vertex.onclick(self.drawLine)

    #------------------------- Functions -------------------------

    def __createPoints(self, points):
        self.line = tt.RawTurtle(canvas=self.__canvas)
        self.line.hideturtle()
        self.line.penup()
        self.line.setpos(-255,255)
        self.line.onclick(self.drawLine)
        self.lineroute = []
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
        x1, y1 = self.line.xcor(), self.line.ycor()
        self.line.setpos(x,y)
        if self.line.isdown():
            newline = [{'x': x1, 'y': y1},{'x': self.line.xcor(), 'y': self.line.ycor()}]
            colision = self.lineColision(newline)
            if not colision[0]:
                self.line.penup()
                self.lineroute.append(newline)
            else:
                incolision = False
                for vertex in self.vertexs:
                    if vertex.distance(colision[1][sp.symbols('x')],colision[1][sp.symbols('y')]) < 8:
                        incolision = True

                if not incolision:        
                    msg.showwarning('Colision', 'Existe una colision entre aristas, el grafo ya no es plano')
                    self.line.undo()
                    self.line.undo()
                    return
                self.line.penup()
                self.lineroute.append(newline)

        else:
            self.line.pendown()

    def lineColision(self, newline):
        for line in self.lineroute:
            x, y, b = sp.symbols('x y b')
            #Ecuacion linea en recorrido
            if (line[1]['x'] - line[0]['x']) != 0:
                pendline = (line[1]['y'] - line[0]['y'])/(line[1]['x'] - line[0]['x'])
            else:
                pendline = 1
            bline = sp.solve(line[0]['x']*pendline + b - line[0]['y'], b)
            ecuationline = sp.Eq(y - pendline*x, bline[0])

            #Ecuacion nueva linea
            if (newline[1]['x'] - newline[0]['x']) != 0:
                pendnewline = (newline[1]['y'] - newline[0]['y'])/(newline[1]['x'] - newline[0]['x'])
            else:
                pendnewline = 1
            bnewline = sp.solve(newline[0]['x']*pendnewline + b - newline[0]['y'], b)
            ecuationnewline = sp.Eq(y - pendnewline*x, bnewline[0])

            result = sp.solve((ecuationline, ecuationnewline),(x,y))

            if len(result) > 0 and result[x] > min(line[1]['x'],line[0]['x']) and result[x] < max(line[1]['x'],line[0]['x']) and result[y] > min(line[1]['y'],line[0]['y']) and result[y] < max(line[1]['y'],line[0]['y']):
                return [True, result]
        return [False, '']


        
    

