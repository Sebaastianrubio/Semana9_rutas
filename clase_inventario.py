# clases_inventario.py

class Producto:
    """Clase que representa un producto en el inventario."""

    def __init__(self, producto_id, nombre, cantidad, precio):
        self._producto_id = producto_id
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Métodos para obtener (getters) los atributos
    def get_id(self):
        return self._producto_id

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    # Métodos para establecer (setters) los atributos
    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    def set_cantidad(self, nueva_cantidad):
        self._cantidad = nueva_cantidad

    def set_precio(self, nuevo_precio):
        self._precio = nuevo_precio

    def __str__(self):
        return f"ID: {self._producto_id} | Nombre: {self._nombre} | Cantidad: {self._cantidad} | Precio: ${self._precio}"


class Inventario:
    """Clase para gestionar la colección de productos."""

    def __init__(self):
        # Un diccionario es la mejor opción para búsquedas rápidas por ID.
        self.productos = {}  

    def anadir_producto(self, producto):
        if producto.get_id() in self.productos:
            print("Error: El producto con este ID ya existe.")
        else:
            self.productos[producto.get_id()] = producto
            print(f"Producto '{producto.get_nombre()}' añadido con éxito.")

    def eliminar_producto(self, producto_id):
        if producto_id in self.productos:
            del self.productos[producto_id]
            print(f"Producto con ID {producto_id} eliminado.")
        else:
            print(f"Error: Producto con ID {producto_id} no encontrado.")

    def actualizar_producto(self, producto_id, nueva_cantidad, nuevo_precio):
        if producto_id in self.productos:
            producto = self.productos[producto_id]
            producto.set_cantidad(nueva_cantidad)
            producto.set_precio(nuevo_precio)
            print(f"Producto con ID {producto_id} actualizado.")
        else:
            print(f"Error: Producto con ID {producto_id} no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        resultados = [p for p in self.productos.values() if nombre.lower() in p.get_nombre().lower()]
        return resultados

    def mostrar_todos_los_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("\n--- Inventario Completo ---")
            for producto in self.productos.values():
                print(producto)