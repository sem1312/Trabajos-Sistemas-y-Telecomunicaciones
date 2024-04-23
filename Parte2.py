import time

class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.conexiones = []

    def agregar_conexion(self, nodo):
        self.conexiones.append(nodo)

    def eliminar_conexion(self, nodo):
        self.conexiones.remove(nodo)

    def enviar_mensaje(self, mensaje):
        print(f"{self.nombre} envía mensaje: {mensaje}")
        for conexion in self.conexiones:
            conexion.recibir_mensaje(mensaje)

    def recibir_mensaje(self, mensaje):
        print(f"{self.nombre} recibe mensaje: {mensaje}")


servidor = Nodo("Servidor")
cliente1 = Nodo("Cliente 1")
cliente2 = Nodo("Cliente 2")
cliente3 = Nodo("Cliente 3")

servidor.agregar_conexion(cliente1)
servidor.agregar_conexion(cliente2)
servidor.agregar_conexion(cliente3)
cliente1.agregar_conexion(servidor)
cliente2.agregar_conexion(servidor)
cliente3.agregar_conexion(servidor)

servidor.enviar_mensaje("¡Hola a todos!")

print("Simulando desconexión y reconexión dinámica...")
cliente1.eliminar_conexion(servidor)
cliente2.eliminar_conexion(servidor)
cliente3.eliminar_conexion(servidor)
time.sleep(3)
print("¡Hola de nuevo a todos!")
cliente1.agregar_conexion(servidor)
cliente2.agregar_conexion(servidor)
cliente3.agregar_conexion(servidor)

servidor.enviar_mensaje("¡Hola de nuevo a todos!")