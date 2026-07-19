# # קבלת חיבורים
# # קבלת הודעות מהקליינטים
# # שליחת הודעות בחזרה


# import websockets
# import asyncio
# #create server

# clients = []


# async def handler(websocket):

#     clients.append(websocket)

#     print("Player connected")


#     try:

#         async for message in websocket:

#             print(message)


#             for client in clients:
#                 await client.send(message)


#     except:

#         clients.remove(websocket)



# async def start():

#     server = await websockets.serve(
#         handler,
#         "localhost",
#         8765
#     )


#     print("Server running")

#     await server.wait_closed()



# asyncio.run(start())