from flask import Flask, render_template, request
import modelo

app = Flask(__name__)

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
	modelo.cadastrar_usuario(nome, email, senha)
	todos = modelo.Usuario.select()
	for i in todos:
		print(i)

@app.route("/sobre")
def sobre():
	return render_template("sobre.html")

@app.route("/categorias")
def categorias():
	return render_template("categorias.html")

app.run(debug=True, host="0.0.0.0")