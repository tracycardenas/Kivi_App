class Materia:
    __slots__ = (
    '_id',
    '_nombre',
    '_modalidad',
    '_profesor'
    )

    def __init__(self, id=None, nombre="", modalidad="", profesor=None):
        self.id = id
        self.nombre = nombre
        self.modalidad = modalidad
        self.profesor = profesor

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
    def modalidad(self):
        return self._modalidad

    @modalidad.setter
    def modalidad(self, modalidad):
        self._modalidad = modalidad

    @property
    def profesor(self):
        return self._profesor

    @profesor.setter
    def profesor(self, profesor):
        """
        :parametro profesor: espera un objeto de tipo profesor
        """
        self._profesor = profesor
