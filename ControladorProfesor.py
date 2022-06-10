from kivy.uix.button import Button
from kivy.uix.label import Label
#from sqlalchemy import insert
from Profesor import Profesor
from ProfesorDAO import ProfesorDAO


class ControladorProfesor:

    def guardarActualizarProfesor(self,id=None, nombre="", especialidad=""):
        if len(nombre) > 3:
            insertarActualizar = False
            profesor = Profesor(nombre=nombre, especialidad=especialidad)
            dao = ProfesorDAO()
            if id:
                profesor.id = id
                insertarActualizar = dao.actualizarProfesor(profesor)
            else:
                insertarActualizar = dao.insertarProfesor(profesor)
            if insertarActualizar:
                return "Profesor insertado o actualizado con Exito!!!"
            else:
                return "La profesor ha sido guardado o actualizado!"
        else:
            return "El nombre debe tener mas de 3 caracteres"

    def eliminarProfesor(self,id):
        dao = ProfesorDAO()
        eliminar = dao.eliminarProfesor(str(id))
        if eliminar:
            return "Profesor eliminado con exito!!!"
        else:
            return "La Profesor no ha sido eliminado!"

    def buscarProfesor(self, id="", inicio=0, cantidad=10):
        dao = ProfesorDAO()
        res=""
        if id != "":
            res = dao.buscarProfesorId(id)
        else:
            res = dao.buscarProfesores(inicio=inicio,cantidad=cantidad)
        items=[]
        if type(res) is Profesor:
            listaProfesores = []
            listaProfesores.append(self._crearLabel(res.id, 0.2))
            listaProfesores.append(self._crearLabel(res.nombre, 0.6))
            listaProfesores.append(self._crearLabel(res.especialidad, 0.2))
            listaProfesores.append(self._crearBoton("Actualizar", res.id))
            listaProfesores.append(self._crearBoton("Eliminar", res.id))
            items.append(listaProfesores)

        if type(res) is list:
            for profesor in res:
                listaProfesores = []
                listaProfesores.append(self._crearLabel(profesor.id, 0.2))
                listaProfesores.append(self._crearLabel(profesor.nome, 0.6))
                listaProfesores.append(self._crearLabel(profesor.especialidad, 0.2))
                listaProfesores.append(self._crearBoton("Actualizar",profesor.id))
                listaProfesores.append(self._crearBoton("Eliminar",profesor.id))
                items.append(listaProfesores)
        return items

    def _crearLabel(self, texto, tam):
        label = Label()
        label.text = str(texto)
        label.size_hint_y = None
        label.size_hint_x = tam
        label.height = '30dp'
        return label

    def _crearBoton(self, texto, id):
        boton = Button()
        boton.text = texto
        boton.id = "bt"+str(id)
        boton.font_size = '10sp'
        boton.size_hint_y = None
        boton.height = '30dp'
        boton.size_hint_x = .1
        return boton