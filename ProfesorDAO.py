from conexionBD import ConexionBD
from Profesor import Profesor

class ProfesorDAO:
    __slots__ = (
    '_con'
    )
    def __init__(self):
        self._con = ConexionBD.conectar()

    def insertarProfesor(self, profesor):
        sql = 'INSERT INTO Profesor (nombre,especialidad) VALUES ("'+profesor.nombre+'","'+profesor.especialidad+'")'
        res = ConexionBD.ejecutarSQL(sql)
        return res == 1

    def actualizarProfesor(self, profesor):
        nombre=profesor.nombre
        especialidad=profesor.especialidad
        id=profesor.id
        sql = "UPDATE Profesor SET nombre='"+ nombre +"', especialidad= '"+especialidad+"' WHERE id="+id
        res = ConexionBD.ejecutarSQL(sql)
        return res == 1

    def eliminarProfesor(self, idProfesor):

        sql = "DELETE FROM Profesor WHERE id = " + str(idProfesor)
        res = ConexionBD.ejecutarSQL(sql)
        return res == 1

    def buscarProfesorId(self, id):

        try:
            
            res = ConexionBD.extraer("Profesor")
            for i in res:
                if(str(i[0])==id):
                    pro=i

            profesor = self.mostrarProfesores(pro)
            return profesor
        except Exception as e:
            print(str(e))
            return None

    def mostrarProfesores(self, res):
        profesor = Profesor(id=res[0], nombre=res[1], especialidad=res[2])
        return profesor

    def buscarProfesorPorNombre(self,nome):

        try:
            res = ConexionBD.extraer("Profesor")
            for i in res:
            
                if (i[1]==nome):
                    prof=i
                
            profesor = Profesor(prof[0], prof[1], prof[2])
            return profesor
        except Exception as e:
            print(str(e))
            return None

    def buscarProfesores(self, inicio=0, cantidad=100):
        profesores = []
        try:
            
            res = ConexionBD.extraer("Profesor")
            profesores = self._mostrarResultado(res)
            
            return profesores
        except Exception as e:
            print(e)
            return profesores    

    def _mostrarResultado(self, res):
        profesores = []
        for linea in res:
            profesor = Profesor(linea[0], linea[1], linea[2])
            profesores.append(profesor)
            
        return profesores