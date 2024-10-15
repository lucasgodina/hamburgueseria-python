# Este archivo es el punto de entrada de la aplicación y manejará la lógica del menú principal.

from database import inicializar_db
from interface import HamburgueseriaApp
import tkinter as tk


# def menu():
#    running = True
#    encargado = None
#    while True:
#        encargado = input("Ingrese el nombre del encargado: ")
#        if encargado.isalpha():
#            break
#        print(
#            "El nombre del encargado no puede contener números ni caracteres especiales."
#        )
#
#    while running:
#        print("Bienvenido a hamburguesas IT")
#        print(f"Encargad@: {encargado}")
#        print("Recuerda, siempre hay que recibir al cliente con una sonrisa :)")
#
#        print("#" * 30)
#        print("1. Ingreso nuevo pedido")
#        print("2. Cambio de encargado")
#        print("3. Salir")
#
#        try:
#            opcion = input("Seleccione una opción: ")
#
#            if opcion == "1":
#                nuevo_pedido()
#            elif opcion == "2":
#                encargado = cambiar_encargado(encargado)
#            elif opcion == "3":
#                print("Saliendo del sistema...")
#                running = False
#            else:
#                print("Opción no válida, por favor intente de nuevo.")
#        except Exception as e:
#            print(f"Ha ocurrido un error: {e}")


def main():
    inicializar_db()
    root = tk.Tk()
    app = HamburgueseriaApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
