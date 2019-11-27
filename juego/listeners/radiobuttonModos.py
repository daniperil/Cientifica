import tkinter as tk

root = tk.Tk()

v = tk.IntVar()

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


root.mainloop()