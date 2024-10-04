# Módulo que contiene las funciones relacionadas con la base de datos.

import sqlite3
from datetime import datetime


def inicializar_db():
    conn = sqlite3.connect("comercio.sqlite")

    cursor = conn.cursor()

    # Crear tabla de ventas
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS pedidos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente TEXT NOT NULL,
            fecha_hora TEXT NOT NULL, 
            cant_combo_s INTEGER NOT NULL,
            cant_combo_d INTEGER NOT NULL,
            cant_combo_t INTEGER NOT NULL,
            cant_flurby INTEGER NOT NULL,
            total INTEGER NOT NULL
        )"""
    )

    # Crear tabla de registros
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS registro (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            encargado TEXT,
            fecha TEXT,
            evento TEXT,
            caja REAL
        )
    """
    )

    conn.commit()
    conn.close()


def guardar_pedido(
    cliente, cant_combo_s, cant_combo_d, cant_combo_t, cant_flurby, total
):
    conn = sqlite3.connect("comercio.sqlite")

    cursor = conn.cursor()

    fecha_hora = datetime.now().strftime("%a %b %d %H:%M:%S %Y")

    cursor.execute(
        "INSERT INTO pedidos (cliente, fecha_hora, cant_combo_s, cant_combo_d, cant_combo_t, cant_flurby, total) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (
            cliente,
            fecha_hora,
            cant_combo_s,
            cant_combo_d,
            cant_combo_t,
            cant_flurby,
            total,
        ),
    )

    conn.commit()

    conn.close()


def guardar_registro(encargado, evento, caja):
    conn = sqlite3.connect("comercio.sqlite")

    cursor = conn.cursor()

    fecha_hora = datetime.now().strftime("%a %b %d %H:%M:%S %Y")

    cursor.execute(
        "INSERT INTO registro (encargado, fecha, evento, caja) VALUES (?, ?, ?, ?)",
        (encargado, fecha_hora, evento, caja),
    )

    conn.commit()

    conn.close()
