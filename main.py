import funciones

funciones.cargar_datos_json()

while True:

    if not funciones.autenticado:  
        print("\nMenu Principal:\n")
        print("1. Registro")
        print("2. Ingresar")
        print("3. Salir\n")
    
        funciones.mostrar_registro()
        opcion = input("\nElija una opción: ")
        funciones.manejar_opciones_registro(opcion)

    else:  
        print("\nMenú Autenticado:\n")
        print("1. Registro de nueva casa y habitacion")
        print("2. Ver casas y habitaciones registradas")
        print("3. Actualizar PIN")
        # print("3. Agregar un dispositivo")              #KISS & ERICK WORKING ON IT
        print("4. Cerrar sesión\n")
        

        autenticado_opcion = input("Elija una opción: ")

        if autenticado_opcion == "1":

            funciones.registrar_casa_habitacion()
            funciones.guardar_datos_json()

        elif autenticado_opcion == "2":

            print("\nCasas y Habitaciones Registradas:\n")

            for casa, habitaciones in funciones.casas_creadas.items():

                print(f"Casa: {casa}")

                for habitacion in habitaciones['habitaciones']:
                    print(f"Habitación: {habitacion}")

                print("")  



        elif autenticado_opcion == "3":

            pinActual = input("\nIngrese su Contraseña Actual: ")
            pinNuevo = input("\nIngrese su Nueva Contraseña:")
            funciones.cambiarPin(pinActual, pinNuevo)
            funciones.guardar_datos_json()



        # elif autenticado_opcion == "3":

        #     funciones.AgregarDispositivo()          #KISS & ERICK WORKING ON IT
        #     funciones.guardar_datos_json()


        elif autenticado_opcion == "4":

            print("Cerrando sesión...")
            funciones.usuario_autenticado = None  
            funciones.autenticado= False
            funciones.guardar_datos_json()

        else:
            print("Opcion invalida")        