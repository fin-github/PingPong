# made by fin-github

from websocket_server import WebsocketServer

def recieveMessage(client: dict, server: WebsocketServer, message: str):
    if message.lower() == "ping":
        print("Ping!")
        server.send_message(client=client, msg="pong")
        print("Pong!")
print("created recievemsg func")

server = WebsocketServer(port=8080)

server.set_fn_message_received(recieveMessage)

print("running server")
try:
    server.run_forever()
except KeyboardInterrupt:
    server.shutdown_abruptly()
