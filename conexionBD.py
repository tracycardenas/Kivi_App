from colorama import Cursor
import sqlalchemy
class ConexionBD:
    __engine= None
    __db_username = 'root' #Usuario externo que hemos creado
    __db_password = 'admin' #Contraseña del usuario externo
    __db_ip = '34.67.249.75' #IP externa de la instancia
    __db_name = 'escuelatest'
    @staticmethod
    def conectar():
        if ConexionBD.__engine == None:
            try:
                s = 'mysql+mysqlconnector://{0}:{1}@{2}/{3}'.format(
                    ConexionBD.__db_username, ConexionBD.__db_password, ConexionBD.__db_ip, ConexionBD.__db_name)
                ConexionBD.__engine = sqlalchemy.create_engine(s)
                return ConexionBD.__engine
            except Exception as error:
                return error
        return ConexionBD.__engine

    @staticmethod
    def ejecutarSQL(sql):
        db_username = 'root' #Usuario externo que hemos creado
        db_password = 'admin' #Contraseña del usuario externo
        db_ip = '34.67.249.75' #IP externa de la instancia
        db_name = 'escuelatest'
        s = 'mysql+mysqlconnector://{0}:{1}@{2}/{3}'.format(db_username, db_password, db_ip, db_name)
        engine = sqlalchemy.create_engine(s)
        return engine.execute(sql)

    @staticmethod 
    def extraer(nombre):
        db_username = 'root' #Usuario externo que hemos creado
        db_password = 'admin' #Contraseña del usuario externo
        db_ip = '34.67.249.75' #IP externa de la instancia
        db_name = 'escuelatest'
        s = 'mysql+mysqlconnector://{0}:{1}@{2}/{3}'.format(db_username, db_password, db_ip, db_name)
        engine = sqlalchemy.create_engine(s)
        return engine.execute('SELECT * FROM '+nombre).fetchall()
