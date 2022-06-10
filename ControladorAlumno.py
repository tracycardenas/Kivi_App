import locale

from kivy.uix.button import Button
from kivy.uix.label import Label
from util import Util
from alumnoDAO import AlumnoDAO
from Alumno import Alumno
from MateriaDAO import MateriaDAO


class ControladorAlumno:
    def guardadActualizarAlumno(self,id=None, nombre="",fechaNacimiento="",materia=""):
        daomateria = MateriaDAO()
        daoAlumno = AlumnoDAO()
        if len(nombre) > 3:
            insertarActualizar = False
            fechaNac = self._conversionFechaBD(fechaNacimiento)
            materiaBase = daomateria.buscarMateriaPorNombre(materia)
            alumno = Alumno(nombre=nombre, fechaNacimiento=fechaNac, materia=
            materiaBase)

            if id:
                alumno.id = id
                insertarActualizar= daoAlumno.actualizarAlumno(alumno)
            else:
                insertarActualizar = daoAlumno.insertarAlumno(alumno)
            if insertarActualizar:
                return "Alumno insertado o actualizado con exito!!!"
            else:
                return "El alumno no puede ser insertado o actualizado!"
        else:
            return "El nombre debe tener mas de 3 caracteres"

    def _conversionFechaBD(self, fechaNacimiento):
        """
        Converte un dato en formato "dd/mm/aaaa" para "aaaa-mm-dd"
        :return: la fecha de nacimiento en el formato aceptado por la bd
        """
        if Util.validaData(fechaNacimiento):
            d = fechaNacimiento.split("/") #convierte un string en lista
            fechaBD = d[2] + "-" + d[1] + "-" + d[0]
            return fechaBD 
        else:
            return ""


    def eliminarAlumno(self,id):
        dao = AlumnoDAO()
        eliminar = dao.eliminarAlumno(str(id))
        if eliminar:
            return "Alumno eliminado con exito!!!"
        else:
            return "El alumno no ha sido eliminado!"

    def buscarAlumno(self, id="",inicio=0, cantidad=10, nombreBuscar=""):
        dao = AlumnoDAO()

        res=""
        if id != "":
            res = dao.buscarAlumnoId(id=id)
        elif nombreBuscar != "":
            res = dao.buscarAlumnos(cantidad=cantidad, nombre=nombreBuscar)
        else:
            res = dao.buscarAlumnos(cantidad=cantidad)
        items=[]
        if type(res) is Alumno:
            listaAlumno = []
            listaAlumno.append(self._crearLabel(res.id, 0.1))
            listaAlumno.append(self._crearLabel(res.nombre, 0.5))
            fechaNac = self._fechaNacimientoBD(res.fechaNacimiento)
            listaAlumno.append(self._crearLabel(fechaNac, 0.1))
            materia = self._buscarmateriaAlumno(res.materia.id)
            listaAlumno.append(self._crearLabel(materia.nombre, 0.1))
            listaAlumno.append(self._crearBoton("Actualizar", res.id))
            listaAlumno.append(self._crearBoton("Eliminar", res.id))
            items.append(listaAlumno)

        if type(res) is list:
            for alumno in res:
                listaAlumno = []
                listaAlumno.append(self._crearLabel(alumno.id, 0.1))
                listaAlumno.append(self._crearLabel(alumno.nombre, 0.4))
                fechaNac = self._fechaNacimientoBD(alumno.fechaNacimiento)
                listaAlumno.append(self._crearLabel(fechaNac, 0.1))
                if alumno.materia:
                    materia= alumno.materia.nombre
                else:
                    materia= ""
                listaAlumno.append(self._crearLabel(materia,0.1))
                listaAlumno.append(self._crearBoton("Actualizar", alumno.id))
                listaAlumno.append(self._crearBoton("Eliminar", alumno.id))
                items.append(listaAlumno)
        return items

    def _buscarmateriaAlumno(self, idmateria):
        daomateria = MateriaDAO()
        return daomateria.buscarMateria(idmateria)

    def _fechaNacimientoBD(self, fecha):
        fechaBD=""
        if fecha is not None:
            fechaArray = str(fecha).split("-")
            fechaBD= fechaArray[2] + "/" + fechaArray[1] + "/" + fechaArray[0]

        return fechaBD


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

    def buscarMateriaPorNombre(self,nombreMateria):
        daoMateria = MateriaDAO()
        return daoMateria.buscarMateriaPorNombre(nombreMateria)

    def buscarMaterias(self):
        daoMateria = MateriaDAO()
        materias = daoMateria.buscarMaterias()
        return materias