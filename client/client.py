# made by fin-github

import websocket

from keyboard import add_hotkey, wait, is_pressed

# state constants
url = "ws://127.0.0.1:8080"
ws = websocket.WebSocket()

def sendPing(ws: websocket.WebSocket):
    ws.send("ping")

def PingPong(ws: websocket.WebSocket):
    print("Ping!")
    sendPing(ws=ws)
    rec = ws.recv()
    if not isinstance(rec, str):
        try:
            rec = rec.decode('utf-8')
        except:
            print("Could not decode recieved result!")
            return
    
    # rec is now str
    if rec.lower() == "pong":
        print("Pong!")

# connect to ws
ws.connect(url=url)
if ws.connected:
    print("Connected successfully!")
else:
    print("Could not connect!")
    quit()



# make pingpong hotkey
add_hotkey("p", lambda: PingPong(ws=ws))
print("Press P to send a ping pong request!\nPress E to exit.")


wait('e')
