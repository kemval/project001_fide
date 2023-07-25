usuarios = {}
habitaciones_creadas = {}
casas_creadas = {}
autenticado = False
usuario_autenticado = None

# #___________________________________________ FUNCIONES_________________________________________________________________


def registrar(nombre, correo, pin):
    while True:
        if nombre in usuarios:
            return 'El usuario ya existe\n'
        usuarios[nombre] = {'nombre': nombre, 'correo': correo, 'pin': pin}
        return 'Usuario registrado correctamente\n'
        

def ingresar(nombre, pin):
    global autenticado, usuario_autenticado  
    if nombre in usuarios and usuarios[nombre]['pin'] == pin:
        current_user = usuarios[nombre]
        print(f'Bienvenido, {current_user["nombre"]}!\n')
        autenticado = True
        usuariod_autenticado = nombre 
        return True
    else:
        print('Usuario y/o contraseña inválidos\n')
        return False
    

def mostrar_registro():
    if usuarios:
        print('Usuarios registrados:\n')
        for nombre in usuarios.values():
            print(f"nombre: {nombre['nombre']}\n")
        print("")


def manejar_opciones_registro(opcion):
    global autenticado  
    if opcion == "1":
        nombre = input("Ingrese su nombre: ").title()
        correo = input("Ingrese su correo electrónico: ")
        pin = input("Ingrese su PIN: ")
        print(registrar(nombre, correo, pin))
        
    elif opcion == "2":
        nombre = input("Digite su nombre: ").title()
        pin = input("Digite su PIN: ")
        if ingresar(nombre, pin):
            print("Inicio de sesión exitoso.\n")
            autenticado = True
        else:
            print("Inicio de sesión fallido.\n")

    elif opcion == "3":
        print("Saliendo...\n")
        exit()
    else:
        print("Opcion invalida\n")

def menu_autenticado():
    print("Menú Autenticado:\n")
    print("1. Registro de nueva casa y habitacion")
    print("2. Registro de cerraduras")
    print("3. Actualizar PIN")
    print("4. Cerrar sesión\n")

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
                            elif opcion == "2":
                                break
                            else:
                                print("Opción inválida. Volviendo al menú principal.\n")
                        break        
                elif opcion == "2":
                    break
                else:
                    print("Opción inválida. Volviendo al menú principal.\n")


#____________________________________________________General__________________________________________________________________


def registro_cerraduras(casa, habitacion):

    nombre_cerradura = input(f"\nIngrese el nombre de la cerradura para la habitación '{habitacion}': ").title()
    while True:
        estado = input(f"\nIngrese el estado de la cerradura (abierto/cerrado) para la habitación '{habitacion}': ").title()

        if estado not in ["Abierto", "Cerrado"]:
            print('Por favor digite una opcion valida (abierto/cerrado)')
        else:
            break

    codigo_apertura = input(f"\nIngrese el código de apertura de la cerradura para la habitación '{habitacion}': ")
    detalles_cerradura = {'nombre': nombre_cerradura, 'estado': estado, 'codigo_apertura': codigo_apertura}
    casas_creadas[casa]['habitaciones'][habitacion]['locks'].append(detalles_cerradura)
    print(f"\nCerradura registrada correctamente para la habitación '{habitacion}'.\n")


def cambiarPin(pinActual, pinNuevo):
    global usuarios, usuario_autenticado
    if usuario_autenticado is not None: 
        if pinActual == usuarios[usuario_autenticado]['pin']:
            usuarios[usuario_autenticado]['pin'] = pinNuevo
            print("\nSu pin ha sido cambiado correctamente.")
        else:
            print("\nNo se pudo cambiar su pin. Pin actual incorrecto.")
   
        
##_________________________________________________________________________________________________________________________________              

while True:
    if not autenticado:  
        print("\nMenu Principal:\n")
        print("1. Registro")
        print("2. Ingresar")
        print("3. Salir\n")
    
        mostrar_registro()
        opcion = input("Elija una opción: ")
        manejar_opciones_registro(opcion)

    else:  
        print("\nMenú Autenticado:\n")
        print("1. Registro de nueva casa y habitacion")
        print("2. Actualizar PIN")
        print("3. Cerrar sesión\n")

        autenticado_opcion = input("Elija una opción: ")
        if autenticado_opcion == "1":
            registrar_casa_habitacion()


        elif autenticado_opcion == "2":
            pinActual = input("Ingrese su Contraseña Actual: ")
            pinNuevo = input("Ingrese su Nueva Contraseña:")
            cambiarPin(pinActual, pinNuevo)

        elif autenticado_opcion == "3":
            print("Cerrando sesión...")
            usuario_autenticado = None  
        else:
            print("Opcion invalida")        


