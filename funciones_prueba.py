import json      #Se importa la biblioteca Json para trabajar con los archivos posteriormente

#Variables Globales

usuarios = {}
habitaciones_creadas = {}
casas_creadas = {}
usuario_autenticado = None
autenticado = False

#Funcion de cargar los datos donde se van a guardar

def cargar_datos_json():

    global usuarios, habitaciones_creadas, casas_creadas

    try:
        with open('usuarios.json', 'r') as usuarios_file:
            usuarios = json.load(usuarios_file)

    except FileNotFoundError:
        usuarios = {}

    try:
        with open('habitaciones.json', 'r') as habitaciones_file:
            habitaciones_creadas = json.load(habitaciones_file)

    except FileNotFoundError:
        habitaciones_creadas = {}

    try:
        with open('casas.json', 'r') as casas_file:
            casas_creadas = json.load(casas_file)

    except FileNotFoundError:
        casas_creadas = {}

#funcion para guardar los datos

def guardar_datos_json():

    with open('usuarios.json', 'w') as usuarios_file:
        json.dump(usuarios, usuarios_file)

    with open('habitaciones.json', 'w') as habitaciones_file:
        json.dump(habitaciones_creadas, habitaciones_file)

    with open('casas.json', 'w') as casas_file:
        json.dump(casas_creadas, casas_file)

#Funcion de la verificacion del usuario

def registrar(nombre, correo, pin):

    while True:
        if nombre in usuarios:
            return 'El usuario ya existe\n'
        usuarios[nombre] = {'nombre': nombre, 'correo': correo, 'pin': pin}
        return 'Usuario registrado correctamente\n'
        
#Funcion que nos permite ingresar

def ingresar(nombre, pin):

    global autenticado, usuario_autenticado  

    if nombre in usuarios and usuarios[nombre]['pin'] == pin:
        current_user = usuarios[nombre]

        print(f'Bienvenido, {current_user["nombre"]}!\n')

        autenticado = True
        usuario_autenticado = nombre 

        return True
    else:

        print('Usuario y/o contraseña inválidos\n')
        return False
    
#Mostrar el registro de usuarios

def mostrar_registro():

    if usuarios:

        print('Usuarios registrados:\n')

        for nombre in usuarios.values():
            print(f"nombre: {nombre['nombre']}\n")
        print("")

#Funcion que nos permite registrarnos

def manejar_opciones_registro(opcion):
    global autenticado  
    if opcion == "1":
        nombre = input("\nIngrese su nombre: ").title()
        correo = input("\nIngrese su correo electrónico: ")
        pin = input("\nIngrese su PIN: ")
        print(registrar(nombre, correo, pin))
        
    elif opcion == "2":
        nombre = input("\nDigite su nombre: ").title()
        pin = input("\nDigite su PIN: ")
        if ingresar(nombre, pin):
            print("\nInicio de sesión exitoso.\n")
            autenticado = True
        else:
            print("\nInicio de sesión fallido.\n")

    elif opcion == "3":
        print("\nSaliendo...\n")
        exit()
    else:
        print("\nOpcion invalida\n")

#Funcion para utilizar el menu de inicio de session

def menu_autenticado():
    print("Menú Autenticado:\n")
    print("1. Registro de nueva casa y habitacion")
    print("2. Registro de cerraduras")
    print("3. Actualizar PIN")
    print("4. Cerrar sesión\n")

#Funcion para utilizar el menu principal

def manejar_menu_autenticado(opcion):
    if opcion == "1":
        print("Registro de nueva casa y habitacion")
    elif opcion == "2":
        print("Registro de cerraduras")
    elif opcion == "3":
        print("Actualizar PIN")
    elif opcion == "4":
        print("Cerrando sesión...")
        return False
    else:
        print("Opcion invalida")
    return True

#Funcion para registrar una casa

