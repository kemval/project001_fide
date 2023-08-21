import funciones_actualizado2

funciones_actualizado2.cargar_datos_json()

while True:

    if not funciones_actualizado2.autenticado:  
        #El Menu de inicio para verificar si estar registrado o no
        print("\nMenu Principal:\n")
        print("1. Registro")
        print("2. Ingresar")
        print("3. Salir\n")
    
        funciones_actualizado2.mostrar_registro()
        opcion = input("\nElija una opción: ")
        funciones_actualizado2.manejar_opciones_registro(opcion)

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

            funciones_actualizado2.registrar_casa_habitacion()
            funciones_actualizado2.guardar_datos_json()

        #Esta opcion nos permite ver el registro de nuestras casas y habitaciones
        elif autenticado_opcion == "2":

            print("\nCasas y Habitaciones Registradas:\n")

            for casa, habitaciones in funciones_actualizado2.casas_creadas.items():

                print(f"Casa: {casa}")

                for habitacion in habitaciones['habitaciones']:
                    print(f"Habitación: {habitacion}")

                print("")  


        #Esta opcion del menu es para actualizar el pin
        elif autenticado_opcion == "3":

            pinActual = input("\nIngrese su Contraseña Actual: ")
            pinNuevo = input("\nIngrese su Nueva Contraseña:")
            funciones_actualizado2.cambiarPin(pinActual, pinNuevo)
            funciones_actualizado2.guardar_datos_json()


        #En esta opcion nos permite ingresar un nuevo dispositivo
        elif autenticado_opcion == "4":

            funciones_actualizado2.AgregarDispositivo()         
            funciones_actualizado2.guardar_datos_json()

        #En esta opcion es para cerrar sesion
        elif autenticado_opcion == "5":

            print("Cerrando sesión...")
            funciones_actualizado2.usuario_autenticado = None  
            funciones_actualizado2.autenticado= False
            funciones_actualizado2.guardar_datos_json()

        #Opcion invalidad
        else:
            print("Opcion invalida")        