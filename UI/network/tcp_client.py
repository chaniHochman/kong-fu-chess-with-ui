#  להתחבר לשרת.
# לשלוח הודעות.
#  לקבל הודעות.

import json
import socket


class TCPClient:
    """
    Manages the TCP connection
    between the client and the server.
    """

    # Create client socket.
    def __init__(self):

        self.socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        self.host = "localhost"
        self.port = 5000

    # Connect to the game server.
    def connect(self):
        #create a socket and connect to the server
        self.socket.connect(
            (
                self.host,
                self.port
            )
        )

    # Send a raw message to the server.
    def send_message(self, message):

        self.socket.send(
            message.encode()
        )

    # Send a login request.
    def login(
        self,
        username,
        password
    ):

        message = {
            "type": "LOGIN",
            "payload": {
                "username": username,
                "password": password
            }
        }

        self.send_message(
            json.dumps(message)
        )

    # Send a register request.
    def register(
        self,
        username,
        password
    ):

        message = {
            "type": "REGISTER",
            "payload": {
                "username": username,
                "password": password
            }
        }

        self.send_message(
            json.dumps(message)
        )

    # Send a play request.
    def play(self):

        message = {
            "type": "PLAY",
            "payload": {}
        }

        self.send_message(
            json.dumps(message)
        )

    # Send a create room request.
    def create_room(self):

        message = {
            "type": "CREATE_ROOM",
            "payload": {}
        }

        self.send_message(
            json.dumps(message)
        )

    # Send a join room request.
    def join_room(
        self,
        room_id
    ):

        message = {
            "type": "JOIN_ROOM",
            "payload": {
                "room_id": room_id
            }
        }

        self.send_message(
            json.dumps(message)
        )

    # Send a move request.
    def send_move(
        self,
        move
    ):

        message = {
            "type": "MOVE",
            "payload": {
                "move": move
            }
        }

        self.send_message(
            json.dumps(message)
        )

    # Listen for messages from the server.
    def receive_messages(self):

        while True:

            data = self.socket.recv(1024)

            if not data:
                break

            print(
                "SERVER:",
                data.decode()
            )

    # Close the connection.
    def disconnect(self):

        self.socket.close()