import pandas as pd
import sqlalchemy

#!pip install mysql-connector #Eliminar comentario en caso de no tener instalada esta librería. No es necesario importarla


db_username = 'root' #Usuario externo que hemos creado
db_password = 'admin' #Contraseña del usuario externo
db_ip = '34.67.249.75' #IP externa de la instancia
db_name = 'escuelatest'

s = 'mysql+mysqlconnector://{0}:{1}@{2}/{3}'.format(db_username, db_password, db_ip, db_name)
engine = sqlalchemy.create_engine(s)
nombr="Luis David"
especialidad="Ingeniero"
id=2
sql = "UPDATE  SET nombre='Luis David', especialidad= 'Ingeniero' WHERE id=2"
print(sql)
engine.execute(sql)



