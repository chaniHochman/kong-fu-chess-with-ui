# פתיחת השרת.
# המתנה ללקוחות.
# קבלת חיבורים.
# שליחת הודעות.

import socket
import threading

class TCPServer:
    
    def __init__(self, bus):

        self.bus = bus

        self.clients = []

    
    def start(self):
        """
        מפעיל את השרת.
        """

        server_socket = socket.socket(
            socket.AF_INET,  #נשתמש בכתובות IPv4.
            socket.SOCK_STREAM  #נשתמש בפרוטוקול TCP.
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
            
            # session = session_manager.create_session(
            #     client_socket
            # )
            
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

            #קבל עד 1024 בתים מהחיבור
            message = client.recv(
                1024
            )

            if not message:
                break

            text = message.decode() #מחזיר למחרוזת רגילה


            event = {

                "type":"CLIENT_MESSAGE",

                "data":text

            }
            self.bus.publish(event)