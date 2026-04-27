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
        return render_template("login.html", mensaje="Clave incorrecta")

# DASHBOARD
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

# OPCIONES
@app.route("/opcion1")
def opcion1():
    return render_template("opcion1.html")

@app.route("/opcion2")
def opcion2():
    return render_template("opcion2.html")

@app.route("/opcion3")
def opcion3():
    return render_template("opcion3.html")

@app.route("/opcion4")
def opcion4():
    return render_template("opcion4.html")

@app.route("/opcion5")
def opcion5():
    return render_template("opcion5.html")

if __name__ == "__main__":
    app.run(debug=True)