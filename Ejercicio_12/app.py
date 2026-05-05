from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

productos_db = {
    "750105531234": {"nombre": "Leche Alpura 1L", "precio": 28.50},
    "750100012345": {"nombre": "Pan Bimbo Grande", "precio": 45.00},
    "750102220987": {"nombre": "Ariel 1kg", "precio": 62.90}
}

ticket = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/scan")
def scan():
    return render_template("scan.html")

@socketio.on("nuevo_codigo")
def handle_codigo(data):
    codigo = data["codigo"]

    if codigo in productos_db:
        producto = productos_db[codigo]
        ticket.append(producto)

        subtotal = sum(p["precio"] for p in ticket)
        iva = subtotal * 0.16
        total = subtotal + iva

        emit("actualizar", {
            "producto": producto,
            "subtotal": subtotal,
            "iva": iva,
            "total": total
        }, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
