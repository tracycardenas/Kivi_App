class Profesor:
    __slots__ = (
        '_id',
        '_nombre',
        '_especialidad'
    )

    def __init__(self, id=None, nombre="", especialidad=""):
        """
        inicializa los atributos de Profesor
        :materia: debe ser un objeto de tipo materia
        """
        self.id = id
        self.nombre = nombre
        self._especialidad =especialidad

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
    def especialidad(self):
        return self._especialidad

    @especialidad.setter
    def especialidad(self, especialidad):
        self._especialidad= especialidad
