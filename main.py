import funciones

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
        print("2. Actualizar PIN")
        print("3. Agregar un dispositivo")
        print("4. Cerrar sesión\n")

        autenticado_opcion = input("Elija una opción: ")

        if autenticado_opcion == "1":
            funciones.registrar_casa_habitacion()


        elif autenticado_opcion == "2":
            pinActual = input("\nIngrese su Contraseña Actual: ")
            pinNuevo = input("\nIngrese su Nueva Contraseña:")
            funciones.cambiarPin(pinActual, pinNuevo)

        elif autenticado_opcion == "3":
            funciones.AgregarDispositivo()

        elif autenticado_opcion == "4":
            print("Cerrando sesión...")
            usuario_autenticado = None  
        else:
            print("Opcion invalida")        