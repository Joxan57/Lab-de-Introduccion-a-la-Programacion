UsuarioCorrecto = "admin"
ContraseñaCorrecta = "Admin2026"

intentos = 0

def count_pass(contraseña):
    total_letras = len(contraseña)
    if total_letras <8:
        print("La contraseña debe contener almenos 8 caracteres")

def caracter_numerico(contraseña):
    if not contraseña.isdigit():
        print("La contraseña debe contener un valor numerico")

def caracter_letra(contraseña):
    if not contraseña.isalpha():
        print("La contraseña debe conntener letras")

while intentos < 3:
    
    usuario = input("Usuario:")
    contraseña = input("Contraseña:")

#Validacion de usuario vacio
    if usuario == "": 
       
        print("No se premite usuario vacio")
        intentos = intentos + 1

#Validacion de espacios
    elif " " in usuario:
        
        print("No se permiten espacios")
        intentos = intentos + 1

    elif (
    count_pass(contraseña) is None or
    caracter_numerico(contraseña) is None or
    caracter_letra(contraseña) is None
):
        intentos = intentos + 1

#Validacion de usuario y contrase incorrecta
    elif usuario != UsuarioCorrecto or ContraseñaCorrecta != contraseña:
        
        print("usuario o contraseña invalidos")
        intentos = intentos + 1
