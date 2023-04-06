import re
import ast
import os 

try:
    ruta_actual=os.path.dirname(os.path.abspath(__file__))
    ruta=os.path.join(ruta_actual)
    F = open(ruta + "/Database.txt", "a")
    F.close
except:print("\nVerificar la ruta del txt") 

Usuario={}
user=0
passwd=0

#Funcion para Registrar
def singUp(user,passwd):
    try:    
        Dics={}
        verify={}
        validacion=0

        #F = open(ruta + "/Database.txt", "r")
        while True: #REGISTRO DE USUARIO-----EL FOR VERIFICA SI EL USUARIO YA EXISTE
            ok = 0
            ok2 = 0
            F = open(ruta + "/Database.txt", "r")
            user = input("Ingrese su Usuario: ")
            for line in F.readlines():
                verify = ast.literal_eval(line)
                validacion = verify.get(user, 0)
                ok+=1

                if validacion == 0:
                    ok2+=1

            if ok==ok2:
                print("Usuario Valido")

                break
            else:
                print("Usuario No Disponible")
            F.close()


        while True: #INGRESA LA CONTRASEÑA, VERIFICA QUE CUMPLA LOS PARAMETROS Y QUE COINCIDA LA SEGUNDA VEZ QUE INGRESAS
            print("La password debe tener al menos 1 mayuscula, 1 minuscula, 1 numero y 1 caracter especial")
            passwd = str(input("Ingrese password: "))
            if re.search("[A-Z]", passwd) and re.search("[a-z]", passwd) and re.search("[0-9]", passwd) and re.search(
                    "[^A-Za-z0-9]", passwd):
                print("Password Valida")
                while True:

                    passwdverify = str(input("Repita la password: "))
                    if passwdverify == passwd:
                        print("Password creada correctamente")
                        break
                    else:
                        print("Las contraseñas no coinciden")
                break
            else:
                print("La password debe tener al menos 1 mayuscula, 1 minuscula, 1 numero y 1 caracter especial")
        F = open(ruta + "/Database.txt", "a")
        Dics[user] = passwd
        F.write(str(Dics)) #GUARDA EN TXT EL USUARIO CREADO
        F.write("\n")
        F.close()
        return user,passwd
    except:print("Verificar ruta del txt")
#------------------------------------------------------------------------------------------------------------------

#Funcion para Hacer Login
def Login():
    try:    
        intentosUser=0
        while True:
            verify = {}
            validacion = 0
            ValidacionPass = 0
            intentos = 0
            count = 0
            count2 = 0
            if intentosUser == 3: #SI INGRESAS USUARIO 3 VECES MAL, SALE DEL SISTEMA
                print("Maximo de intentos")
                break
            user = input("Ingrese su Usuario: ")
            F = open(ruta + "/Database.txt", "r")
            for line in F.readlines():
                verify = ast.literal_eval(line)
                validacion = verify.get(user, 0)
                count += 1
                if validacion != 0:         #VERIFICA QUE EL USUARIO EXISTE EN LA BASE DE DATOS
                    print("USUARIO VALIDO")
                    while True:
                        ValidacionPass = input("Ingrese contraseña: ")
                        if ValidacionPass == validacion: #VERIFICA QUE LA CONTRASEÑA COINCIDE CON EL USUARIO
                            print("Contraseña Correcta")
                            print("Bienvenido al sistema")
                            break
                        else:
                            print("Contraseña Incorrecta")  #MAXIMO DE INTENTOS DE CONTRASEÑA
                            intentos += 1
                            if intentos == 3:
                                print("Maximo de intentos")
                                break

                else:
                    count2 += 1
            F.close()
            if count == count2:
                print("USUARIO INVALIDO")
                intentosUser+=1
                continue
            break
    except:
        print("No esta creada la base de datos, registrese y se creara automaticamente")        
#------------------------------------------------------------------------------------------------------------------

#Funcion para Mostrar txt
def mostrar():
    try:
        F = open(ruta + "/Database.txt", "r")
        print(F.read())
    except:
        print("NO EXISTE EL ARCHIVO")   
        print("Al Registrarse se crea automaticamente") 


# ------------------------------------------------------------------------------------------------------------------

#Menu de Opciones
"""while True:
    x=input("\n Menu de Opciones \n 1-Registrar \n 2-Login \n 3-VerDB \n 4-Salir \n :")
    if x== "1":
        try:
            user, passwd = singUp(user, passwd)
            Usuario[user] = passwd
            print(Usuario)
        except:print("Archivo txt no creado o ruta con errores")    
    elif x== "2":
        Login()
    elif x == "3":
        mostrar()
    elif x == "4":
        break
    else:
        print("ingrese valor valido")
"""

