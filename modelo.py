import os
from peewee import *

arq = "usuario.db"
db = SqliteDatabase(arq)

class BaseModel(Model):
	class Meta():
		database = db

class Usuario(BaseModel):
	nome = CharField(primary_key=True)
	email = CharField()
	senha = CharField()

# def cadastrar_usuario(nome, email, senha):
# 	usuario = Usuario.create(nome=nome, email=email, senha=senha)
# 	usuario.save()
	
# if __name__ == "__main__":
# 	if os.path.exists(arq):
# 		os.remove(arq)

# 	try:
# 		db.connect()
# 		db.create_tables([Usuario])

# 	except OperationalError as erro:
# 			print("erro")