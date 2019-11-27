import tkinter as tk

root = tk.Tk()

v = tk.IntVar()
#Clase que se encarga de los botones para la selección de serie numérica
tk.Label(root,
        text="""Escoger una serie numérica:""",
        justify = tk.LEFT,
        padx = 20).pack()
#Boton para Fibonacci
tk.Radiobutton(root,
              text="Fibonacci",
              padx = 20,
              variable=v,
              value=1).pack(anchor=tk.W)
#Boton para Cuadrática
tk.Radiobutton(root,
              text="Cuadrática",
              padx = 20,
              variable=v,
              value=2).pack(anchor=tk.W)
#Boton para primos
tk.Radiobutton(root,
              text="Números primos",
              padx = 20,
              variable=v,
              value=3).pack(anchor=tk.W)
#Boton para potencias de 2
tk.Radiobutton(root,
              text="Potencias de 2",
              padx = 20,
              variable=v,
              value=4).pack(anchor=tk.W)
#Boton para numeros pares
tk.Radiobutton(root,
              text="Números pares",
              padx = 20,
              variable=v,
              value=5).pack(anchor=tk.W)
#Boton para numeros impares
tk.Radiobutton(root,
              text="Números impares",
              padx = 20,
              variable=v,
              value=6).pack(anchor=tk.W)

root.mainloop()