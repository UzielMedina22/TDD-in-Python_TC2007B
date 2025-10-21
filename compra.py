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
Descripción: Clases del producto y de la orden de compra.
"""

# Clase de un producto.
class Producto():
    # Inicialización de los datos del producto. T: O(1), E: O(1)
    def __init__(self, c_Nombre: str, c_Precio: float):
        self.nombre = c_Nombre or ""
        self.precio = c_Precio or 0.0
        

# Clase de una orden de compra.
class Orden():
    # Inicialización de la orden. T: O(1), E: O(1)
    def __init__(self):
        self.lista = []
    
    # Agregar un producto. T: O(1), E: O(1)
    def agregar_producto(self, p: Producto):
        if p.nombre.strip() != "" and p.precio > 0.0:
            self.lista.append(p)