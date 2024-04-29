import time
import random

class Nodo:
    def __init__(self, nombre, capacidad_buffer=5):
        self.nombre = nombre
        self.conexiones = []
        self.buffer = []
        self.capacidad_buffer = capacidad_buffer

    def agregar_conexion(self, nodo):
        self.conexiones.append(nodo)

    def eliminar_conexion(self, nodo):
        self.conexiones.remove(nodo)

    def enviar_mensaje(self, mensaje):
        for conexion in self.conexiones:
            if random.random() < 0.3:
                pass
            else:
                if len(conexion.buffer) < conexion.capacidad_buffer:
                    conexion.buffer.append(mensaje)
                else:
                    pass

    def procesar_buffer(self):
        while self.buffer:
            mensaje = self.buffer.pop(0)
            for conexion in self.conexiones:
                conexion.recibir_mensaje(mensaje)

    def recibir_mensaje(self, mensaje):
        pass

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

servidor.enviar_mensaje("Hola")

print("Simulando desconexion y reconexion...")
cliente1.eliminar_conexion(servidor)
cliente2.eliminar_conexion(servidor)
cliente3.eliminar_conexion(servidor)
time.sleep(3)
print("Hola")
cliente1.agregar_conexion(servidor)
cliente2.agregar_conexion(servidor)
cliente3.agregar_conexion(servidor)

servidor.procesar_buffer()
servidor.enviar_mensaje("Hola")
