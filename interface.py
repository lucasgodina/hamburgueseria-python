import tkinter as tk
from tkinter import ttk, messagebox
from pedidos import nuevo_pedido, guardar_registro_out, cambiar_encargado


class HamburgueseriaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hamburguesería IT")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        self.encargado = None
        self.create_bienvenida()

    def create_bienvenida(self):
        # Limpiar la ventana
        for widget in self.root.winfo_children():
            widget.destroy()

        # Mensaje de bienvenida y entrada de encargado
        self.frame_bienvenida = ttk.Frame(self.root, padding="20")
        self.frame_bienvenida.pack(expand=True)

        ttk.Label(
            self.frame_bienvenida,
            text="¡Bienvenido a Hamburguesería IT!",
            font=("Arial", 14),
        ).pack(pady=10)
        ttk.Label(self.frame_bienvenida, text="Encargado:").pack(pady=5)

        self.entry_encargado = ttk.Entry(self.frame_bienvenida)
        self.entry_encargado.pack(pady=5)

        self.button_confirmar_encargado = ttk.Button(
            self.frame_bienvenida, text="Confirmar", command=self.set_encargado
        )
        self.button_confirmar_encargado.pack(pady=20)

    def set_encargado(self):
        nuevo_encargado = self.entry_encargado.get()
        if nuevo_encargado.isalpha():
            cambiar_encargado(self.encargado, nuevo_encargado)
            self.encargado = nuevo_encargado
            self.create_pedido()  # Ir a la pantalla de pedido
        else:
            messagebox.showerror("Error", "El nombre solo puede contener letras.")

    def create_pedido(self):
        # Limpiar la ventana
        for widget in self.root.winfo_children():
            widget.destroy()

        # Pantalla de Pedido
        self.frame_pedido = ttk.Frame(self.root, padding="20")
        self.frame_pedido.pack(expand=True)

        ttk.Label(self.frame_pedido, text="Nuevo Pedido", font=("Arial", 14)).pack(
            pady=10
        )

        # ingresar combos
        self.entry_cliente = self.create_labeled_entry(self.frame_pedido, "Cliente:")
        self.entry_combo_s = self.create_labeled_entry(
            self.frame_pedido, "Combos Simples:", spinbox=True
        )
        self.entry_combo_d = self.create_labeled_entry(
            self.frame_pedido, "Combos Dobles:", spinbox=True
        )
        self.entry_combo_t = self.create_labeled_entry(
            self.frame_pedido, "Combos Triples:", spinbox=True
        )
        self.entry_flurby = self.create_labeled_entry(
            self.frame_pedido, "Flurbys:", spinbox=True
        )

        # Botones de acciones
        self.button_confirmar_pedido = ttk.Button(
            self.frame_pedido, text="Confirmar Pedido", command=self.confirmar_pedido
        )
        self.button_confirmar_pedido.pack(pady=5)

        self.button_cancelar_pedido = ttk.Button(
            self.frame_pedido, text="Cancelar Pedido", command=self.cancelar_pedido
        )
        self.button_cancelar_pedido.pack(pady=5)

        self.button_cambiar_encargado = ttk.Button(
            self.frame_pedido, text="Cambiar Empleado", command=self.create_bienvenida
        )
        self.button_cambiar_encargado.pack(pady=5)

        self.button_salir_seguro = ttk.Button(
            self.frame_pedido, text="Salir Seguro", command=self.salir_seguro
        )

        self.button_salir_seguro.pack(pady=5)

    def salir_seguro(self):
        if messagebox.askyesno("Confirmar Salida", "¿Está seguro de que desea salir?"):
            if self.encargado:
                guardar_registro_out(self.encargado)
                messagebox.showinfo(
                    "Salida", "Registro guardado. Saliendo del programa."
                )
            self.root.destroy()  # Cerrar la ventana principal

    def create_labeled_entry(self, parent, label_text, spinbox=False):
        # Método crear etiquetas y entradas
        frame = ttk.Frame(parent)
        frame.pack(fill="x", pady=5)
        ttk.Label(frame, text=label_text).pack(side="left", padx=5)

        if spinbox:
            entry = ttk.Spinbox(frame, from_=0, to=10, width=5)
        else:
            entry = ttk.Entry(frame)

        entry.pack(side="right", padx=5)
        return entry

    def confirmar_pedido(self):
        try:
            cliente = self.entry_cliente.get()

            if not cliente.isalpha():
                messagebox.showerror("Error", "El nombre solo puede contener letras.")
                return
            if self.entry_combo_s.get():
                cant_combo_s = int(self.entry_combo_s.get())
            else:
                cant_combo_s = 0
            if self.entry_combo_d.get():
                cant_combo_d = int(self.entry_combo_d.get())
            else:
                cant_combo_d = 0
            if self.entry_combo_t.get():
                cant_combo_t = int(self.entry_combo_t.get())
            else:
                cant_combo_t = 0
            if self.entry_flurby.get():
                cant_flurby = int(self.entry_flurby.get())
            else:
                cant_flurby = 0

            if (
                cant_combo_s != 0
                or cant_combo_d != 0
                or cant_combo_t != 0
                or cant_flurby != 0
            ):
                self.total_pesos = nuevo_pedido(
                    cliente, cant_combo_s, cant_combo_d, cant_combo_t, cant_flurby
                )

                self.create_resumen(self.total_pesos)  # Ir a la pantalla de resumen
            else:
                messagebox.showerror(
                    "Error", "Por favor, ingrese mínimo un valor distinto de 0."
                )
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos.")
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {e}")

    def cancelar_pedido(self):
        # Limpiar los campos del pedido
        self.entry_cliente.delete(0, tk.END)
        self.entry_combo_s.delete(0, tk.END)
        self.entry_combo_d.delete(0, tk.END)
        self.entry_combo_t.delete(0, tk.END)
        self.entry_flurby.delete(0, tk.END)

    def create_resumen(self, total_pesos):
        # Limpiar la ventana
        for widget in self.root.winfo_children():
            widget.destroy()

        # Pantalla de Resumen de Pago
        self.frame_resumen = ttk.Frame(self.root, padding="20")
        self.frame_resumen.pack(expand=True)

        ttk.Label(self.frame_resumen, text="Resumen de Pago", font=("Arial", 14)).pack(
            pady=10
        )

        ttk.Label(self.frame_resumen, text=f"Total en Pesos: ${total_pesos:.2f}").pack(
            pady=5
        )

        self.entry_pago_cliente = self.create_labeled_entry(
            self.frame_resumen, "Paga con:"
        )

        self.button_confirmar_pago = ttk.Button(
            self.frame_resumen, text="Confirmar Pago", command=self.confirmar_pago
        )
        self.button_confirmar_pago.pack(pady=20)

    def confirmar_pago(self):
        try:
            paga_con = float(self.entry_pago_cliente.get())
            if paga_con < self.total_pesos:
                messagebox.showerror("Error", "No hay suficiente dinero para pagar.")
                return
            cambio = paga_con - self.total_pesos
            messagebox.showinfo(
                "Pago Confirmado", "Su vuelto es: ${:.2f}".format(cambio)
            )
            self.create_pedido()  # Volver a la pantalla de pedido
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un valor válido.")


if __name__ == "__main__":
    root = tk.Tk()
    app = HamburgueseriaApp(root)
    root.mainloop()
