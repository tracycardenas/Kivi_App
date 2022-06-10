from conexionBD import ConexionBD
from Materia import Materia

class MateriaDAO:
    __slots__ = (
        '_con'
    )

    def __init__(self):
        self._con = ConexionBD.conectar()

    def insertarMateria(self, materia):
        """
        Agrega una materia en la base de datos
        :parametro materia: espera un objeto de tipo materia
        :return: True en el caso de que la materia se agregue y False en el caso contrario
        """
        sql = 'INSERT INTO Materia(nombre,modalidad,Profesor_id) VALUES ("'+materia.nombre+'","'+materia.modalidad+'",'+str(materia.profesor.id)+')'

        res = ConexionBD.ejecutarSQL(sql)
        return res == 1

    def actualizarMateria(self, materia):
        """
        Actualiza una materia en la base de datos
        :parametro materia: espera un objeto de tipo materia
        :return: True caso de que la materia sea actualizada y False caso contrario
        """
        sql = "UPDATE Materia SET nombre='"+materia.nombre+"', modalidad='"+materia.modalidad+"', Profesor_id="+str(materia.profesor.id)+"  WHERE id="+materia.id
   
        res = ConexionBD.ejecutarSQL(sql)
        return res == 1

    def eliminarMateria(self, id):
        """
        Elimina una materia de la base de datos
        :parametro id: Espera un id(string) de la materia que va a ser eliminada
        :return: True caso de que la materia sea eliminada y False caso contrario
        """
        sql = "DELETE FROM Materia WHERE id = " + str(id)
        res=ConexionBD.ejecutarSQL(sql)
        return res == 1

    def buscarMateria(self,id):
        """
        Busca una materia de la base de datos
        :parametro id: Espera un id de la materia a ser buscada
        :return: una materia que tenga el id dado
        """
        try:
            
            res = ConexionBD.extraer("Materia")
            for i in res:
                if(str(i[0])==str(id)):
                    mat=i;

            materia = Materia(mat[0], mat[1], mat[2],mat[3])
            return materia
        except Exception as e:
            print(str(e))
            return None

    def buscarMateriaPorNombre(self,nome):
        """
        Busca una materia en la bd por su nombre
        :parametro nombre: Espera un nombre de una materia a ser buscada
        :return: una materia de acuerdo con el nombre dado
        """
        try:
            res = ConexionBD.extraer("Materia")
            for i in res:
                if(i[1]==nome):
                    mat=i;
            materia = Materia(mat[0], mat[1], mat[2],mat[3])
            return materia
        except Exception as e:
            print(str(e))
            return None

    def buscarMaterias(self, inicio=0, cantidad=100):
        """
        Busca materias en la base de datos
        :parametro cantidad: espera una cantidad de materias a ser buscadas
        :return: diversas materias de acuerdo con la cantidad dada
        """
        materias = []
        try:
            res = ConexionBD.extraer("Materia")
            materias = self._mostrarResultado(res)
            return materias
        except Exception as e:
            print(e)
            return materias

    def _mostrarResultado(self, res):
        materias = []
        for linea in res:
            materia = Materia(linea[0], linea[1], linea[2],linea[3])
            materias.append(materia)
        return materias
