import mysql.connector

class Comunicacion():
    def __init__(self):
        self.conexion = mysql.connector.connect(user='root', password='', host = 'localhost', database='gestor', port='3306')

    def crearTabla (self,user):
        txt = "contraseña"
        nombre = f"{txt}_{user}"
        cursor = self.conexion.cursor()
        bd = f''' CREATE TABLE `{nombre}` (
                    sitio VARCHAR(45),
                    contraseña VARCHAR(10000),
                    user VARCHAR(45))'''
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()

    def agregar_contraseña(self,sitio,contraseña,user):
        txt = "contraseña"
        nombre = f"{txt}_{user}"
        cursor = self.conexion.cursor()
        bd = f'''INSERT INTO `{nombre}` (sitio,contraseña,user) VALUES (%s,%s,%s)'''
        datos = (sitio,contraseña,user)
        cursor.execute(bd, datos)
        self.conexion.commit()
        cursor.close()

    def agregar_cliente(self,nombre,apellido,user,mail,nacimiento,contra,clave):
        cursor = self.conexion.cursor()
        bd = '''INSERT INTO clientes (Nombre, Apellido, User, Mail, Nacimiento, Contra, Clave) VALUES (%s,%s,%s,%s,%s,%s,%s)'''
        datos = (nombre,apellido,user,mail,nacimiento,contra,clave)
        cursor.execute(bd, datos)
        self.conexion.commit()
        cursor.close()    

    def eliminar_contraseña(self,sitio,user):
        txt = "contraseña"
        nombre = f"{txt}_{user}"
        cursor = self.conexion.cursor()
        bd = f'''DELETE FROM `{nombre}` WHERE sitio = ('{sitio}')'''
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()

    def mostrar_contraseña(self,user):
        txt = "contraseña"
        nombre = f"{txt}_{user}"
        cursor = self.conexion.cursor()
        bd= f'''SELECT * FROM `{nombre}`'''
        cursor.execute(bd)
        lista = cursor.fetchall()
        return lista
    
        
    def buscar_contraseña(self,sitio,user):
        txt = "contraseña"
        nombre = f"{txt}_{user}"
        cursor = self.conexion.cursor()
        bd = f'''SELECT * FROM `{nombre}` WHERE sitio = ('{sitio}')'''
        cursor.execute(bd)
        contra = cursor.fetchall()
        cursor.close()
        return contra
    
    def buscar_cliente(self,user):
        cursor = self.conexion.cursor()
        bd = '''SELECT * FROM clientes WHERE User = ('{}')'''.format(user)
        cursor.execute(bd)
        datos = cursor.fetchall()
        cursor.close()
        return datos
    
    def modificar_datos(self,nombre,apellido,mail,nacimiento,user):
        cursor = self.conexion.cursor()
        bd = '''UPDATE clientes SET Nombre='{}', Apellido='{}', Mail='{}', Nacimiento='{}' WHERE user = '{}' '''.format(nombre,apellido,mail,nacimiento,user)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()

    def modificar_contra(self,user,contra):
        cursor = self.conexion.cursor()
        bd = '''UPDATE clientes SET Contra = (%s) WHERE user = (%s) '''
        dato = (contra,user)
        cursor.execute(bd,dato)
        self.conexion.commit()
        cursor.close()

    def mostrar_cliente(self,user):
        cursor = self.conexion.cursor()
        bd= f'''SELECT * FROM clientes WHERE user = ('{user}')'''
        cursor.execute(bd)
        lista = cursor.fetchall()
        return lista





