import socket



class TCPClient:
    """
    Create client socket.
    """



    def __init__(self):

        self.socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )



    def connect(self):
        """
        Connect to the game server.
        """

        self.socket.connect(
            (
                "localhost",
                5000
            )
        )


    def send_message(self, message):

        """
        Send a message
        to the server.
        """


        self.socket.send(
            message.encode()
        )



    def receive_messages(self):

        """
        Listen for messages
        from the server.
        """
        while True:

            data = (
                self.socket.recv(1024)
            )

            if not data:
                break


            print(
                "SERVER:",
                data.decode()
            )