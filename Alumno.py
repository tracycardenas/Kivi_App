class Alumno:
    __slots__ = (
        '_id',
        '_nombre',
        '_fechaNacimiento',
        '_materia'
    )

    def __init__(self, id=None, nombre="", fechaNacimiento="", materia=None):
        """
        inicializa los atributos de Alumno
        :materia: debe ser un objeto de tipo materia
        """
        self.id = id
        self.nombre = nombre
        self.fechaNacimiento = fechaNacimiento
        self.materia = materia

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def fechaNacimiento(self):
        return self._fechaNacimiento

    @fechaNacimiento.setter
    def fechaNacimiento(self, fechaNacimiento):
        self._fechaNacimiento = fechaNacimiento


    @property
    def materia(self):
        return self._materia

    @materia.setter
    def materia(self, materia):
        """
        :parametro materia: espera un objeto de tipo materia
        """
        self._materia = materia
