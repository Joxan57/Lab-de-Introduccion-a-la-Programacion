UsuarioCorrecto = "admin"
ContraseñaCorrecta = "Admin2026"

intentos = 0
acceso = 0
total_break = 0

def count_pass(contraseña):
    if len(contraseña) < 8:
        print("La contraseña debe contener al menos 8 caracteres")
        return False
    return True

def caracter_numerico(contraseña):
    for c in contraseña:
        if c.isdigit():
            return True
    print("La contraseña debe contener al menos un número")
    return False

def caracter_letra(contraseña):
    for c in contraseña:
        if c.isalpha():
            return True
    print("La contraseña debe contener al menos una letra")
    return False

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

#Aceptacion
    elif usuario == UsuarioCorrecto and ContraseñaCorrecta == contraseña:
        
        acceso = acceso + 1
        print("inicio de sesion exitoso")

        while acceso == 1:
    
            print("MUENUUU")
            print("1. Clasificar numero(positivo/negativo/cero+par/impar)")
            print("2. Categoria de edad y permisos(reglas de negocio)")
            print("3. Calcular tarifa final (Descuentos multiples)")
            print("4. Cerrar sesion (volver al login)")
            print("5. Salir")

            opcion = int(input("Dame el numero de opcion: "))
        # 1. Clasificacion Numero 
            if opcion == 1:
                
                print("Clasificacion de numero")
                x = int(input("Dame el numero a clasificar:"))
                
                if type(x) == int:
                    if x == 0:
                        print("Tu numero es cero")
                    elif x > 0:
                        print("Tu numero es positivo")
                    elif x < 0:
                        print("Tu numero es negativo")
                    if x % 2 == 0:
                        print("Numero par")
                    else:
                        print("Numero impar")
                else:
                    print("Caracter invalido")
        #2. Categoria de edad           
            elif opcion == 2:
                print("Categoria de edad y permisos(reglas de negocio")
                edad = int(input("Dame tu edad: "))
                ident = str(input("Cuentas con identificacion? [y/n] "))
                licen = str(input("Cuentas con licencia? [y/n] ")) 

            #Clasificacion edad
                if edad >= 12:
                    print("Niñez")
                elif 12 < edad <18:
                    print("Adolecencia") 
                elif 17<edad<65:
                    print("Adultez")
                elif edad > 65:
                    print("Mayor")

                #Permisos
                 #Registro
                if edad >= 13: 
                    print("Puede registrarse")
                else:
                    print("No puede registrarse")
                 #Compra sin tutor
                if edad>=18:
                    print("Puedes comprar sin tutor")
                else:
                    print("Puedes comprar con tutor")
                 #Conducir
                if edad >= 18 and licen == "y":
                    print("Puedes conducir")
                else:
                    print("No puedes conducir")
                 #Servicio Vip
                if edad >= 21 and ident == "y":
                    print("Tiene acceso a Servicio VIP")
                else: 
                    print("Sin acceso a servicio VIP")
        #3. Calculadora tarifa final
            elif opcion == 3:

                print("calculadora tarifa final")
        #4. Cerrar Secion
            elif opcion == 4:
                print("sesion cerrada")
                acceso = 0
                intentos = 0
        #5. Salir 
            elif opcion == 5:
                print("saliendo")
                total_break = total_break + 1
                break
        # Opcion invalida
            else: 
                print("opcion invalida")
                continue
            
    if total_break == 1:
        break
    




