from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("pagina_inicial.html")

@app.route("/cadastro", methods=["GET", "POST"])
def cadastrar():
	if request.method == "POST":
		nome = request.form["nome"]
		email = request.form["email"]
		senha = request.form["senha"]
		pais = request.form["pais"]
	return render_template("cadastro.html")

app.run(debug=True, host="0.0.0.0")
