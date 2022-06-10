from kivy.uix.label import Label
from kivy.uix.popup import Popup

from ControladorProfesor import ControladorProfesor

class ViewProfesor:

    def __init__(self, gerencVentana):
        self._gerencVentana = gerencVentana

    def registroActualProfesor(self):
        result = ""
        try:
            ventana = self._gerencVentana.get_screen("RegistroProfesor")
            idProfesor = ventana.ids.lblIdProfesor.text
            nombre = ventana.ids.inputNombre.text
            especialidad = ventana.ids.inputEspecialidad.text
            control = ControladorProfesor()
            if ventana.ids.btRegistroActual.text == "Eliminar":
                result = control.eliminarProfesor(idProfesor)
            else:
                result = control.guardarActualizarProfesor(id=idProfesor, nombre=nombre,
                especialidad=especialidad)

            self._popVentana(result)
            self._limpiarVentana(ventana)
        except Exception as e:
            print(e)
            self._popVentana(f" {ventana.ids.btRegistroActual.text} Profesor")


    def _limpiarVentanaListar(self,ventana):
        encabezado = [
        ventana.ids.colId,
        ventana.ids.colNombre,
        ventana.ids.colEspecialidad,
        ventana.ids.lblActual,
        ventana.ids.lblEliminar
        ]
        ventana.ids.listaProfesores.clear_widgets()
        for c in encabezado:
            ventana.ids.listaProfesores.add_widget(c)


    def buscaProfesores(self):
        control = ControladorProfesor()
        ventana = self._gerencVentana.get_screen("ListarProfesores")
        idBusq = ventana.ids.inputId.text
        resultado = control.buscarProfesor(id=idBusq)
        self._limpiarVentanaListar(ventana)
        for res in resultado:
            for r in res:
                if r.text == "Actualizar" or r.text == "Eliminar":
                    r.bind(on_release= self.mostrarVentanaAt)
                ventana.ids.listaProfesores.add_widget(r)

    def mostrarVentanaAt(self,boton):
        profesor=[]
        if boton.id:
            id = str(boton.id).replace("bt", "")
            control = ControladorProfesor()
            profesor = control.buscarProfesor(id=id)
        ventanaCad = self._gerencVentana.get_screen("RegistroProfesor")
        for t in profesor:
            ventanaCad.ids.lblIdProfesor.text = t[0].text
            ventanaCad.ids.inputNombre.text = t[1].text
            ventanaCad.ids.inputEspecialidad.text = t[2].text
        ventanaCad.ids.btRegistroActual.text = boton.text
        self._limpiarVentanaListar(self._gerencVentana.get_screen("ListarProfesores"))
        self._gerencVentana.ventanaRegistroProfesor()
    
    def mostrarVentanaAtRegistro(self,boton):
        profesor=[]
   
        ventanaCad = self._gerencVentana.get_screen("RegistroProfesor")
        for t in profesor:
            ventanaCad.ids.lblId.text = t[0].text
            ventanaCad.ids.inputNombre.text = t[1].text
            ventanaCad.ids.inputEspecialidad.text = t[2].text
        ventanaCad.ids.btRegistroActual.text = boton.text
        self._limpiarVentanaListar(self._gerencVentana.get_screen("ListarProfesores"))
        self._gerencVentana.ventanaRegistroProfesor()

    def _limpiarVentana(self, ventana):
        ventana.ids.lblId.text = ""
        ventana.ids.inputNombre.text = ""
        ventana.ids.inputEspecialidad.text=""
        ventana.ids.btRegistroActual.text = "Actualizar"

    def _popVentana(self, texto=""):
        popup = Popup(title='Informacion', content=Label(text=texto),
        auto_dismiss=True)

        popup.size_hint = (0.98, 0.4)
        popup.open()
