import tkinter as tk
from tkinter import ttk, messagebox
from pedidos import nuevo_pedido, cambiar_encargado


class HamburgueseriaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hamburguesería IT")
        self.root.resizable(0, 0)

        self.encargado = None

        self.create_widgets()

    def create_widgets(self):
        self.frame = ttk.Frame(self.root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.label_encargado = ttk.Label(self.frame, text="Encargado:")
        self.label_encargado.grid(row=0, column=0, sticky=tk.W)

        self.entry_encargado = ttk.Entry(self.frame)
        self.entry_encargado.grid(row=0, column=1, sticky=(tk.W, tk.E))

        self.button_set_encargado = ttk.Button(
            self.frame, text="Establecer Encargado", command=self.set_encargado
        )
        self.button_set_encargado.grid(row=0, column=2, sticky=tk.W)

        self.button_nuevo_pedido = ttk.Button(
            self.frame, text="Nuevo Pedido", command=self.nuevo_pedido
        )
        self.button_nuevo_pedido.grid(
            row=1, column=0, columnspan=3, sticky=(tk.W, tk.E)
        )

        self.button_cambiar_encargado = ttk.Button(
            self.frame, text="Cambiar Encargado", command=self.cambiar_encargado
        )
        self.button_cambiar_encargado.grid(
            row=2, column=0, columnspan=3, sticky=(tk.W, tk.E)
        )

    def set_encargado(self):
        encargado = self.entry_encargado.get()
        if encargado.isalpha():
            self.encargado = encargado
            messagebox.showinfo("Encargado", f"Encargado establecido: {encargado}")
        else:
            messagebox.showerror(
                "Error", "El nombre del encargado solo puede contener letras."
            )

    def nuevo_pedido(self):
        if self.encargado:
            self.pedido_window = tk.Toplevel(self.root)
            self.pedido_window.title("Nuevo Pedido")

            ttk.Label(self.pedido_window, text="Cliente:").grid(row=0, column=0)
            self.entry_cliente = ttk.Entry(self.pedido_window)
            self.entry_cliente.grid(row=0, column=1)

            ttk.Label(self.pedido_window, text="Combos Simples:").grid(row=1, column=0)
            self.entry_combo_s = ttk.Entry(self.pedido_window)
            self.entry_combo_s.grid(row=1, column=1)

            ttk.Label(self.pedido_window, text="Combos Dobles:").grid(row=2, column=0)
            self.entry_combo_d = ttk.Entry(self.pedido_window)
            self.entry_combo_d.grid(row=2, column=1)

            ttk.Label(self.pedido_window, text="Combos Triples:").grid(row=3, column=0)
            self.entry_combo_t = ttk.Entry(self.pedido_window)
            self.entry_combo_t.grid(row=3, column=1)

            ttk.Label(self.pedido_window, text="Flurbys:").grid(row=4, column=0)
            self.entry_flurby = ttk.Entry(self.pedido_window)
            self.entry_flurby.grid(row=4, column=1)

            self.button_confirmar_pedido = ttk.Button(
                self.pedido_window,
                text="Confirmar Pedido",
                command=self.confirmar_pedido,
            )
            self.button_confirmar_pedido.grid(row=5, column=0, columnspan=2)

        else:
            messagebox.showerror("Error", "Debe establecer un encargado primero.")

    def confirmar_pedido(self):
        try:
            cliente = self.entry_cliente.get()
            cant_combo_s = int(self.entry_combo_s.get())
            cant_combo_d = int(self.entry_combo_d.get())
            cant_combo_t = int(self.entry_combo_t.get())
            cant_flurby = int(self.entry_flurby.get())

            total = nuevo_pedido(
                cliente, cant_combo_s, cant_combo_d, cant_combo_t, cant_flurby
            )
            messagebox.showinfo("Pedido Confirmado", f"Total a pagar: ${total}")
            self.pedido_window.destroy()
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos.")
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {e}")

    def cambiar_encargado(self):
        if self.encargado:
            self.cambiar_encargado_window = tk.Toplevel(self.root)
            self.cambiar_encargado_window.title("Cambiar Encargado")

            ttk.Label(self.cambiar_encargado_window, text="Nuevo Encargado:").grid(
                row=0, column=0
            )
            self.entry_nuevo_encargado = ttk.Entry(self.cambiar_encargado_window)
            self.entry_nuevo_encargado.grid(row=0, column=1)

            self.button_confirmar_cambio = ttk.Button(
                self.cambiar_encargado_window,
                text="Confirmar Cambio",
                command=self.confirmar_cambio_encargado,
            )
            self.button_confirmar_cambio.grid(row=1, column=0, columnspan=2)
        else:
            messagebox.showerror("Error", "Debe establecer un encargado primero.")

    def confirmar_cambio_encargado(self):
        nuevo_encargado = self.entry_nuevo_encargado.get()
        if nuevo_encargado.isalpha():
            self.encargado = cambiar_encargado(self.encargado, nuevo_encargado)
            messagebox.showinfo("Encargado", f"Nuevo encargado: {nuevo_encargado}")
            self.cambiar_encargado_window.destroy()
        else:
            messagebox.showerror(
                "Error", "El nombre del encargado solo puede contener letras."
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = HamburgueseriaApp(root)
    root.mainloop()
