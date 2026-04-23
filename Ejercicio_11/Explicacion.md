Este proyecto consiste en una aplicación web hecha con Flask que permite usar la cámara del dispositivo para escanear códigos QR y códigos de barras en tiempo real.

Dependiendo del tipo de código:

* 🔳 Si es un QR → muestra un enlace para acceder
* 📦 Si es un código de barras → busca el producto usando una API

---

## ⚙️ Tecnologías utilizadas

* Python (Flask)
* HTML / CSS
* JavaScript
* Librerías:

  * html5-qrcode (QR)
  * ZXing (códigos de barras)
* API:

  * Open Food Facts

---

## Estructura del proyecto

```
/proyecto
 ├── app.py
 └── /templates
      └── index.html
```

---

## 🐍 Explicación de `app.py`

Este archivo es el encargado de crear el servidor web con Flask.

```python
from flask import Flask, render_template
```

Importo Flask para crear la app y `render_template` para mostrar HTML.

```python
app = Flask(__name__)
```

Inicializo la aplicación.

```python
@app.route('/')
def index():
    return render_template('index.html')
```

Defino la ruta principal (`/`), que carga el archivo `index.html`.

```python
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
```

Ejecuto el servidor:

* `host="0.0.0.0"` permite acceso desde otros dispositivos
* `port=5000` define el puerto
* `debug=True` ayuda a detectar errores

---

## 🌐 Explicación de `index.html`

### 📱 Adaptación a móviles

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

Permite que la página se vea bien en celulares.

---

### 🎨 Interfaz

La página contiene:

* Un título
* Dos botones:

  * Escanear QR
  * Escanear códigos de barras
* Un contenedor para la cámara
* Un área para mostrar resultados

```html
<div id="scanner"></div>
<div id="resultado"></div>
```

---

### 🔳 Botón QR

```html
<button onclick="iniciarQR()">QR</button>
```

Activa la función `iniciarQR()`.

---

### 📦 Botón Códigos de Barras

```html
<button onclick="iniciarBarras()">Barras</button>
```

Activa la función `iniciarBarras()`.

---

## 🧠 Lógica en JavaScript

---

### 🛑 Función `detener()`

```javascript
function detener()
```

Sirve para:

* Apagar la cámara
* Detener el escaneo
* Limpiar el contenedor

---

### 🔳 Función `iniciarQR()`

```javascript
function iniciarQR()
```

* Activa el lector de QR
* Usa la cámara trasera (`facingMode: "environment"`)
* Cuando detecta un código:

  * Detiene el escáner
  * Muestra el enlace

```javascript
document.getElementById("resultado").innerHTML =
    `<a href="${text}" target="_blank">${text}</a>`;
```

---

### 📦 Función `iniciarBarras()`

```javascript
function iniciarBarras()
```

* Activa la cámara manualmente
* Usa ZXing para leer códigos de barras
* Escanea continuamente

```javascript
codeReader.decodeFromVideoElementContinuously(video, (result) => {
```

Cuando detecta:

```javascript
buscarProducto(result.text);
```

---

### 🔍 Función `buscarProducto()`

```javascript
async function buscarProducto(codigo)
```

* Envía el código a una API
* Busca información del producto

```javascript
fetch(`https://world.openfoodfacts.org/api/v0/product/${codigo}.json`)
```

---

### 📊 Resultado

Si encuentra el producto:

```javascript
<h3>Nombre del producto</h3>
<p>Marca</p>
```

Si no:

```javascript
Muestra solo el código
```

---

## 🚀 Cómo ejecutar el proyecto

1. Instalar Flask:

```bash
pip install flask
```

2. Ejecutar el servidor:

```bash
python app.py
```

3. Abrir en el navegador:

```
http://localhost:5000
```

---

## 📱 Uso en celular

Para usar la cámara en el celular se recomienda usar HTTPS.

Se puede usar ngrok:

```bash
ngrok http 5000
```

Y abrir el enlace generado en el celular.

---

## 🧠 Resumen

Este proyecto usa Flask para crear una página web que accede a la cámara del dispositivo y permite escanear códigos en tiempo real.

* QR → abre enlaces
* Barras → identifica productos

Todo se procesa directamente desde el navegador usando JavaScript.

