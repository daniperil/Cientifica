import tkinter as tk

root = tk.Tk()

v = tk.IntVar()

tk.Label(root,
        text="""Escoger una serie numérica:""",
        justify = tk.LEFT,
        padx = 20).pack()
tk.Radiobutton(root,
              text="Aventura: Sin tiempo límite.",
              padx = 20,
              variable=v,
              value=1).pack(anchor=tk.W)
tk.Radiobutton(root,
              text="Desafio: con tiempo limite.",
              padx = 20,
              variable=v,
              value=2).pack(anchor=tk.W)


root.mainloop()