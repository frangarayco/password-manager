import sys
import typing
from PyQt5.QtWidgets import QMessageBox, QInputDialog,QLineEdit,QAbstractItemView, QListView,QApplication, QMainWindow, QHeaderView, QWidget, QTableWidget, QTableWidgetItem, QMenu, QAction, QActionGroup
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, QAbstractListModel, Qt, QStringListModel, QVariant
from PyQt5 import QtCore, QtWidgets, uic
from BaseDatos import Comunicacion
from gestor import Gestor
from fechas import ValidadorFecha

"""
class DatosCompartidos():
    def __init__(self):
        super(DatosCompartidos, self).__init__()

    def nombre_user(self, user)


"""
    
  



class VentanaPrincipal(QMainWindow):
    def __init__(self, ventana):
        super(VentanaPrincipal, self).__init__()
        vl = VentanaLogin()
        self.vl = ventana
        self.click_position = QtCore.QPoint()
        try:
            uic.loadUi('Principal.ui', self)
        except Exception as e:
             print(f"Error al cargar la interfaz gráfica: {e}")
        
        #eliminar barra y titulo 
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        #SizeGrip
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

        #mover ventana
        self.frame_superior.mouseMoveEvent = self.mover_ventana

        #Coneccion botones
        self.bt_perfil.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_perfil))
        self.bt_contra.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_contra))
        self.bt_agregarContra.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_agregar))

        #Menu
        self.bt_menu.clicked.connect(self.mover_menu)

        #Base de datos
        self.baseDatos = Comunicacion()
        
        #Gestor
        self.gestor = Gestor()

        #Inicio de la pagina perfil 
        self.text_cambiarContra.setReadOnly(True)
        self.text_repetir.setReadOnly(True)
        self.text_user.setReadOnly(True)
        self.bt_cambiar_contra.setEnabled(False)

        #Ajuste de tabla 
        self.listadoContras.setColumnWidth(1,592)
        self.listadoContras.setColumnWidth(0,150)

        #Botones menu
        self.bt_perfil.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_perfil))
        self.bt_contra.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_contra))
        self.bt_agregarContra.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_agregar))

        #Seleccion una fila en la tabla 
        self.listadoContras.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listadoContras.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.listadoContras.setSelectionMode(QAbstractItemView.SingleSelection)
        self.listadoContras.clicked.connect(self.seleccionar_fila)

        #Control barra de titulo 
        self.bt_minimizar.clicked.connect(self.control_bt_minimizar)
        self.bt_cerrar.clicked.connect(lambda: self.close())

        #Botones
        self.bt_mostrar_contra.clicked.connect(self.mostrar_contra)
        self.bt_buscar_contra.clicked.connect(self.buscar_contra)
        self.bt_modificar_perfil.clicked.connect(self.modificar_datos)
        self.bt_guardar_agregar.clicked.connect(self.agregar_contra)
        self.bt_eliminar_contra.clicked.connect(self.eliminar_contra)
        self.bt_cambiar_contra.clicked.connect(self.modificar_contra)
        self.bt_perfil.clicked.connect(self.mostrar_cliente)
        self.bt_desencriptar.clicked.connect(self.desencriptar_todo)
        self.bt_copiar_agregar.clicked.connect(self.copiar_aleatorio)
        self.bt_contra.clicked.connect(self.limpiar_contra)
        self.bt_agregarContra.clicked.connect(self.limpiar_agregar)

       
        #otros botones
        self.checkBox_mostrar1.clicked.connect(self.mostrar_contenido)
        self.checkBox_mostrar2.clicked.connect(self.mostrar_contenido2)
        self.check_mostrar.clicked.connect(self.mostrar_contenido3)
        self.check_habilitar.clicked.connect(self.habilitar_cambio)

         
        #botones copn metodos en otra clase
        self.bt_generar_agregar.clicked.connect(self.generar_aleatoreo)

        #Acciones
        self.textRepetir.returnPressed.connect(self.agregar_contra)
        self.textBuscar.returnPressed.connect(self.buscar_contra)
        
    
    def limpiar_contra(self):
        self.textBuscar.setText("")
        self.signal_contra.setText("")
        self.mostrarBusqueda.setText("")

    def limpiar_agregar(self):
        self.textSitio.setText("")
        self.textContra.setText("")
        self.textRepetir.setText("")
        self.signal_agregar.setText("")
        self.textCopiar.setText("")


    def mover_menu(self):
        if self.frame_control.isVisible(): 
            width = self.frame_control.width()
            normal = 0 
            if width == 0:
                extender = 200
            else: 
                extender = normal
            self.animacion = QPropertyAnimation(self.frame_control, b'minimumWidth')
            self.animacion.setDuration(300)
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion.start()
    

    def control_bt_minimizar(self):
        self.showMinimized()

    def control_bt_normal(self):
        self.showNormal()

    def control_bt_maximizar(self):
        self.showMaximized()

    #SizeGrip
    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

    
    def mover_ventana(self, event):
        if self.isMaximized() == False: 
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.click_position)
                self.click_position = event.globalPos()
                event.accept()
        if event.globalPos().y() <=10:
            self.showMaximized()
        else: 
            self.showNormal()
    
    """

    # Mover ventana 
    def mousePressEvent(self, event):
        self.click.position = event.globalPos()

    """
    def seleccionar_fila(self): 
        fila = "a"
        filaSelec = self.listadoContras.selectedItems()
        if filaSelec:
            fila = filaSelec[0].row()
        else: 
            self.signal_contra.setText("Error, debe seleccionar una fila")
        return fila 
    
    def generar_aleatoreo(self):
        contra = self.gestor.generar_aleatoreo()
        self.textCopiar.setText(contra)
   
    def mostrar_contenido(self):
        if self.checkBox_mostrar1.isChecked():
            self.textContra.setEchoMode(QLineEdit.Normal)
        else:
            self.textContra.setEchoMode(QLineEdit.Password)

    def mostrar_contenido2(self):
        if self.checkBox_mostrar2.isChecked():
            self.textRepetir.setEchoMode(QLineEdit.Normal)
        else:
            self.textRepetir.setEchoMode(QLineEdit.Password)

    def mostrar_contenido3(self):
        if self.check_mostrar.isChecked():
            self.text_cambiarContra.setEchoMode(QLineEdit.Normal)
            self.text_repetir.setEchoMode(QLineEdit.Normal)
        else:
            self.text_repetir.setEchoMode(QLineEdit.Password)
            self.text_cambiarContra.setEchoMode(QLineEdit.Password)


    def habilitar_cambio(self):
        if self.check_habilitar.isChecked():
            self.bt_cambiar_contra.setEnabled(True)
            self.text_cambiarContra.setReadOnly(False)
            self.text_repetir.setReadOnly(False)
        else:
            self.bt_cambiar_contra.setEnabled(False)
            self.text_cambiarContra.setReadOnly(True)
            self.text_repetir.setReadOnly(True)

    def desencriptar_todo(self):
        dialogo = QInputDialog(self)
        dialogo.setWindowTitle("Ingresar Contraseña")
        dialogo.setLabelText("Por favor, ingrese la contraseña:")
        dialogo.setInputMode(QInputDialog.TextInput)
        dialogo.setTextEchoMode(QLineEdit.Password)

        text_edit = dialogo.findChild(QLineEdit)
        if text_edit is not None:
            text_edit.setMinimumWidth(300)  

        resu = dialogo.exec_()
        texto = dialogo.textValue()
        if resu : 
            user = self.vl.text_user.text()
            dato = self.baseDatos.buscar_cliente(user)
            _,_,_,_,_,contra,_ = dato [0]
            contraDescrypt = self.gestor.desencriptar_dato(contra,user)
            if texto == contraDescrypt:
                self.mostrar_descript(user)
                self.descript_busqueda(user)
            else:
                QMessageBox.warning(self, "Iniciar Sesión", "Contraseña o nombre de usuario incorrecto")
       

    def mostrar_descript(self,user):
        if self.listadoContras.rowCount() > 0:
            self.signal_contra.setText("")
            dato = self.baseDatos.mostrar_contraseña(user)
            i = len(dato)
            self.listadoContras.setRowCount(i)
            tableRow = 0
            for row in dato:
                contra = self.gestor.desencriptar_dato(row[1],user)
                self.listadoContras.setItem(tableRow,0,QtWidgets.QTableWidgetItem(row[0]))
                self.listadoContras.setItem(tableRow,1,QtWidgets.QTableWidgetItem(contra)) 
                tableRow += 1
        else: 
            self.descript_busqueda(user)
    
    def descript_busqueda(self,user):
        nombre = self.textBuscar.text()
        dato = self.baseDatos.buscar_contraseña(nombre,user)
        if dato != []:
            sitio, contra, _ = dato[0]
            contraDescrypt = self.gestor.desencriptar_dato(contra,user)
            self.mostrarBusqueda.setText(contraDescrypt)
    

    def mostrar_cliente(self): 
        self.signal_perfil.setText("")
        user = self.vl.text_user.text()
        dato = self.baseDatos.mostrar_cliente(user)
        nombre, apellido, user, mail, nacimiento, _ , _= dato[0]
        self.text_nombre.setText(nombre)
        self.text_apellido.setText(apellido)
        self.text_user.setText(user)
        self.text_mail.setText(mail)
        self.text_nacimiento.setText(nacimiento)

    def modificar_contra(self): 
        self.signal_perfil.setText("")
        self.text_cambiarContra.setReadOnly(False)
        self.text_repetir.setReadOnly(False)
        if self.text_cambiarContra.text() != "":
            if self.text_cambiarContra.text() == self.text_repetir.text():
                contra = self.text_cambiarContra.text()
                user = self.text_user.text()
                contraEncrypt = self.gestor.encriptar_dato(contra,user)
                self.baseDatos.modificar_contra(user,contraEncrypt)
                self.signal_perfil.setText("La contraseña se cambio correctamente")
            else:
                self.signal_perfil.setText("Las claves no son iguales")
                
        else: 
            self.signal_perfil.setText("Error, debe completar los campos de contraseña")
        

    def copiar_aleatorio(self):
        if self.textCopiar.text() != "":
            copy = self.textCopiar.text()
            clipboard = QApplication.clipboard()
            clipboard.setText(copy)
            self.signal_agregar.setText("Se copio correctamente")
        


    def agregar_contra(self):
        sitio = self.textSitio.text()
        if (self.textContra.text() == self.textRepetir.text()):
            contra = self.textContra.text()
            if sitio != "" and contra != "":
                user = self.vl.text_user.text()
                contraEncrypt = self.gestor.encriptar_dato(contra,user)
                self.baseDatos.agregar_contraseña(sitio,contraEncrypt,user)
                self.signal_agregar.setText("Se agrego correctamente")
                self.textSitio.clear()
                self.textContra.clear()
                self.textRepetir.clear()
            else:
                self.signal_agregar.setText("Completar todos los campos")
        else:
            self.signal_agregar.setText("Las claves no son iguales, Error!!")

        
        
    def mostrar_contra(self):
        self.signal_contra.setText("")
        user = self.vl.text_user.text()
        dato = self.baseDatos.mostrar_contraseña(user)
       ## if dato != []:
        i = len(dato)
        self.listadoContras.setRowCount(i)
        tableRow = 0
        for row in dato:
            self.listadoContras.setItem(tableRow,0,QtWidgets.QTableWidgetItem(row[0]))
            self.listadoContras.setItem(tableRow,1,QtWidgets.QTableWidgetItem(row[1]))
            tableRow += 1
      ##  else: 
    ##    self.signal_contra.setText("No hay datos para mostrar")
        



    def buscar_contra(self):
        nombre = self.textBuscar.text()
        user = self.vl.text_user.text()
        dato = self.baseDatos.buscar_contraseña(nombre,user)
        if dato != []:
            _, contra, _ = dato[0]
            self.mostrarBusqueda.setText(contra)
            self.signal_contra.setText("Encontrado")
        else:
            self.signal_contra.setText("No existe el sitio")
            self.mostrarBusqueda.setText("")
   
    def eliminar_contra(self):
        fila = self.seleccionar_fila()
        user = self.vl.text_user.text()
        if fila != "a":
            sitio = self.listadoContras.item(fila, 0).text()
            self.baseDatos.eliminar_contraseña(sitio,user)
            self.signal_contra.setText("Se elimino correctamente")
            self.listadoContras.removeRow(fila+1)
            self.mostrar_contra()
        else:   
            self.signal_contra.setText("Error, debe seleccionar una fila")
   
    def modificar_datos(self):
        user = self.text_user.text()
        datos = self.baseDatos.buscar_cliente(user)
        if datos != []:
            nombre = self.text_nombre.text()
            apellido = self.text_apellido.text()
            mail = self.text_mail.text()
            nacimiento = self.text_nacimiento.text()
            self.baseDatos.modificar_datos(nombre,apellido,mail,nacimiento,user)
            self.signal_perfil.setText("Los datos se modificaron correctamente")
        else:
            self.signal_perfil.setText("No se encontro al usuario")
       
        

