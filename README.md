# Hamburguesería IT

Este proyecto es una aplicación de escritorio para gestionar una hamburguesería. Permite realizar pedidos, cambiar de encargado y llevar un registro de las ventas y encargados.

## Requisitos

- Python 3.x
- Tkinter
- SQLite3

## Instalación

1. Clona el repositorio:
   ```sh
   git clone https://github.com/lucasgodina/hamburgueseria-python.git
   ```
2. Navega al directorio del proyecto:
   ```sh
   cd hamburgueseria-python
   ```
3. Instala las dependencias necesarias:
   ```sh
   pip install -r requirements.txt
   ```

## Uso

Ejecuta la aplicación:
   ```sh
   python hamburgueseria.py
   ```

## Estructura del Proyecto

- `hamburgueseria.py`: Punto de entrada de la aplicación.
- `interface.py`: Contiene la interfaz gráfica de usuario.
- `pedidos.py`: Módulo que maneja la lógica de los pedidos y el cambio de encargado.
- `database.py`: Módulo que maneja la interacción con la base de datos.

## Funcionalidades

- **Ingreso de Pedidos**: Permite ingresar nuevos pedidos con detalles de combos y flurbys.
- **Cambio de Encargado**: Permite cambiar el encargado actual y registrar el cambio.
- **Registro de Ventas**: Guarda los pedidos y cambios de encargado en una base de datos SQLite.
