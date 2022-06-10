from kivy.uix.screenmanager import Screen, ScreenManager

from ventanaAlumno import ViewAlumno
from ventanaMateria import ViewMateria
from ventanaProfesor import ViewProfesor


class VentanaInicial(Screen):
    pass


class RegistroMateria(Screen):
    pass


class ListarMaterias(Screen):
    pass

class RegistroAlumno(Screen):
    pass


class ListarAlumnos(Screen):
    pass

class RegistroProfesor(Screen):
    pass

class ListarProfesores(Screen):
    pass


class AdministrarVentanas(ScreenManager):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._ventanaMateria = ViewMateria(self)
        self._ventanaAlumno = ViewAlumno(self)
        self._ventanaProfesor = ViewProfesor(self)

    def ventanaInicial(self):
        self.current = "VentanaInicial"

    def ventanaRegistroMateria(self):
        self.current = 'RegistroMateria'

    def ventanaListarMaterias(self):
        self.current = "ListarMaterias"

    def ventanaRegistroAlumno(self):
        self.current = "RegistroAlumno"

    def ventanaListarAlumnos(self):
        self._ventanaAlumno.alternarBusq("id")
        self.current = "ListarAlumnos"

    def ventanaRegistroProfesor(self):
        self.current = "RegistroProfesor"

    def ventanaListarProfesores(self):
        self.current = "ListarProfesores"


    def registrarActualizar(self):
        self._ventanaMateria.registroActualMateria()

    def registrarActualizarAlumno(self):
        self._ventanaAlumno.registroActualAlumno()

    def registrarActualizarProfesor(self):
        self._ventanaProfesor.registroActualProfesor()

    def buscarMaterias(self):
        self._ventanaMateria.buscaMaterias()

    def buscarAlumnos(self):
        self._ventanaAlumno.buscarAlumnos()

    def buscarProfesores(self):
        self._ventanaProfesor.buscaProfesores()

    def buscarAlumnosNombre(self, nombre):
        self._ventanaAlumno.buscarAlumnos(nombre)