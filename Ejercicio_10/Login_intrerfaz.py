from flask import Flask, render_template_string, request, redirect, session

app = Flask(__name__)
app.secret_key = "clave_secreta"

USUARIO = "admin"
PASSWORD = "Admin2026"

base_html = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>App Pro</title>

    <!-- Bootstrap -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">

    <style>
        body {
            background: linear-gradient(135deg, #1e1e2f, #2a2a40);
            color: white;
            min-height: 100vh;
        }

        .card-custom {
            background: #2c2c3c;
            border: none;
            border-radius: 15px;
            transition: all 0.3s;
            cursor: pointer;
        }

        .card-custom:hover {
            transform: translateY(-10px) scale(1.03);
            box-shadow: 0 10px 25px rgba(0,0,0,0.6);
        }

        .logout-btn {
            position: fixed;
            top: 20px;
            right: 20px;
        }

        .form-box {
            max-width: 400px;
            margin: auto;
            margin-top: 100px;
            background: #2c2c3c;
            padding: 25px;
            border-radius: 15px;
        }
    </style>
</head>
<body>

{{contenido|safe}}

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""

@app.route('/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('usuario')
        password = request.form.get('password')

        if user == USUARIO and password == PASSWORD:
            session['login'] = True
            return redirect('/menu')

    return render_template_string(base_html, contenido="""
        <div class='form-box text-center'>
            <h2>🔐 Login</h2>
            <form method='post'>
                <input class='form-control my-2' name='usuario' placeholder='Usuario' required>
                <input class='form-control my-2' type='password' name='password' placeholder='Contraseña' required>
                <button class='btn btn-success w-100 mt-2'>Entrar</button>
            </form>
        </div>
    """)

@app.route('/menu')
def menu():
    if not session.get('login'):
        return redirect('/')

    return render_template_string(base_html, contenido="""
        <a href='/logout' class='btn btn-danger logout-btn'>Cerrar sesión</a>

        <div class='container text-center mt-5'>
            <h1 class='mb-4'>🚀 MENÚ PRINCIPAL</h1>

            <div class='row justify-content-center g-4'>
                <div class='col-md-3'>
                    <div class='card card-custom p-4' onclick="location.href='/clasificar'">
                        <h3>🔢</h3>
                        <h5>Clasificar número</h5>
                    </div>
                </div>

                <div class='col-md-3'>
                    <div class='card card-custom p-4' onclick="location.href='/edad'">
                        <h3>🎂</h3>
                        <h5>Categoría edad</h5>
                    </div>
                </div>

                <div class='col-md-3'>
                    <div class='card card-custom p-4' onclick="location.href='/calc'">
                        <h3>🧮</h3>
                        <h5>Calculadora</h5>
                    </div>
                </div>
            </div>
        </div>
    """)

@app.route('/clasificar', methods=['GET','POST'])
def clasificar():
    if not session.get('login'):
        return redirect('/')

    resultado = ""

    if request.method == 'POST':
        try:
            x = int(request.form.get('numero'))

            if x == 0:
                resultado += "Cero<br>"
            elif x > 0:
                resultado += "Positivo<br>"
            else:
                resultado += "Negativo<br>"

            resultado += "Par" if x % 2 == 0 else "Impar"

        except:
            resultado = "Error: número inválido"

    return render_template_string(base_html, contenido=f"""
        <div class='container text-center mt-5'>
            <h2>🔢 Clasificar número</h2>
            <form method='post'>
                <input class='form-control w-50 mx-auto my-3' name='numero' placeholder='Número'>
                <button class='btn btn-success'>Calcular</button>
            </form>
            <p class='mt-3'>{resultado}</p>
            <a href='/menu'>Volver</a>
        </div>
    """)

@app.route('/edad', methods=['GET','POST'])
def edad():
    if not session.get('login'):
        return redirect('/')

    resultado = ""

    if request.method == 'POST':
        try:
            edad = int(request.form.get('edad'))

            if edad < 12:
                resultado = "Niñez"
            elif edad < 18:
                resultado = "Adolescencia"
            elif edad < 65:
                resultado = "Adultez"
            else:
                resultado = "Mayor"

        except:
            resultado = "Edad inválida"

    return render_template_string(base_html, contenido=f"""
        <div class='container text-center mt-5'>
            <h2>🎂 Categoría edad</h2>
            <form method='post'>
                <input class='form-control w-50 mx-auto my-3' name='edad' placeholder='Edad'>
                <button class='btn btn-success'>Evaluar</button>
            </form>
            <p class='mt-3'>{resultado}</p>
            <a href='/menu'>Volver</a>
        </div>
    """)

@app.route('/calc', methods=['GET','POST'])
def calc():
    if not session.get('login'):
        return redirect('/')

    resultado = ""

    if request.method == 'POST':
        try:
            edad = int(request.form.get('edad'))
            precio = 200
            descuento = 0

            if edad <= 12:
                descuento += 50
            elif edad <= 17:
                descuento += 20
            elif edad > 65:
                descuento += 30

            total = precio - (precio * descuento / 100)
            resultado = f"Total: $ {total}"

        except:
            resultado = "Error en datos"

    return render_template_string(base_html, contenido=f"""
        <div class='container text-center mt-5'>
            <h2>🧮 Calculadora</h2>
            <form method='post'>
                <input class='form-control w-50 mx-auto my-3' name='edad' placeholder='Edad'>
                <button class='btn btn-success'>Calcular</button>
            </form>
            <p class='mt-3'>{resultado}</p>
            <a href='/menu'>Volver</a>
        </div>
    """)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
