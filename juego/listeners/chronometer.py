from tkinter import *

global count
count = 0

#La clase chornometer es la que se encarga de medir el tiempo en el juego, esta tiene tres métodos inicio, stop y reset.
class chronometer():

    def __init__(self):
        self.root = Tk()
        #titulo del root
        self.root.title("Stop Watch")
        #tamaño
        self.root.geometry("600x500")
        #si se puede modificar tamaño en x o y
        self.root.resizable(False, False)
        #declaración del punto de incion
        self.t = StringVar()
        self.t.set("00:00:00")
        self.lb = Label(self.root, textvariable=self.t)
        #Parámetros del label
        self.lb.config(font=("Courier 40 bold"))
        #Botones 1, 2 y 3 que definen las funcionalidades del cronómetro.
        self.bt1 = Button(self.root, text="Start", command=self.start, font=("Courier 12 bold"))
        self.bt2 = Button(self.root, text="Stop", command=self.stop, font=("Courier 12 bold"))
        self.bt3 = Button(self.root, text="Reset", command=self.reset, font=("Courier 12 bold"))
        #Lugar donde se van a poner el tiempo y los botones
        self.lb.place(x=160, y=10)
        self.bt1.place(x=130, y=100)
        self.bt2.place(x=255, y=100)
        self.bt3.place(x=370, y=100)


#Método de reset
    def reset(self):
        global count
        count = 1
        self.t.set('00:00:00')

#Método de start
    def start(self):
        global count
        count = 0
        self.start_timer()

#Método de comenzar contabilizador
    def start_timer(self):
        global count
        self.timer()

#Método de parar
    def stop(self):
        global count
        count = 1

#Manera como se van a manejar los tiempos
    def timer(self):
        global count
        if (count == 0):
            self.d = str(self.t.get())
            h, m, s = map(int, self.d.split(":"))

            h = int(h)
            m = int(m)
            s = int(s)
            if (s < 59):
                s += 1
            elif (s == 59):
                s = 0
                if (m < 59):
                    m += 1
                elif (m == 59):
                    h += 1
                    m = 0
            if (h < 10):
                h = str(0) + str(h)
            else:
                h = str(h)
            if (m < 10):
                m = str(0) + str(m)
            else:
                m = str(m)
            if (s < 10):
                s = str(0) + str(s)
            else:
                s = str(s)
            self.d = h + ":" + m + ":" + s

            self.t.set(self.d)
            if (count == 0):
                self.root.after(930, self.start_timer)
