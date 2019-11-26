import tkinter as tk

root = tk.Tk()

v = tk.IntVar()

tk.Label(root,
        text="""Tamaño del tablero:""",
        justify = tk.LEFT,
        padx = 20).pack()
tk.Radiobutton(root,
              text="3x3",
              padx = 20,
              variable=v,
              value=1).pack(anchor=tk.W)
tk.Radiobutton(root,
              text="4x4",
              padx = 20,
              variable=v,
              value=2).pack(anchor=tk.W)
tk.Radiobutton(root,
              text="5x5",
              padx = 20,
              variable=v,
              value=3).pack(anchor=tk.W)


root.mainloop()