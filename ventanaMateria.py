from kivy.uix.label import Label
from kivy.uix.popup import Popup

from ControladorMateria import ControladorMateria

class ViewMateria:

    def __init__(self, gerencVentana):
        self._gerencVentana = gerencVentana

    def registroActualMateria(self):
        result = ""
        try:
            ventana = self._gerencVentana.get_screen("RegistroMateria")
            idMateria = ventana.ids.lblId.text
            nombre = ventana.ids.inputNombre.text
            modalidad = self._verModalidad(ventana)
            profesor = ventana.ids.spProfesor.text

            control = ControladorMateria()
            if ventana.ids.btRegistroActual.text == "Eliminar":
                result = control.eliminarMateria(idMateria)
            else:
                result = control.guardarActualizarMateria(id=idMateria, nombre=nombre,
                modalidad=modalidad, profesor = profesor)

            self._popVentana(result)
            self._limpiarVentana(ventana)
        except Exception as e:
            print(e)
            self._popVentana(f"---No fue posible {ventana.ids.btRegistroActual.text} Materia!!!")


    def _limpiarVentanaListar(self,ventana):
        encabezado = [
        ventana.ids.colId,
        ventana.ids.colNombre,
        ventana.ids.colModalidad,
        ventana.ids.colProfesor,
        ventana.ids.lblActual,
        ventana.ids.lblEliminar
        ]
        ventana.ids.listaMaterias.clear_widgets()
        for c in encabezado:
            ventana.ids.listaMaterias.add_widget(c)


    def buscaMaterias(self):
        control = ControladorMateria()
        ventana = self._gerencVentana.get_screen("ListarMaterias")
        idBusq = ventana.ids.inputId.text
        resultado = control.buscarMateria(id=idBusq)
        self._limpiarVentanaListar(ventana)
        for res in resultado:
            for r in res:
                if r.text == "Actualizar" or r.text == "Eliminar":
                    r.bind(on_release= self.mostrarVentanaAt)
                ventana.ids.listaMaterias.add_widget(r)

    def mostrarVentanaAt(self,boton):
        ventanaRegistro = self._gerencVentana.get_screen("RegistroMateria")
        ventanaRegistro.ids.spProfesor.values = self._mostrarSpinner()
        materia=[]
        if boton.id:
            id = str(boton.id).replace("bt", "")
            control = ControladorMateria()
            materia = control.buscarMateria(id=id)
        ventanaCad = self._gerencVentana.get_screen("RegistroMateria")
        for t in materia:
            ventanaCad.ids.lblId.text = t[0].text
            ventanaCad.ids.inputNombre.text = t[1].text
            if t[2] != "":
                self._marcarModalidad(t[2].text, ventanaCad)
            ventanaCad.ids.spProfesor.text = t[3].text

        ventanaCad.ids.btRegistroActual.text = boton.text
        self._limpiarVentanaListar(self._gerencVentana.get_screen("ListarMaterias"))
        self._gerencVentana.ventanaRegistroMateria()


    def mostrarVentanaAtRegistro(self,boton):
        materia=[]
        ventanaCad = self._gerencVentana.get_screen("RegistroMateria")
        ventanaCad.ids.spProfesor.values = self._mostrarSpinner()
        for t in materia:
            ventanaCad.ids.lblId.text = t[0].text
            ventanaCad.ids.inputNombre.text = t[1].text
            if t[2] != "":
                self._marcarModalidad(t[2].text, ventanaCad)
            ventanaCad.ids.spProfesor.text = t[3].text
        ventanaCad.ids.btRegistroActual.text = boton.text
        self._limpiarVentanaListar(self._gerencVentana.get_screen("ListarMaterias"))
        self._gerencVentana.ventanaRegistroMateria()

    def _mostrarSpinner(self):
        listaValores = self._buscarProfesorventana()
        return listaValores


    def _buscarProfesorventana(self):
        control = ControladorMateria()
        profesores = control.buscarProfesores()
        nombresProfesores =[]
        for profesor in profesores:
            nombresProfesores.append(profesor.nombre)
        return nombresProfesores

    def _limpiarVentana(self, ventana):
        ventana.ids.lblId.text = ""
        ventana.ids.inputNombre.text = ""
        ventana.ids.chkMatutino.active = False
        ventana.ids.chkVespertino.active = False
        ventana.ids.chkNocturno.active = False
        ventana.ids.spProfesor.text = "Seleccione..."
        ventana.ids.btRegistroActual.text = "Actualizar"

    def _popVentana(self, texto=""):
        popup = Popup(title='Informacion', content=Label(text=texto),
        auto_dismiss=True)

        popup.size_hint = (0.98, 0.4)
        popup.open()

    def _verModalidad(self, ventana):
        modalidad = ""
        if ventana.ids.chkMatutino.active:
            modalidad = ventana.ids.chkMatutino.value
        elif ventana.ids.chkVespertino.active:
            modalidad = ventana.ids.chkVespertino.value
        elif ventana.ids.chkNoturno.active:
            modalidad = ventana.ids.chkNoturno.value
        return modalidad

    def _marcarModalidad(self, texto, ventana):
        if ventana.ids.chkMatutino.value == texto:
            ventana.ids.chkMatutino.active = True
        elif ventana.ids.chkVespertino.value == texto:
            ventana.ids.chkVespertino.active = True
        elif ventana.ids.chkNoturno.value == texto:
            ventana.ids.chkNoturno.active = True