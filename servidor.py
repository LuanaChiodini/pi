from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/cadastro")
def cadastrar():
	return render_template("cadastro.html")

@app.route("/sobre")
def sobre():
	return render_template("sobre.html")

@app.route("/categorias")
def categorias():
	return render_template("categorias.html")

app.run(debug=True, host="0.0.0.0")