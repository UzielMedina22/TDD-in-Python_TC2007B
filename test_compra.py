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

    # Casos de prueba al agregar producto.
    def test_agregar_producto(self):
        # 1. Entradas.
        orden1 = Carrito()
        producto_1 = Producto("Dona", 6.0)
        orden1.agregar_producto(producto_1)

        orden2 = Carrito()
        producto_2_1 = Producto("Baguette", 25.0)
        orden2.agregar_producto(producto_2_1)
        producto_2_2 = Producto("Bolillo", 4.0)
        orden2.agregar_producto(producto_2_2)
        producto_2_3 = Producto("Bolillo", 4.0)
        orden2.agregar_producto(producto_2_3)

        orden3 = Carrito()
        producto_3_1 = Producto("Baguette", 25.0)
        orden3.agregar_producto(producto_3_1)
        producto_3_2 = Producto("Bolillo", 4.0)
        orden3.agregar_producto(producto_3_2)
        producto_3_3 = Producto("Croissant", 10.0)
        orden3.agregar_producto(producto_3_3)
        producto_3_4 = Producto("Dona", 6.0)
        orden3.agregar_producto(producto_3_4)

        orden4 = Carrito()
        producto_4_1 = Producto("  ", 25.0)
        orden4.agregar_producto(producto_4_1)
        producto_4_2 = Producto("X", -2.0)
        orden4.agregar_producto(producto_4_2)
        
        # 2. Resultados esperados.
        res1 = 1                        # Se agregó un producto en la orden 1.
        res2 = "Bolillo"                # Se ubica correctamente el segundo producto agregado a la orden 2.
        res3 = 5                        # Se obtiene la longitud de la orden 3, después de agregarse 5 productos.
        res4 = 0                        # No se pudo agregar un producto sin nombre (cadena vacía o con espacios).
        res5 = 0                        # No se pudo agregar un producto con precio negativo.

        # 3. Pruebas.
        self.assertEqual(len(orden1.lista), res1)
        self.assertEqual(orden2.lista[1].nombre, res2)
        self.assertNotEqual(len(orden3.lista), res3)
        self.assertEqual(len(orden4.lista), res4)
        self.assertEqual(len(orden4.lista), res5)
    
    # Casos de prueba al eliminar un producto.
    def test_eliminar_producto(self):
        # 1. Entradas.
        orden = Carrito()
        p1 = Producto("Dona", 6.0)
        p2 = Producto("Baguette", 25.0)
        p3 = Producto("Bolillo", 4.0)
        p4 = Producto("Bolillo", 4.0)

        orden.agregar_producto(p1)
        orden.agregar_producto(p2)
        orden.agregar_producto(p3)
        orden.agregar_producto(p4)

        # 2. Resultados esperados.
        res1 = True                     # Se elimina Dona correctamente.
        res2 = 3                        # Quedan 3 productos tras eliminar Dona.
        res3 = True                     # Se elimina el primer Bolillo.
        res4 = 2                        # Quedan 2 productos tras eliminar un Bolillo.
        res5 = False                    # No se puede eliminar un producto que no existe.
        res6 = ["Baguette", "Bolillo"]  # Productos restantes al final.

        # 3. Pruebas.
        self.assertEqual(orden.eliminar_producto("Dona"), res1)
        self.assertEqual(len(orden.lista), res2)
        self.assertEqual(orden.eliminar_producto("Bolillo"), res3)
        self.assertEqual(len(orden.lista), res4)
        self.assertEqual(orden.eliminar_producto("Concha"), res5)
        self.assertListEqual([p.nombre for p in orden.lista], res6)
        
    # Casos de prueba del cálculo de subtotal.
    def test_calcular_subtotal(self):
        # 1. Entradas.
        orden1 = Carrito()
        p1 = Producto("Producto1", 100.0)
        p2 = Producto("Producto2", 200.0)
        p3 = Producto("Producto3", 50.0)
        orden1.agregar_producto(p1)
        orden1.agregar_producto(p2)
        orden1.agregar_producto(p3)

        orden2 = Carrito()

        # 2. Resultados esperados.
        resultado1 = orden1.calcular_subtotal()
        resultado2 = orden2.calcular_subtotal()
        res1 = 350.0                                # Subtotal de los artículos de la orden 1.
        res2 = 0.0                                  # Al no haber productos, el subtotal será igual a cero.
        
        # 3. Pruebas.
        self.assertEqual(resultado1, res1)
        self.assertEqual(resultado2, res2)

    # Casos de prueba del cálculo de subtotal con descuentos.
    def test_calcular_subtotal_descuentos(self):
        # 1. Entradas.
        orden1 = Carrito()
        orden1.agregar_producto(Producto("Camisa", 200))
        orden1.agregar_producto(Producto("Pantalón", 300))

        orden2 = Carrito()

        # 2. Entradas.
        resultado1 = orden1.calcular_descuento(10)      # Calcular 10% de descuento del subtotal de la orden 1.
        resultado2 = orden1.calcular_descuento(0)       # Calcular 0% de descuento del subtotal de la orden 1.
        resultado3 = orden1.calcular_descuento(50)      # Calcular 50% de descuento del subtotal de la orden 1.
        resultado4 = orden2.calcular_descuento(10)      # Calcular 10% de descuento del subtotal de la orden 2 (lista vacía).

        # 3. Pruebas.
        self.assertAlmostEqual(resultado1, 450.0)
        self.assertEqual(resultado2, 500.0)
        self.assertEqual(resultado3, 250.0)
        self.assertEqual(resultado4, 0.0)


# Correr los casos de prueba.
if __name__ == "__main__":
    unittest.main()


"""
Referencias:

- Forrester, R. (2024, 28 octubre). Python Destructors: A Complete Guide. Medium. Recuperado el 20 de octubre de 2025, de 
  https://medium.com/@ryan_forrester_/python-destructors-a-complete-guide-6e276cc5e7a9
"""