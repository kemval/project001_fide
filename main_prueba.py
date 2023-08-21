import funciones_prueba

funciones_prueba.cargar_datos_json()

while True:

    if not funciones_prueba.autenticado:  
        #El Menu de inicio para verificar si estar registrado o no
        print("\nMenu Principal:\n")
        print("1. Registro")
        print("2. Ingresar")
        print("3. Salir\n")
    
        funciones_prueba.mostrar_registro()
        opcion = input("\nElija una opción: ")
        funciones_prueba.manejar_opciones_registro(opcion)

    else: 
        #Aqui nos muestra el menu Principal donde puede realizar todas las opciones el Usuario
        print("\nMenú Autenticado:\n")
        print("1. Registro de nueva casa, habitacion y dispositivos")
        print("2. Ver casas y habitaciones registradas")
        print("3. Actualizar PIN")
        print("4. Cerrar sesión\n")

        

        autenticado_opcion = input("Elija una opción: ")

        #Esta opcion nos permite ingresar una nueva casa y habitacion
        if autenticado_opcion == "1":

            funciones_prueba.registrar_casa_habitacion()
            funciones_prueba.guardar_datos_json()

        #Esta opcion nos permite ver el registro de nuestras casas y habitaciones
        elif autenticado_opcion == "2":

            print("\nCasas y Habitaciones Registradas:\n")

            for casa, habitaciones in funciones_prueba.casas_creadas.items():

                print(f"Casa: {casa}")

                for habitacion in habitaciones['habitaciones']:
                    print(f"Habitación: {habitacion}")

                print("")  
 
        #Esta opcion del menu es para actualizar el pin
        elif autenticado_opcion == "3":

            pinActual = input("\nIngrese su Contraseña Actual: ")
            pinNuevo = input("\nIngrese su Nueva Contraseña:")
            funciones_prueba.cambiarPin(pinActual, pinNuevo)
            funciones_prueba.guardar_datos_json()

        #En esta opcion es para cerrar sesion
        elif autenticado_opcion == "4":

            print("Cerrando sesión...")
            funciones_prueba.usuario_autenticado = None  
            funciones_prueba.autenticado= False
            funciones_prueba.guardar_datos_json()

        #Opcion invalidad
        else:
            print("Opcion invalida")        