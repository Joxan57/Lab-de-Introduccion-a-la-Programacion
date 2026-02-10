# Crear un entorno virtual en Python (paso a paso)

Un **entorno virtual** en Python sirve para aislar librerías y versiones de cada proyecto, evitando conflictos entre dependencias.

---

## 1. Verificar que Python esté instalado

Abre la terminal o consola y escribe:

```bash
python --version
o

bash
Copiar código
python3 --version
Si aparece una versión (por ejemplo Python 3.12.1), todo bien.

2. Ubicarse en la carpeta del proyecto
Muévete a la carpeta donde estará tu proyecto:

bash
Copiar código
cd ruta/del/proyecto
Ejemplo en Windows:

bash
Copiar código
cd Documents\mi_proyecto
Ejemplo en macOS / Linux:

bash
Copiar código
cd ~/mi_proyecto
3. Crear el entorno virtual
Ejecuta el siguiente comando:

bash
Copiar código
python -m venv venv
📌 venv es el nombre del entorno (puedes cambiarlo si quieres).

Al hacerlo, se creará una carpeta llamada venv.

4. Activar el entorno virtual
En Windows (CMD o PowerShell)
bash
Copiar código
venv\Scripts\activate
En macOS o Linux
bash
Copiar código
source venv/bin/activate
Si se activó correctamente, verás algo así:

text
Copiar código
(venv)
al inicio de la línea de la terminal.

5. Instalar librerías dentro del entorno
Con el entorno activado, instala paquetes con pip:

bash
Copiar código
pip install nombre_paquete
Ejemplo:

bash
Copiar código
pip install numpy
Estas librerías solo se instalarán en este entorno.

6. Ver las librerías instaladas
bash
Copiar código
pip list
7. Guardar dependencias (opcional pero recomendado)
bash
Copiar código
pip freeze > requirements.txt
Esto crea un archivo con todas las dependencias del proyecto.

8. Desactivar el entorno virtual
Cuando termines de trabajar:

bash
Copiar código
deactivate
Resumen rápido
Crear entorno:

bash
Copiar código
python -m venv venv
Activar entorno:

Windows:

bash
Copiar código
venv\Scripts\activate
macOS / Linux:

bash
Copiar código
source venv/bin/activate
Instalar paquetes:

bash
Copiar código
pip install paquete
Salir del entorno:

bash
Copiar código

