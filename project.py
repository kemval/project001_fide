existing_rooms = set()  # Set to store existing room names

while True:
    def register_new_room():
     
        room_name = input("Enter the room name: ").title() # input from user

        if room_name == "E":
            exit() 

        elif room_name in existing_rooms:                                            # review if we have an existing room duplicated
            print("Room name already exists. Please choose a different name.")
        
        else:
            existing_rooms.add(room_name)
            print("Room registered successfully.")

    # Example usage:
    register_new_room()
    