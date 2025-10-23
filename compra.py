"""
TDD in Python (Clases)

Integración de seguridad informática en redes y sistemas de software (TC2007B).

Docente: Dr. Edgar León Sandoval

Equipo:
    - Miguel de Jesús Degollado Macías (A012553)
    - Jorge Antonio Flores Hernández (A01254623)
    - Jonathan Uziel Medina Rodríguez (A1255048)

Fecha de entrega: 23/10/2025
_________________________________________________________________________________
Descripción: Clases del producto y del carrito de compra.
"""

# Clase de un producto.
class Producto():
    # Inicialización de los datos del producto. T: O(1), E: O(1)
    def __init__(self, c_Nombre: str, c_Precio: float):
        self.nombre = c_Nombre or ""
        self.precio = c_Precio or 0.0
        

# Clase de un carrito de compras.
class Carrito():
    # Inicialización del carrito. T: O(1), E: O(1)
    def __init__(self):
        self.lista = []     # Lista de productos en el carrito.
    
    # Agregar un producto. T: O(1), E: O(1)
    def agregar_producto(self, p: Producto):
        # Agregar producto si tiene nombre y precio igual o mayor a cero. 
        if p.nombre.strip() != "" and p.precio > -1.0:
            self.lista.append(p)

    # Eliminar un producto por nombre. T: O(n), E: O(1)
    def eliminar_producto(self, nombre: str):
        for i, producto in enumerate(self.lista):
            if producto.nombre == nombre:
                del self.lista[i]
                return True  # Se eliminó con éxito
            
        return False # No se encontró el producto para eliminar
    
    # Calcular el subtotal del carrito. T: O(n), E: O(1)
    def calcular_subtotal(self) -> float:
        subtotal = 0.0
        if self.lista:                      # Sumar si la lista tiene productos.
            for producto in self.lista:
                subtotal += producto.precio
        return subtotal                        # Devolver el subtotal o cero (si la lista está vacía). 
    
    # Calcular el descuento del subtotal. T: O(n), E: O(1)
    def calcular_descuento(self, porcentaje: float) -> float:
        subtotal = self.calcular_subtotal()
        descuento = subtotal * (porcentaje / 100)
        subtotal -= descuento
        return subtotal

    
"""
Referencias:

- Nehme, A. (2025, 16 febrero). How to trim a string in Python: Three different methods. DataCamp. Recuperado el 20 de octubre de 2025, de 
  https://www.datacamp.com/tutorial/python-trim
"""