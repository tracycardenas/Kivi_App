from kivy.uix.label import Label
from kivy.uix.popup import Popup

from ControladorAlumno import ControladorAlumno


class ViewAlumno:

    def __init__(self, gerencVentana):
        self._gerencVentana = gerencVentana

    def registroActualAlumno(self):
        result = ""
        try:
            ventana = self._gerencVentana.get_screen("RegistroAlumno")
            idAlumno = ventana.ids.lblIdAlumno.text
            nombreAlumno = ventana.ids.txtNombreAlumno.text
            fechaNacimiento =ventana.ids.txtFechaNacAlumno.text
            materia =ventana.ids.spMateria.text

            controlador = ControladorAlumno()
            if ventana.ids.btRegistroActualAlumno.text == "Eliminar":
                result = controlador.eliminarAlumno(idAlumno)
            else:
                result = controlador.guardadActualizarAlumno(id=idAlumno,
                                                        nombre=nombreAlumno,
                                                        fechaNacimiento=fechaNacimiento,
                                                        materia=materia)
            self._popVentana(result)
            self._limpiarventana(ventana)
        except Exception as e:
            print(str(e))
            self._popVentana(f"No fue posible {ventana.ids.btRegistroActualAlumno.text} el alumno!!!")


    def _limpiarventanaListar(self,ventana):
        encabezado = [
            ventana.ids.colIdAlumno,
            ventana.ids.colNombreAlumno,
            ventana.ids.colFechaNac,
            ventana.ids.colMateria,
            ventana.ids.lblActual,
            ventana.ids.lblEliminar
            ]
        ventana.ids.listaAlumnos.clear_widgets()
        for c in encabezado:
            ventana.ids.listaAlumnos.add_widget(c)


    def buscarAlumnos(self, nombreB=""):
        control = ControladorAlumno()
        ventana = self._gerencVentana.get_screen("ListarAlumnos")
        idBusc = ventana.ids.inputIdAlumno.text
        resultado = control.buscarAlumno(id=idBusc, nombreBuscar=nombreB)
        self._limpiarventanaListar(ventana)
        for res in resultado:
            for r in res:
                if r.text == "Actualizar" or r.text == "Eliminar":
                    r.bind(on_release= self.mostrarVentanaAt)
                ventana.ids.listaAlumnos.add_widget(r)

    def mostrarVentanaAt(self,boton):
        ventanaRegistro = self._gerencVentana.get_screen("RegistroAlumno")
        ventanaRegistro.ids.spMateria.values = self._mostrarSpinner()
        alumnos=[]
        if boton.id:
            id = str(boton.id).replace("bt", "")
            control = ControladorAlumno()
            alumnos = control.buscarAlumno(id=id)
        for a in alumnos:
            ventanaRegistro.ids.lblIdAlumno.text = a[0].text
            ventanaRegistro.ids.txtNombreAlumno.text = a[1].text
            ventanaRegistro.ids.txtFechaNacAlumno.text = a[2].text
            ventanaRegistro.ids.spMateria.text = a[3].text
        ventanaRegistro.ids.btRegistroActualAlumno.text = boton.text
        self._limpiarventanaListar(self._gerencVentana.get_screen("ListarAlumnos"))
        self._gerencVentana.ventanaRegistroAlumno()

    def mostrarVentanaAtRegistro(self,boton):
        ventanaRegistro = self._gerencVentana.get_screen("RegistroAlumno")
        ventanaRegistro.ids.spMateria.values = self._mostrarSpinner()
        alumnos=[]
        for a in alumnos:
            ventanaRegistro.ids.lblIdAlumno.text = a[0].text
            ventanaRegistro.ids.txtNombreAlumno.text = a[1].text
            ventanaRegistro.ids.txtFechaNacAlumno.text = a[2].text
            ventanaRegistro.ids.spMateria.text = a[3].text
        ventanaRegistro.ids.btRegistroActualAlumno.text = boton.text
        self._limpiarventanaListar(self._gerencVentana.get_screen("ListarAlumnos"))
        self._gerencVentana.ventanaRegistroAlumno()

    def _mostrarSpinner(self):
        listaValores = self._buscarMateriasventana()
        return listaValores


    def _buscarMateriasventana(self):
        control = ControladorAlumno()
        materias = control.buscarMaterias()
        nombresMaterias =[]
        for materia in materias:
            nombresMaterias.append(materia.nombre)
        return nombresMaterias

    def _limpiarventana(self, ventana):
        ventana.ids.lblIdAlumno.text = ""
        ventana.ids.txtNombreAlumno.text = ""
        ventana.ids.txtFechaNacAlumno.text = ""
        ventana.ids.spMateria.text = "Seleccione..."
        ventana.ids.btRegistroActualAlumno.text = "Registrar"

    def _popVentana(self, texto=""):
        popup = Popup(title='Informacion', content=Label(text=texto),
        auto_dismiss=True)
        popup.size_hint = (0.98, 0.4)
        popup.open()

    def alternarBusq(self, tipo):
        ventana = self._gerencVentana.get_screen("ListarAlumnos")
        if ventana.ids.inputIdAlumno is not None:
            ventana.ids.inputIdAlumno.text = ""
        if ventana.ids.inputBuscNombre is not None:
            ventana.ids.inputBuscNombre.text = ""
        buscNombre = ventana.ids.buscNombre
        buscId = ventana.ids.buscId
        ventana.ids.busquedas.remove_widget(buscNombre)
        ventana.ids.busquedas.remove_widget(buscId)
        if tipo == "id":
            buscId.active = True
            buscNombre.active = False
            ventana.ids.busquedas.add_widget(ventana.ids.buscId,2)
        elif tipo == "nombre":
            buscNombre.active = True
            buscId.active = False
            ventana.ids.busquedas.add_widget(ventana.ids.buscNombre,2)