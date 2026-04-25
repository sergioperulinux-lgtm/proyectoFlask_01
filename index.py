from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("login.html", mensaje="")

@app.route("/login", methods=["POST"])
def login():
    usuario = request.form.get("usuario")
    clave = request.form.get("clave")

    if usuario == "admin" and clave == "1234":
        return redirect("/dashboard")   # 👈 simple, sin complicaciones
    else:
        return render_template("login.html", mensaje="Usuario o contraseña incorrectos")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)