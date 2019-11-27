import tkinter as tk

root = tk.Tk()

v = tk.IntVar()

#Botones para tamaño del tablero
tk.Label(root,
        text="""Tamaño del tablero:""",
        justify = tk.LEFT,
        padx = 20).pack()
#Boton para 3x3
tk.Radiobutton(root,
              text="3x3",
              padx = 20,
              variable=v,
              value=1).pack(anchor=tk.W)
#Boton para 4x4
tk.Radiobutton(root,
              text="4x4",
              padx = 20,
              variable=v,
              value=2).pack(anchor=tk.W)
#Boton para 5x5
tk.Radiobutton(root,
              text="5x5",
              padx = 20,
              variable=v,
              value=3).pack(anchor=tk.W)


root.mainloop()