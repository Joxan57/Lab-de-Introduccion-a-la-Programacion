Verificar que Python esté instalado

Abre VS Code → abre una terminal (Ctrl + ñ o Ctrl + `) y escribe:

```python
python --version
```


o si no funciona:

```python
py --version
```


👉 Si te sale algo como Python 3.x.x, todo bien.
👉 Si no, instala Python desde python.org y marca la casilla “Add Python to PATH”.

2️⃣ Abrir tu proyecto en VS Code

Crea una carpeta para tu proyecto
Ejemplo: mi_proyecto_python

Ábrela en VS Code:

Archivo → Abrir carpeta → selecciona tu carpeta

📁 Tu estructura inicial será algo así:

mi_proyecto_python/

3️⃣ Crear el entorno virtual (venv)

En la terminal de VS Code, dentro de la carpeta del proyecto, escribe:

En Windows:
```python
python -m venv venv
```

o:

```python
py -m venv venv
```

📌 venv es el nombre del entorno (puedes llamarlo como quieras, pero venv es el estándar).

Ahora tu carpeta se verá así:

mi_proyecto_python/
│── venv/

4️⃣ Activar el entorno virtual
🔹 Windows (PowerShell o CMD):
```python
venv\Scripts\activate
```

Si todo salió bien, verás algo así:

(venv) C:\ruta\mi_proyecto_python>


👉 Ese (venv) significa que el entorno virtual está activo ✅

🔹 Mac / Linux:
```python
source venv/bin/activate
```
5️⃣ Seleccionar el entorno virtual en VS Code (MUY IMPORTANTE)

Presiona:

Ctrl + Shift + P


Escribe:

Python: Select Interpreter


Elige el que diga algo como:

Python 3.x (venv)


🧠 Esto hace que VS Code use ese Python, no el del sistema.

6️⃣ Crear tu archivo Python

Crea un archivo, por ejemplo:

main.py


Prueba con algo simple:

print("Hola desde mi entorno virtual")


Ejecuta:

```python
python main.py
```

7️⃣ Instalar librerías en el entorno virtual

⚠️ Asegúrate de que el entorno esté activado (que veas (venv)).

Ejemplo: instalar requests
```python
pip install requests
```

Instalar varias librerías:

```python
pip install numpy pandas matplotlib
```

Ver librerías instaladas:

```python
pip list
```
8️⃣ Guardar las librerías del proyecto (requirements.txt)

Esto es CLAVE si luego quieres pasar tu proyecto a otra PC.

pip freeze > requirements.txt


Se crea un archivo:

requirements.txt


Con contenido tipo:

requests==2.31.0
numpy==1.26.4

9️⃣ Instalar librerías desde requirements.txt

En otro equipo o proyecto:

```python
pip install -r requirements.txt
```
10️⃣ Desactivar el entorno virtual (cuando quieras)
```python
deactivate
```
🔥 RESUMEN RÁPIDO
# Crear entorno
```python
python -m venv venv
```
# Activar (Windows)
```python
venv\Scripts\activate
```
# Instalar librerías
```python
pip install nombre_libreria
```
# Guardar dependencias
```python
pip freeze > requirements.txt
```
# Salir del entorno
deactivate
