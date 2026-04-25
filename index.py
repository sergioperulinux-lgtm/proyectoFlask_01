from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# LOGIN
@app.route("/")
def inicio():
    return render_template("login.html", mensaje="")

@app.route("/login", methods=["POST"])
def login():
    usuario = request.form.get("usuario")
    clave = request.form.get("clave")

    if usuario == "admin" and clave == "1234":
        return redirect(url_for("dashboard"))
    else:
        return render_template("login.html", mensaje="Usuario o contraseña incorrectos")

# DASHBOARD
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

# CATEGORÍAS
@app.route("/categorias")
def categorias():
    return render_template("categorias.html")

# CURSOS
@app.route("/cursos")
def cursos():
    return render_template("cursos.html")

# PÁGINAS
@app.route("/paginas")
def paginas():
    return render_template("paginas.html")

# PERFIL
@app.route("/perfil")
def perfil():
    return render_template("perfil.html")

# EJECUCIÓN
if __name__ == "__main__":
    app.run(debug=True)