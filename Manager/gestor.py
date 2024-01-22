from cryptography.fernet import Fernet
from BaseDatos import Comunicacion
import base64
import random

class Gestor():
    def __init__(self):
        super()
        self.minus = "abcdefghijklmnopqrstuvwxyz"
        self.mayus = self.minus.upper()
        self.numeros = "0123456789"
        self.simbolos = "@()[]{}*,;/-_¿?.¡!$<#>&+%="
        self.base = self.minus + self.mayus + self.numeros + self.simbolos
        self.longitud = 20
        self.bd = Comunicacion()

    def generar_aleatoreo(self):
        muestra = random.sample(self.base, self.longitud)
        contra = "".join(muestra)
        return contra

    def generar_key(self):
        contra = Fernet.generate_key()
        clave = base64.urlsafe_b64encode(contra)
        return clave

    def encriptar_dato(self, dato, user):
        x = self.bd.buscar_cliente(user)
        _,_,_,_,_,_,key = x[0]
        clave = base64.urlsafe_b64decode(key)
        obj_cifrado = Fernet(clave)
        return obj_cifrado.encrypt(str.encode(dato))

    def desencriptar_dato(self, dato, user):
        x = self.bd.buscar_cliente(user)
        _,_,_,_,_,_,key = x[0]
        clave = base64.urlsafe_b64decode(key)
        obj_cifrado = Fernet(clave)
        return obj_cifrado.decrypt(dato).decode()




