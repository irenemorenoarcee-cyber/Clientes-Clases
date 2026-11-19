#un Cliente (es un objeto) compra un Producto(es un objeto)
#crear la clase Cliente (se puede crear una super clase que se llame persona, del que hereda Cleinte que es una sub clase)
#crear la clase Producto
#metodo fuera-> def comprar_producto_cliente(cleinte, producto, unidades
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
class Cliente(Persona):
    def __init__(self, nombre, apellido, método_pago):
        super().__init__(nombre, apellido)
        self.método_pago = método_pago
class Producto:
    def __init__(self, referencia, precio, cantidad):
        self.referencia = referencia
        self.precio = precio
        self.cantidad = cantidad
    def precio_total(self):
        return self.precio * self.cantidad
def precio_total(self):
    return self.precio * self.cantidad
producto = Producto("01234X", "5", "4")
print(Producto("01234X", 5, 4).precio_total())
cliente = Cliente("Casilda", "Domecq", "PayPal")
print(cliente.nombre, cliente.apellido, cliente.método_pago)