def registrar_casa_habitacion():
    while True: 
        casa = input("Ingrese el nombre de la casa o 'E' para salir: ").title()

        if casa == "E":
            break

        elif casa in casas_creadas:
            print("\nEsta casa ya existe, por favor ingrese un nombre diferente.\n")
        else:
            casas_creadas[casa] = {'habitaciones': {}}  # Create nested dictionary for rooms
            print("\nCasa registrada correctamente.\n") 

            while True:

                print("Desea agregar habitaciones a esta casa?\n")
                print("1. Si")
                print("2. No\n")

                opcion = input("\nElija una opción: ")

                if opcion == "1":
                    while True:
                        habitacion = input("\nIngrese el nombre de la habitación o 'E' para salir: \n").title()

                        if habitacion == "E":
                            break
                        elif habitacion in casas_creadas[casa]['habitaciones']:
                            print("\nEste cuarto ya existe, por favor ingrese uno diferente.\n")
                
                        else:
                            casas_creadas[casa]['habitaciones'][habitacion] = {'locks': []}  # Create locks list for room
                            print(f"Habitación '{habitacion}' registrada correctamente.\n")
                            print("Desea agregar cerraduras a esta habitación?\n")
                            print("1. Si")
                            print("2. No\n")

                            opcion = input("Elija una opción: ")

                            if opcion == "1":
                                registro_cerraduras(casa, habitacion)
                            else:
                                print("No se aregara ninguna cerradura.\n")
                            print('Desea agregar dispositivos a la habitacion?\n')
                            print("1. Si")
                            print("2. No\n")
                            DispositivoNuevo = input('Elija una opcion: ')

                            if DispositivoNuevo == "1":
                                AgregarDispositivo(casa, habitacion)
                            elif DispositivoNuevo == "2":
                                break
                            else:
                                print("Opción inválida. Volviendo al menú principal.\n")

                        break        
                elif opcion == "2":
                    break
                else:
                    print("Opción inválida. Volviendo al menú principal.\n")

#Funcion para agregar los dispositivos

def AgregarDispositivo(casa, habitacion):

    NombreDispositivo = input("Ingrese el nombre del dispositivo: ")

    Estado = input("Ingrese el estado inicial del dispositivo (encendido/apagado): ")

    if(Estado.lower() == "encendido"): 

        Estado = "Encendido"
    else: 
        Estado = "Apagado"

    Programacion = input("Ingrese la programacion del dispositivo (si/no): ")

    if(Programacion.lower() == "si"):

        Programacion = input("Ingrese la programacion del dispositivo: ")
    else:
        Programacion = "No tienen programacion"

    DetallesDispositivo = {'nombre': NombreDispositivo, 'estado': Estado, 'Programacion': Programacion}
    casas_creadas[casa]['habitaciones'][habitacion]['locks'].append(DetallesDispositivo)
    print(DetallesDispositivo)


#Funcion para agregar las cerraduras

def registro_cerraduras(casa, habitacion):

    nombre_cerradura = input(f"\nIngrese el nombre de la cerradura para la habitación '{habitacion}': ").title()

    while True:

        estado = input(f"\nIngrese el estado de la cerradura (abierto/cerrado) para la habitación '{habitacion}': ").title()

        if estado not in ["Abierto", "Cerrado"]:
            print('Por favor digite una opcion valida (abierto/cerrado)')
        else:
            break

    while True:

        codigo_apertura = input(f"\nIngrese el código numeral de apertura de la cerradura para la habitación '{habitacion}': ")
        
        if codigo_apertura.isdigit():
            codigo_apertura = int(codigo_apertura)
            break
        else:
            print("\nPor favor, ingrese un número válido para el código de apertura.\n")        

    detalles_cerradura = {'nombre': nombre_cerradura, 'estado': estado, 'codigo_apertura': codigo_apertura}

    casas_creadas[casa]['habitaciones'][habitacion]['locks'].append(detalles_cerradura)

    print(f"\nCerradura registrada correctamente para la habitación '{habitacion}'.\n")


#Funcion para cambiar el pin

def cambiarPin(pinActual, pinNuevo):

    global usuarios, usuario_autenticado

    #Primero verifica que el usuario este en el sistema

    if usuario_autenticado is not None: 

        #Luego perimete cambia el pin

        if pinActual == usuarios[usuario_autenticado]['pin']:
            usuarios[usuario_autenticado]['pin'] = pinNuevo
            print("\nSu pin ha sido cambiado correctamente.")

        else:
            print("\nNo se pudo cambiar su pin. Pin actual incorrecto.")
   
        
            
