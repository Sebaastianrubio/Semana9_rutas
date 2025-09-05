# db_manager.py

import sqlite3

DATABASE = 'inventario.db'

def crear_tabla():
    """Crea la tabla de productos si no existe."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    print("Base de datos y tabla 'productos' listas.")


def anadir_producto_db(producto):
    """Inserta un nuevo producto en la base de datos."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO productos (id, nombre, cantidad, precio)
        VALUES (?, ?, ?, ?)
    ''', (producto.get_id(), producto.get_nombre(), producto.get_cantidad(), producto.get_precio()))
    conn.commit()
    conn.close()


def eliminar_producto_db(producto_id):
    """Elimina un producto de la base de datos por su ID."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM productos WHERE id = ?', (producto_id,))
    conn.commit()
    conn.close()


def actualizar_producto_db(producto_id, nueva_cantidad, nuevo_precio):
    """Actualiza la cantidad y precio de un producto en la base de datos."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE productos SET cantidad = ?, precio = ? WHERE id = ?
    ''', (nueva_cantidad, nuevo_precio, producto_id))
    conn.commit()
    conn.close()


def cargar_productos_desde_db(inventario):
    """Carga los productos desde la base de datos al objeto Inventario."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM productos')
    filas = cursor.fetchall()
    conn.close()
    
    for fila in filas:
        producto = Producto(fila[0], fila[1], fila[2], fila[3])
        inventario.anadir_producto(producto)
    print("Inventario cargado desde la base de datos.")