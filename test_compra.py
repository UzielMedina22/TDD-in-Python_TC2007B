"""
TDD in Python

Integración de seguridad informática en redes y sistemas de software (TC2007B).

Docente: Dr. Edgar León Sandoval

Equipo:
    - Miguel de Jesús Degollado Macías (A012553)
    - Jorge Antonio Flores Hernández (A01254623)
    - Jonathan Uziel Medina Rodríguez (A1255048)

Fecha de entrega: 23/10/2025
_________________________________________________________________________________
Descripción: Pruebas TDD sobre la compra de un producto.
"""

import unittest
from compra import *


# Casos de prueba de una compra.
class TestCompra(unittest.TestCase):
    def test_add_items(self):
        # 1. Entradas.
        orden1 = Orden()
        producto_1 = Producto("Dona", 6.0)
        orden1.agregar_producto(producto_1)

        orden2 = Orden()
        producto_2_1 = Producto("Baguette", 25.0)
        orden2.agregar_producto(producto_2_1)
        producto_2_2 = Producto("Bolillo", 4.0)
        orden2.agregar_producto(producto_2_2)
        producto_2_3 = Producto("Bolillo", 4.0)
        orden2.agregar_producto(producto_2_3)

        orden3 = Orden()
        producto_3_1 = Producto("Baguette", 25.0)
        orden3.agregar_producto(producto_3_1)
        producto_3_2 = Producto("Bolillo", 4.0)
        orden3.agregar_producto(producto_3_2)
        producto_3_3 = Producto("Croissant", 10.0)
        orden3.agregar_producto(producto_3_3)
        producto_3_4 = Producto("Dona", 6.0)
        orden3.agregar_producto(producto_3_4)

        orden4 = Orden()
        producto_4_1 = Producto("", 25.0)
        orden4.agregar_producto(producto_4_1)
        producto_4_2 = Producto("X", 0.0)
        orden4.agregar_producto(producto_4_2)
        
        # 2. Resultados esperados.
        res1 = 1
        res2 = "Bolillo"
        res3 = 5
        res4 = []
        res5 = []

        # 3. Pruebas.
        self.assertEqual(len(orden1.lista), res1)
        self.assertEqual(orden2.lista[1].nombre, res2)
        self.assertNotEqual(len(orden3.lista), res3)
        self.assertEqual(len(orden4.lista), 0)
        self.assertEqual(len(orden4.lista), 0)


# Correr los casos de prueba.
if __name__ == "__main__":
    unittest.main()