import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
v = tk.IntVar()
w = tk.IntVar()
x = tk.IntVar()

colors = {
    'back': '#0D0802',
    'text': '#FFFFFF',
    'options': '#AAA7A7',
    'radios': '#000000'
}

root.iconbitmap('./imagenes/logo.ico')
root.title('SCIENTIFIC PUZZLE')

wi = 415
h = 557
root.geometry('%dx%d+0+0' % (wi, h))
root.configure(background=colors['back'])

# Esta clase se encarga de hacer el menu de los botones de selección de los modos de juego.
tk.Label(root,
         background=colors['back'],
         text="""Escoger modo de juego:""",
         justify=tk.LEFT,
         fg=colors['text'],
         font=('comicsans', 12, 'bold'),
         pady=15).pack()

#Boton de tipo juego desafio
tk.Radiobutton(root,
               text="Desafio: con tiempo limite.",
               padx=50,
               activeforeground=colors['radios'],
               fg=colors['options'],
               variable=v,
               pady=5,
               background=colors['back'],
               value=2).pack(anchor=tk.W)

# Boton de tipo de juego aventura
tk.Radiobutton(root,
               background=colors['back'],
               padx=50,
               pady=5,
               activeforeground=colors['radios'],
               text="Aventura: Sin tiempo límite.",
               fg=colors['options'],
               variable=v,
               value=1).pack(anchor=tk.W)

#Botones para tamaño del tablero
tk.Label(root,
         fg=colors['text'],
         font=('comicsans', 12, 'bold'),
         text="""Tamaño del tablero:""",
         justify=tk.LEFT,
         pady=15,
         background=colors['back'],
         padx=20).pack()

#Boton para 3x3
tk.Radiobutton(root,
               text="3x3",
               padx=50,
               pady=5,
               activeforeground=colors['back'],
               background=colors['back'],
               variable=w,
               fg=colors['options'],
               value=3).pack(anchor=tk.W)

#Boton para 4x4
tk.Radiobutton(root,
               text="4x4",
               fg=colors['options'],
               padx=50,
               pady=5,
               activeforeground=colors['back'],
               variable=w,
               background=colors['back'],
               value=4).pack(anchor=tk.W)

#Boton para 5x5
tk.Radiobutton(root,
               text="5x5",
               padx=50,
               pady=5,
               activeforeground=colors['back'],
               background=colors['back'],
               fg=colors['options'],
               variable=w,
               value=5).pack(anchor=tk.W)

#Clase que se encarga de los botones para la selección de serie numérica
tk.Label(root,
         fg=colors['text'],
         font=('comicsans', 12, 'bold'),
         text="""Escoger una serie numérica:""",
         justify=tk.LEFT,
         pady=15,
         background=colors['back'],
         padx=20).pack()

#Boton para Fibonacci
tk.Radiobutton(root,
               text="Fibonacci",
               fg=colors['options'],
               padx=50,
               pady=5,
               variable=x,
               background=colors['back'],
               value=1).pack(anchor=tk.W)

#Boton para Cuadrática
tk.Radiobutton(root,
               text="Cuadrática",
               padx=50,
               pady=5,
               fg=colors['options'],
               variable=x,
               background=colors['back'],
               value=2).pack(anchor=tk.W)

#Boton para primos
tk.Radiobutton(root,
               text="Números primos",
               fg=colors['options'],
               padx=50,
               pady=5,
               variable=x,
               background=colors['back'],
               value=3).pack(anchor=tk.W)

#Boton para potencias de 2
tk.Radiobutton(root,
               text="Potencias de 2",
               padx=50,
               pady=5,
               fg=colors['options'],
               variable=x,
               background=colors['back'],
               value=4).pack(anchor=tk.W)

#Boton para numeros pares
tk.Radiobutton(root,
               text="Números pares",
               fg=colors['options'],
               padx=50,
               pady=5,
               variable=x,
               background=colors['back'],
               value=5).pack(anchor=tk.W)

#Boton para numeros impares
tk.Radiobutton(root,
               text="Números impares",
               fg=colors['options'],
               padx=50,
               pady=5,
               variable=x,
               background=colors['back'],
               value=6).pack(anchor=tk.W)


def modojuego():
    return v.get()


def tamaniotablero():
    return w.get()


def serie():
    return x.get()


def aceptar():
    if not v.get == 0 and not w.get() == 0 and not x.get() == 0:
        root.destroy()
    else:
        messagebox.askokcancel("SELECCIONAR", "No has seleccionado todas las opciones para comenzar el juego")


tk.Button(root,
          text='ACEPTAR',
          padx=30,
          command=aceptar,
          justify=tk.LEFT
          ).pack()


def ask_quit():
    if messagebox.askokcancel("SALIR", "Quieres salir del juego?"):
        root.destroy()


root.protocol("WM_DELETE_WINDOW", ask_quit)

root.mainloop()

