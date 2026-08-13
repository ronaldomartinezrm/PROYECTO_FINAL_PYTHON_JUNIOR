from models.producto import Producto

class Inventario:


    def __init__(self):
        """
            Aqui represento el inventario en una estructra de lista, porque me interesa
            el orden de inserción.
        """
        self.productos = [] # Es clave no perder de vista el atribbuto de la clase

    def registrar_producto(self, codigo, nombre, precio, stock):
        """
            Permite agregar productos al inventario.
        """
        producto = Producto(codigo, nombre, precio, stock) # aqui creamos internamente el producto que agregaremos al inventario (stand).
        self.productos.append(producto) # aqui agregamos el producto al inventario (lista)
        print(f"El producto {producto.nombre} ha sido agregado exitosamente")

    
    def listar_productos(self):
        """
        Listar significa mostrar todo lo que hay en una lista.
        """
        if not self.productos: # Si No hay elementos en la lista self.productos
            print("No hay productos registrados hasta el momento")
            return
        print("\nLISTADO DE PRODUCTOS")
        print("-"*40)

        for producto in self.productos:
            producto.mostrar()
            print("-"*40)


    def buscar_producto(self, codigo):
        for producto in self.productos:
            if producto.codigo == codigo:
                print("se encontró el producto!")
                return producto

        return None   

    def eliminar_producto(self, codigo):
        """
        1. buscamos el producto
        2. Si no existe (is None): producto no encontrado
        3. Si existe, se carga en la variable producto y lo eliminamos con remove()
        """
        producto = self.buscar_producto(codigo)
        if producto is None:
            print("Producto no encontrado")
            return
        self.productos.remove(producto)
        print("Producto eliminado exitosamente")

    def mostrar_cantidad_productos(self):
        """
            Este método se puede implementar si necesitamos conocer cuantos productos tenemos en inventario.
        """
        return self.productos.__len__()

    