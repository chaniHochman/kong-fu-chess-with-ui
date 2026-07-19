from tcp_client import TCPClient
import threading


client = TCPClient()

client.connect()

listener = threading.Thread(
    target=client.receive_messages,
    daemon=True
)

listener.start()


username = input("Username: ")

password = input("Password: ")


client.login(
    username,
    password
)


while True:

    print()

    print("1. Play")
    print("2. Create Room")
    print("3. Join Room")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":

        client.play()

    elif choice == "2":

        client.create_room()

    elif choice == "3":

        room = input("Room ID: ")

        client.join_room(room)

    elif choice == "4":

        break