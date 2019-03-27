from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("pagina_inicial.html")

@app.route("/cadastro")
def cadastrar():
	return render_template("cadastro.html")

app.run(debug=True, host="0.0.0.0")