users = {}
existing_rooms = set()

def login(username, password):        #Funcion para validar el login del usuario
    if username in users and users[username]['password'] == password:
        current_user = users[username]
        print (f'Bienvenido, {current_user["username"]}!')
    else:
        return 'usuario y/o contrasena invalido'

def register(username, password):      #Funcion para hacer el registro de un nuevo usuario
    if username in users:
        return 'El usuario ya existe'
    users[username] = {'username': username, 'password': password}
    return 'Usuario registrado correctamente'
def show_registration():     #Funcion para mostrar los usuarios registrados
    if users:
        print("Usuarios registrados:")
        for user in users.values():
            print(f"Username: {user['username']}")
        print("")
    
    print("Options:")
    print("1. Login")
    print("2. Register")
    print("3. Salir")

def handle_registration_option(option):   #Funcion para controlar el menu
    if option == "1":
        username = input("Digite su usuario: ")
        password = input("Digite su contrasena: ")
        print(login(username, password))
        
    elif option == "2":
        username = input("Digite su usuario: ")
        password = input("Digite su contrasena: ")
        print(register(username, password))
    elif option == "3":
        print("Saliendo...")
        exit()
    else:
        print("Opcion invalida")

def register_new_room(): #funcion para agregar nueva habitacion

    room_name = input("Enter the room name: ").title() # input from user

    if room_name == "E":
        exit() 

    elif room_name in existing_rooms:                                            # review if we have an existing room duplicated
        print("Este cuarto ya existe, por favor digite uno diferente.")
        
    else:
        existing_rooms.add(room_name)
        print("Cuarto registrado correctamente.")

while True:
    show_registration()
    option = input("Eliga una opcion: ")
    handle_registration_option(option)
