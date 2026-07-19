import socket
import threading

class TCPServer:
    """
    מנהל את תקשורת הרשת
    בין השרת לשחקנים.
    """
    def __init__(self, bus):

        """
        מקבל MessageBus
        שאליו יעברו ההודעות.
        """

        self.bus = bus

        self.clients = []

    def start(self):
        """
        מפעיל את השרת.
        """

        server_socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        server_socket.bind(
            ("localhost", 5000)
        )

        server_socket.listen()

        print(
            "Server started"
        )


        while True:

            client, address = (
                server_socket.accept()
            )

            print(
                "New client:",
                address
            )

            self.clients.append(client)

            thread = threading.Thread(

                target=self.handle_client,

                args=(client,)

            )


            thread.start()



    def handle_client(self, client):
        """
        מטפל בשחקן אחד.

        קורא הודעות ממנו
        ומעביר אותן ל-BUS.
        """

        while True:


            message = client.recv(
                1024
            )

            if not message:
                break

            text = message.decode()


            event = {

                "type":"CLIENT_MESSAGE",

                "data":text

            }
            self.bus.publish(event)