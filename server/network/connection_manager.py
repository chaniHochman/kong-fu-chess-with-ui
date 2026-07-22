#מנהל חיבורים
# אחראי על:
# TCP
# Socket
# Close
# Receive
# Send
class ConnectionManager:
    """
    Manages all active client connections.

    Does not know users or games.
    """


    # Creates an empty connection list.
    def __init__(self):

        self._connections = []



    # Adds a new client connection.
    def add(self, connection):

        self._connections.append(
            connection
        )



    # Removes a client connection.
    def remove(self, connection):

        if connection in self._connections:

            self._connections.remove(
                connection
            )



    # Returns all active connections.
    def get_all(self):

        return self._connections.copy()



    # Closes every connection.
    def close_all(self):

        for connection in self._connections:

            connection.close()


        self._connections.clear()