"""
Pruebas automatizadas con pytest para `compra.py`.

Estas pruebas cubren:
 - agregar productos (válidos e inválidos)
 - eliminar productos (existentes y no existentes)
 - cálculo de subtotal
 - cálculo de descuento (varios porcentajes)

Ejecución:
    pytest -q

"""
import pytest

from compra import Producto, Carrito


def test_agregar_producto_valido_e_invalido():
    carrito = Carrito()
    p_ok = Producto("Dona", 6.0)
    carrito.agregar_producto(p_ok)

    # producto con nombre solo espacios no debe agregarse
    p_name_spaces = Producto("   ", 10.0)
    carrito.agregar_producto(p_name_spaces)

    # producto con precio negativo no debe agregarse
    p_neg_price = Producto("X", -5.0)
    carrito.agregar_producto(p_neg_price)

    assert len(carrito.lista) == 1
    assert carrito.lista[0].nombre == "Dona"


def test_agregar_varios_y_posiciones():
    carrito = Carrito()
    carrito.agregar_producto(Producto("Baguette", 25.0))
    carrito.agregar_producto(Producto("Bolillo", 4.0))
    carrito.agregar_producto(Producto("Bolillo", 4.0))

    assert len(carrito.lista) == 3
    assert carrito.lista[1].nombre == "Bolillo"


def test_eliminar_producto_existente_y_no_existente():
    carrito = Carrito()
    carrito.agregar_producto(Producto("Dona", 6.0))
    carrito.agregar_producto(Producto("Baguette", 25.0))
    carrito.agregar_producto(Producto("Bolillo", 4.0))
    carrito.agregar_producto(Producto("Bolillo", 4.0))

    # eliminar existente
    assert carrito.eliminar_producto("Dona") is True
    assert len(carrito.lista) == 3

    # eliminar primer Bolillo
    assert carrito.eliminar_producto("Bolillo") is True
    assert len(carrito.lista) == 2

    # intentar eliminar inexistente
    assert carrito.eliminar_producto("Concha") is False

    # nombres restantes
    nombres = [p.nombre for p in carrito.lista]
    assert nombres == ["Baguette", "Bolillo"]


def test_calcular_subtotal_con_productos_y_sin_productos():
    carrito = Carrito()
    carrito.agregar_producto(Producto("Producto1", 100.0))
    carrito.agregar_producto(Producto("Producto2", 200.0))
    carrito.agregar_producto(Producto("Producto3", 50.0))

    assert carrito.calcular_subtotal() == pytest.approx(350.0)

    carrito_vacio = Carrito()
    assert carrito_vacio.calcular_subtotal() == 0.0


@pytest.mark.parametrize("porcentaje, esperado", [
    (10, 450.0),  # 10% de 500 -> 450
    (0, 500.0),   # 0% -> 500
    (50, 250.0),  # 50% -> 250
])
def test_calcular_descuento_varios(porcentaje, esperado):
    carrito = Carrito()
    carrito.agregar_producto(Producto("Camisa", 200.0))
    carrito.agregar_producto(Producto("Pantalón", 300.0))

    assert carrito.calcular_descuento(porcentaje) == pytest.approx(esperado)


def test_calcular_descuento_en_carrito_vacio():
    carrito = Carrito()
    assert carrito.calcular_descuento(10) == 0.0
