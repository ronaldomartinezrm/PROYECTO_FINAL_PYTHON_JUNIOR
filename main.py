from utils.menu import mostrar_menu
from services.inventario import Inventario
from services.ventas import Ventas
from models.producto import Producto

def main():

    # Dependencias de la clase main
    inventario = Inventario() #instanciamos la clase inventario
    ventas = Ventas() # instanciamos la clase ventas

    while True:
        opcion = mostrar_menu()

        if opcion ==  "1":
            inventario.registrar_producto()

        elif opcion == "2":
            inventario.listar_productos()

        elif opcion == "3":
            inventario.buscar_producto()

        elif opcion == "4":
            inventario.eliminar_producto()

        elif opcion == "5":
            ventas.registrar_venta()

        elif opcion == "6":
            ventas.listar_ventas()

        elif opcion == "7":
            ventas.total_vendido()

        elif opcion == "8":
            print("\nGracias por utilizar el sistema.")
            break

        else:
            print("\nOpción inválida.")


"""
producto = Producto(
    "P001",
    "teclado Logitech",
    180000,
    20
)

producto.mostrar()

print("\n¿Hay 5 unidades disponibles?")
print(producto.hay_stock(5))

print("\n¿Hay 25 unidades disponibles?")
print(producto.hay_stock(25))


print("\nVendiendo 3 unidades...")
resultado = producto.disminuir_stock(3)

if(resultado):
    print("Venta realizada")
else:
    print("Venta no realizada")

producto.mostrar()

"""

inventario = Inventario()
print("Se crean dos productos...")
inventario.registrar_producto("P001", "teclado logitech", 18000, 10)
inventario.registrar_producto("P002", "mouse logitech", 2000, 30)

inventario.listar_productos()
print("buscando el producto P002...")
producto_encontrado= inventario.buscar_producto("P003")
print(f"producto encontrado:")
if producto_encontrado != None:
    producto_encontrado.mostrar()
else:
    print("No se encontró el producto")


print(f"cantidad de productos en lista: {inventario.mostrar_cantidad_productos()}")

print("Eliminando el producto P002")
inventario.eliminar_producto("P002")
print(f"cantidad de productos en lista: {inventario.mostrar_cantidad_productos()}")

#main()