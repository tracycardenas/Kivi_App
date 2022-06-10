from kivy.uix.button import Button
from kivy.uix.label import Label
#from sqlalchemy import insert
from Materia import Materia
from MateriaDAO import MateriaDAO
from ProfesorDAO import ProfesorDAO


class ControladorMateria:

    def guardarActualizarMateria(self,id=None, nombre="", modalidad="", profesor=""):
       
        daoProfesor = ProfesorDAO()
        dao = MateriaDAO()
        if len(nombre) > 3:
            insertarActualizar = False
            profesorBase = daoProfesor.buscarProfesorPorNombre(profesor)
            materia = Materia(nombre=nombre, modalidad=modalidad,profesor=profesorBase)

            
            if id:
                materia.id = id
                insertarActualizar = dao.actualizarMateria(materia)
            else:
                insertarActualizar = dao.insertarMateria(materia)
            if insertarActualizar:
                return "Materia insertada o actualizada con Exito!!!"
            else:
                return "La materia no ha sido guardada o actualizada!"
        else:
            return "El nombre debe tener mas de 3 caracteres"

    def eliminarMateria(self,id):
        dao = MateriaDAO()
        eliminar = dao.eliminarMateria(str(id))
        if eliminar:
            return "Materia eliminada con exito!!!"
        else:
            return "La materia no ha sido eliminada!"

    def buscarMateria(self, id="", inicio=0, cantidad=10):
        dao = MateriaDAO()
        res=""
        if id != "":
            res = dao.buscarMateria(id)
        else:
            res = dao.buscarMaterias(inicio=inicio,cantidad=cantidad)
        items=[]
        if type(res) is Materia:
            listaMaterias = []
            listaMaterias.append(self._crearLabel(res.id, 0.2))
            listaMaterias.append(self._crearLabel(res.nombre, 0.6))
            listaMaterias.append(self._crearLabel(res.modalidad, 0.2))
            listaMaterias.append(self._crearBoton("Actualizar", res.id))
            listaMaterias.append(self._crearBoton("Eliminar", res.id))
            items.append(listaMaterias)

        if type(res) is list:
            for materia in res:
                listaMaterias = []
                listaMaterias.append(self._crearLabel(materia.id, 0.2))
                listaMaterias.append(self._crearLabel(materia.nome, 0.6))
                listaMaterias.append(self._crearLabel(materia.modalidad, 0.2))
                listaMaterias.append(self._crearBoton("Actualizar",materia.id))
                listaMaterias.append(self._crearBoton("Eliminar",materia.id))
                items.append(listaMaterias)
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

    def buscarProfesores(self):
        daoProfesor = ProfesorDAO()
        profesores = daoProfesor.buscarProfesores()
        return profesores