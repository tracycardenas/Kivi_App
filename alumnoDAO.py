from sympy import Line
from conexionBD import ConexionBD
from Alumno import Alumno
from MateriaDAO import MateriaDAO


class AlumnoDAO:
    __slots__ = (
    '_con'
    )
    def __init__(self):
        self._con = ConexionBD.conectar()

    def insertarAlumno(self, alumno):
        sql = 'INSERT INTO Alumno(nombre,fechaNacimiento,Materia_id) VALUES ("'+alumno.nombre+'","'+alumno.fechaNacimiento+'",'+str(alumno.materia.id)+')'
    

        res = ConexionBD.ejecutarSQL(sql)
        return res == 1

    def actualizarAlumno(self, alumno):

        sql = "UPDATE Alumno SET nombre='"+alumno.nombre+"', fechaNacimiento='"+alumno.fechaNacimiento+"', Materia_id="+str(alumno.materia.id)+"  WHERE id="+alumno.id
   
        res = ConexionBD.ejecutarSQL(sql)
        return res == 1

    def eliminarAlumno(self, idAluno):

        sql = "DELETE FROM Alumno WHERE id = " + str(idAluno)

        res = ConexionBD.ejecutarSQL(sql)
        return res == 1

    def buscarAlumnoId(self, id):

        try:
            
            res = ConexionBD.extraer("Alumno")
            for i in res:
                if(str(i[0]) == id):
                    al=i
            alumno = self.mostrarAlumnos(al)
            return alumno
        except Exception as e:
            print(str(e))
            return None

    def mostrarAlumnos(self, res):
        alumno = Alumno(id=res[0], nombre=res[1], fechaNacimiento=res[2])
        if res[3]:
            materia = MateriaDAO().buscarMateria(res[3])
            alumno.materia = materia
        return alumno

    def buscarAlumnos(self, cantidad=100, nombre=""):
        alumnos = []
        alun=[]
        try:
            
            res = ConexionBD.extraer("Alumno")
            if(nombre!=""):
                for i in res:
                    
                    if(i[1]==nombre):
                        
                        alun.append(i)
            else: 
                alun=res;    
            alumnos = self._mostrarResultado(alun)
            return alumnos
        except Exception as e:
            print(e)
            return alumnos

    def _mostrarResultado(self, res):
        alumnos = []
        
        for linea in res:
            alumno = self.mostrarAlumnos(linea)
            alumnos.append(alumno)
        return alumnos