from tcp_client import TCPClient
import threading


client = TCPClient()

client.connect()

listener = threading.Thread(

    target=client.receive_messages

)

listener.start()

while True:

    message = input(
        "Command:"
    )


    client.send_message(
        message
    )