class VentanaLogin(QMainWindow):
    def __init__(self):
        super(VentanaLogin, self).__init__()
        self.click_position = QtCore.QPoint()
        try:
            uic.loadUi('Login.ui', self)
        except Exception as e:
             print(f"Error al cargar la interfaz gráfica: {e}")
        
        #Control barra de titulo 
        self.bt_minimizar.clicked.connect(self.control_bt_minimizar)
        self.bt_cerrar.clicked.connect(lambda: self.close())

        #eliminar barra y titulo 
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        #Base de datos
        self.baseDatos = Comunicacion()

        #Gestor
        self.gestor = Gestor()

        #Botones
        self.bt_iniciar_sesion.clicked.connect(self.iniciar_sesion)
        self.bt_registro.clicked.connect(self.registrar)
        self.check_mostrar.clicked.connect(self.mostrar_contenido4)

        #Acccion
        self.text_contra.returnPressed.connect(self.iniciar_sesion)
        

    def control_bt_minimizar(self):
        self.showMinimized()

    def mostrar_contenido4(self):
        if self.check_mostrar.isChecked():
            self.text_contra.setEchoMode(QLineEdit.Normal)
        else:
            self.text_contra.setEchoMode(QLineEdit.Password)
    

    def iniciar_sesion(self):
        if self.text_user.text() != "" and self.text_contra.text() != "":
            user = self.text_user.text()
            contra = self.text_contra.text()
            dato = self.baseDatos.buscar_cliente(user)
            if dato != []:
                _, _, datoUser, _, _, datoContra,_ = dato[0]
                contraDescrypt = self.gestor.desencriptar_dato(datoContra,datoUser)
                if user != datoUser or contraDescrypt != contra:
                    QMessageBox.warning(self, "Iniciar Sesión", "Contraseña o nombre de usuario incorrecto")
                else:
                    self.abrir_ventanaPrincipal()
            else: 
                QMessageBox.warning(self, "Iniciar Sesión", "Contraseña o nombre de usuario incorrecto")
        else: 
            self.signal_login.setText("Error, debe completar todos los datos")
    
    def registrar(self):
        vr = VentanaRegistro()
        vr.show()
        self.close()
    

    def abrir_ventanaPrincipal(self):
        vp = VentanaPrincipal(self)
        vp.show()
        self.close()



