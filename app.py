from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# memoria simple
tareas = []
mensajes = []

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

# 🧮 CALCULADORA
@app.route("/calculadora", methods=["GET", "POST"])
def calculadora():
    resultado = None
    if request.method == "POST":
        n1 = float(request.form.get("n1"))
        n2 = float(request.form.get("n2"))
        op = request.form.get("op")

        if op == "+":
            resultado = n1 + n2
        elif op == "-":
            resultado = n1 - n2
        elif op == "*":
            resultado = n1 * n2
        elif op == "/":
            resultado = n1 / n2

    return render_template("calculadora.html", resultado=resultado)

# 📅 TAREAS
@app.route("/tareas", methods=["GET", "POST"])
def tareas_view():
    if request.method == "POST":
        tarea = request.form.get("tarea")
        tareas.append(tarea)
    return render_template("tareas.html", tareas=tareas)

# 💬 CHAT
@app.route("/chat", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        msg = request.form.get("mensaje")
        mensajes.append(("Tú", msg))

        # respuesta automática simple
        respuesta = "No entiendo, pero estoy aprendiendo 😅"
        if "hola" in msg.lower():
            respuesta = "Hola! ¿Cómo estás?"
        elif "adios" in msg.lower():
            respuesta = "Hasta luego 👋"

        mensajes.append(("Bot", respuesta))

    return render_template("chat.html", mensajes=mensajes)

# 🤖 GENERADOR
@app.route("/generador", methods=["GET", "POST"])
def generador():
    texto = ""
    if request.method == "POST":
        tema = request.form.get("tema")
        texto = f"Este es un texto generado sobre: {tema}. Puedes ampliarlo luego."
    return render_template("generador.html", texto=texto)

# 📊 PANEL
@app.route("/panel")
def panel():
    return render_template("panel.html", total_tareas=len(tareas), total_msgs=len(mensajes))

if __name__ == "__main__":
    app.run(debug=True)