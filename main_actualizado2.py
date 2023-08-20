import funciones

funciones.cargar_datos_json()

while True:

    if not funciones.autenticado:  
        #El Menu de inicio para verificar si estar registrado o no
        print("\nMenu Principal:\n")
        print("1. Registro")
        print("2. Ingresar")
        print("3. Salir\n")
    
        funciones.mostrar_registro()
        opcion = input("\nElija una opción: ")
        funciones.manejar_opciones_registro(opcion)

    else: 
        #Aqui nos muestra el menu Principal donde puede realizar todas las opciones el Usuario
        print("\nMenú Autenticado:\n")
        print("1. Registro de nueva casa y habitacion")
        print("2. Ver casas y habitaciones registradas")
        print("3. Actualizar PIN")
        print("4. Agregar un dispositivo")              #KISS & ERICK WORKING ON IT
        print("5. Cerrar sesión\n")
        

        autenticado_opcion = input("Elija una opción: ")

        #Esta opcion nos permite ingresar una nueva casa y habitacion
        if autenticado_opcion == "1":

            funciones.registrar_casa_habitacion()
            funciones.guardar_datos_json()

        #Esta opcion nos permite ver el registro de nuestras casas y habitaciones
        elif autenticado_opcion == "2":

            print("\nCasas y Habitaciones Registradas:\n")

            for casa, habitaciones in funciones.casas_creadas.items():

                print(f"Casa: {casa}")

                for habitacion in habitaciones['habitaciones']:
                    print(f"Habitación: {habitacion}")

                print("")  


        #Esta opcion del menu es para actualizar el pin
        elif autenticado_opcion == "3":

            pinActual = input("\nIngrese su Contraseña Actual: ")
            pinNuevo = input("\nIngrese su Nueva Contraseña:")
            funciones.cambiarPin(pinActual, pinNuevo)
            funciones.guardar_datos_json()


        #En esta opcion nos permite ingresar un nuevo dispositivo
        elif autenticado_opcion == "4":

            funciones.AgregarDispositivo()         
            funciones.guardar_datos_json()

        #En esta opcion es para cerrar sesion
        elif autenticado_opcion == "5":

            print("Cerrando sesión...")
            funciones.usuario_autenticado = None  
            funciones.autenticado= False
            funciones.guardar_datos_json()

        #Opcion invalidad
        else:
            print("Opcion invalida")        