class VentanaRegistro(QMainWindow): 
    def __init__(self):
        super(VentanaRegistro, self).__init__()
        self.click_position = QtCore.QPoint()
        try:
            uic.loadUi('Registro.ui', self)
        except Exception as e:
             print(f"Error al cargar la interfaz gráfica: {e}")
        

        #Base de datos
        self.baseDatos = Comunicacion()

        #Fecha
        self.fecha = ValidadorFecha()

        #Gestor
        self.gestor = Gestor()

        #Control barra de titulo 
        self.bt_minimizar.clicked.connect(self.control_bt_minimizar)
        self.bt_cerrar.clicked.connect(lambda: self.close())

        #eliminar barra y titulo 
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        #Botones
        self.bt_registrar.clicked.connect(self.agregar_cliente)
        self.bt_genera.clicked.connect(self.generar_aleatorio)
        self.bt_copiar.clicked.connect(self.copiar_aleatorio)
        self.check_mostrar.clicked.connect(self.mostrar_contenido)
        self.check_repetir.clicked.connect(self.mostrar_contenido2)

        

    def control_bt_minimizar(self):
        self.showMinimized()

    def mostrar_contenido(self):
        if self.check_mostrar.isChecked():
            self.text_contra.setEchoMode(QLineEdit.Normal)
        else:
            self.text_contra.setEchoMode(QLineEdit.Password)

    def mostrar_contenido2(self):
        if self.check_repetir.isChecked():
            self.text_repetir.setEchoMode(QLineEdit.Normal)
        else:
            self.text_repetir.setEchoMode(QLineEdit.Password)

    def agregar_cliente(self):
        self.signal_registro.setText("")
        self.signal_user.setText("")
        self.signal_nacimiento.setText("")
        nombre = self.text_nombre.text()
        apellido = self.text_apellido.text()
        dato = self.baseDatos.buscar_cliente(self.text_user.text())
        if dato == []:
            user = self.text_user.text()
            if self.fecha.es_fecha_valida(self.text_nacimiento.text()):
                nacimiento =  self.text_nacimiento.text()
                mail = self.text_mail.text()
                if self.text_contra.text() == self.text_repetir.text():
                    contra = self.text_contra.text()
                    if nombre != "" or apellido != "" or user != "" or nacimiento != "" or mail != "" or contra != "":
                        clave = self.gestor.generar_key()
                        self.baseDatos.agregar_cliente(nombre,apellido,user,mail,nacimiento,contra,clave) 
                        contraEncrypt = self.gestor.encriptar_dato(contra, user)
                        self.baseDatos.modificar_contra(user,contraEncrypt)
                        self.baseDatos.crearTabla(user)
                        QMessageBox.information(self, "Registro", "Se registro con exito")
                        self.cerrarVentana()
                    else: 
                        self.signal_registro.setText("Debe completar todos los campos")
                else: 
                    self.signal_registro.setText("Error, las claves son distintas")
            else: 
                self.signal_nacimiento.setText("La fecha es invalida")
        else: 
            self.signal_user.setText("El nombre de usuario ya existe")
        
    def generar_aleatorio(self): 
        contra = self.gestor.generar_aleatoreo()
        self.text_aleatorio.setText(contra)

    def copiar_aleatorio(self):
        copy = self.text_aleatorio.text()
        clipboard = QApplication.clipboard()
        clipboard.setText(copy)
        self.signal_registro.setText("Se copio correctamente")

    def cerrarVentana(self):
        self.close()
        vl = VentanaLogin()
        vl.show()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mi_app = VentanaLogin()
    mi_app.show()
    sys.exit(app.exec()) 
    


    


    




    

     
            




    
    


        


