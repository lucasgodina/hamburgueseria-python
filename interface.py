import tkinter as tk
from tkinter import ttk


ventana = tk.Tk()
ventana.title("Pedidos")
ventana.resizable(0, 0)

titulo = ttk.Label(ventana, text="Pedidos")
titulo.grid(row=0, column=0)

ventana.mainloop()
