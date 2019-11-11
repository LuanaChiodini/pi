from flask import Flask, render_template, request, redirect, session
from modelo import db, Usuario
import peewee

app = Flask(__name__)
app.config["SECRET_KEY"] = "2222"

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/cadastro")
def cadastro():
	return render_template("cadastro.html")

@app.route("/cadastrar", methods=["POST"])
def cadastrar():
	nome = request.form["nome"]
	email = request.form["email"]
	senha = request.form["senha"]
	Usuario.create(nome=nome, email=email, senha=senha)
	todos = Usuario.select()
	# for i in todos:
	# 	print(i.nome)
	return redirect("/")

@app.route("/sobre")
def sobre():
	return render_template("sobre_nos.html")

@app.route("/categorias")
def categorias():
	return render_template("categorias.html")

@app.route("/form_login")
def form_login():
	return render_template("form_login.html")

@app.route("/login", methods=["POST"])
def login():
	login = request.form["login"]
	senha = request.form["senha"]
	todos = Usuario.select()
	for i in todos:
		if i.nome == login and i.senha == senha:
			session["usuario"] = login
			return redirect("/")
	else:
		return render_template("cadastro.html")

@app.route("/logout")
def logout():
	session.pop("usuario")
	return redirect("/")

if __name__ == "__main__":
	try:
		db.connect()
		db.create_tables([Usuario])

	except peewee.OperationalError as erro:
		print("ERROR: " + erro)

app.run(debug=True, host="0.0.0.0")