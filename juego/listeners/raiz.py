import tkinter as tk

root = tk.Tk()
v = tk.IntVar()
w = tk.IntVar()
x = tk.IntVar()

#Esta clase se encarga de hacer el menu de los botones de selección de los modos de juego.
tk.Label(root,
        text="""Escoger una serie numérica:""",
        justify = tk.LEFT,
        padx = 20).pack()
#Boton de tipo de juego aventura
tk.Radiobutton(root,
              text="Aventura: Sin tiempo límite.",
              padx = 20,
              variable=v,
              value=1).pack(anchor=tk.W)
#Boton de tipo juego desafio
tk.Radiobutton(root,
              text="Desafio: con tiempo limite.",
              padx = 20,
              variable=v,
              value=2).pack(anchor=tk.W)

#Botones para tamaño del tablero
tk.Label(root,
        text="""Tamaño del tablero:""",
        justify = tk.LEFT,
        padx = 20).pack()
#Boton para 3x3
tk.Radiobutton(root,
              text="3x3",
              padx = 20,
              variable=w,
              value=1).pack(anchor=tk.W)
#Boton para 4x4
tk.Radiobutton(root,
              text="4x4",
              padx = 20,
              variable=w,
              value=2).pack(anchor=tk.W)
#Boton para 5x5
tk.Radiobutton(root,
              text="5x5",
              padx = 20,
              variable=w,
              value=3).pack(anchor=tk.W)


#Clase que se encarga de los botones para la selección de serie numérica
tk.Label(root,
        text="""Escoger una serie numérica:""",
        justify = tk.LEFT,
        padx = 20).pack()
#Boton para Fibonacci
tk.Radiobutton(root,
              text="Fibonacci",
              padx = 20,
              variable=x,
              value=1).pack(anchor=tk.W)
#Boton para Cuadrática
tk.Radiobutton(root,
              text="Cuadrática",
              padx = 20,
              variable=x,
              value=2).pack(anchor=tk.W)
#Boton para primos
tk.Radiobutton(root,
              text="Números primos",
              padx = 20,
              variable=x,
              value=3).pack(anchor=tk.W)
#Boton para potencias de 2
tk.Radiobutton(root,
              text="Potencias de 2",
              padx = 20,
              variable=x,
              value=4).pack(anchor=tk.W)
#Boton para numeros pares
tk.Radiobutton(root,
              text="Números pares",
              padx = 20,
              variable=x,
              value=5).pack(anchor=tk.W)
#Boton para numeros impares
tk.Radiobutton(root,
              text="Números impares",
              padx = 20,
              variable=x,
              value=6).pack(anchor=tk.W)

root.mainloop()

