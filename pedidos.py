# Módulo que contiene las funciones relacionadas con los pedidos y el cambio de encargado.

from database import guardar_pedido, guardar_registro
import requests  # Para la consulta de valor del dólar

total_caja = 0


def obtener_valor_dolar():
    try:
        # Suponiendo que tienes una API para consultar el valor del dólar:
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        data = response.json()
        # Supongamos que el precio del dólar en pesos está en el campo "rates" con clave "ARS"
        valor_dolar = data["rates"]["ARS"]
        return valor_dolar
    except Exception as e:
        print(f"Error al obtener el valor del dólar: {e}")
        # Valor predeterminado en caso de que falle la consulta
        return 1000.0


valor_dolar = obtener_valor_dolar()


# Versión anterior de la función nuevo_pedido que no se utiliza en la interfaz gráfica.
# def nuevo_pedido():
#    global total_caja
#    try:
#        cliente = input("Ingrese el nombre del cliente: ")
#        cant_combo_s = int(input("Ingrese la cantidad de combos simples: "))
#        cant_combo_d = int(input("Ingrese la cantidad de combos dobles: "))
#        cant_combo_t = int(input("Ingrese la cantidad de combos triples: "))
#        cant_flurby = int(input("Ingrese la cantidad de flurbys: "))
#
#        total = cant_combo_s * 5 + cant_combo_d * 6 + cant_combo_t * 7 + cant_flurby * 2
#
#        print(f"Total a pagar: ${total}")
#
#        abona = int(input("El cliente abona con: $"))
#        while abona < total:
#            print(
#                f"El monto abonado no puede ser menor que el total a pagar (${total})."
#            )
#            abona = int(input("El cliente abona con: $"))
#        vuelto = abona - total
#
#        print(f"Pedido para {cliente}")
#        print(f"Total a pagar: ${total}")
#        print(f"Abona con: ${abona}")
#        print(f"Vuelto: ${vuelto}")
#        confirma = input("¿Desea confirmar el pedido? (S/N): ")
#
#        while confirma.upper() not in ["S", "N"]:
#            print("Opción no válida, por favor intente de nuevo.")
#            confirma = input("¿Desea confirmar el pedido? (S/N): ")
#
#        if confirma.upper() == "S":
#            guardar_pedido(
#                cliente, cant_combo_s, cant_combo_d, cant_combo_t, cant_flurby, total
#            )
#            total_caja += total  # Actualizar el total de la caja
#            print("Pedido confirmado")
#        else:
#            print("Pedido cancelado")
#    except ValueError:
#        print("Error: Entrada inválida. Por favor, ingrese un número válido.")
#    except Exception as e:
#        print(f"Error inesperado: {e}")


def nuevo_pedido(cliente, cant_combo_s, cant_combo_d, cant_combo_t, cant_flurby):
    global total_caja
    total = (
        cant_combo_s * 5 + cant_combo_d * 6 + cant_combo_t * 7 + cant_flurby * 2
    ) * valor_dolar
    guardar_pedido(
        cliente, cant_combo_s, cant_combo_d, cant_combo_t, cant_flurby, total
    )
    total_caja += total  # Actualizar el total de la caja
    return total


# Versión anterior de la función cambiar_encargado que no se utiliza en la interfaz gráfica.
# def cambiar_encargado(encargado_actual):
#    global total_caja
#    while True:
#        nuevo_encargado = input("Ingrese el nombre del nuevo encargado: ")
#       if nuevo_encargado.isalpha():
#            if encargado_actual:
#                guardar_registro(encargado_actual, "OUT", total_caja)
#            guardar_registro(nuevo_encargado, "IN", total_caja)
#            return nuevo_encargado
#        else:
#            print("Error: El nombre del encargado solo puede contener letras.")


def cambiar_encargado(encargado_actual, nuevo_encargado):
    global total_caja
    if encargado_actual:
        guardar_registro(encargado_actual, "OUT", total_caja)
    guardar_registro(nuevo_encargado, "IN", total_caja)
    return nuevo_encargado


def guardar_registro_out(encargado):
    global total_caja
    guardar_registro(encargado, "OUT", total_caja)
    return
