import socket
import requests
import threading
import getpass
import sys
import pypresence
import time
import os
import ctypes
from plyer import notification
import os
import loadwave

def main():
    arg = sys.argv[1]
    global PORT
    PORT = 5050
    if(arg == "kenu-1"):
        HOST = "20.238.119.193"
        connectserver(arg, HOST)
    elif(arg == "kenu-2"):
        HOST = "20.250.2.200"
        connectserver(arg, HOST)
    else:
        print("This server is invalid.")
        exit()
    
    try:
        client_id = '1085214791771111485'
        global RPC
        RPC = pypresence.Presence(client_id)
        RPC.connect()
    except Exception as e:
        pass

def signin():
    global username
    global password
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
        

def handle_receive():
    while True:
        try:
            message = client.recv(1024).decode()
            if "0xx1m" in message:
                words = message.split("0xx1m ")
                username = words[1].split(" ")[0]
                if(len(words) > 0):
                    notification.notify(
                        title=username,
                        message=words[1].split(">")[1],
                        app_name='KenuCord',
                        timeout=3,
                    )
                else:
                    notification.notify(
                        title=username,
                        message='You got mention!',
                        app_name='KenuCord',
                        timeout=3,
                    )
            elif("You have entered the room" in message):
                words = message.split("You have entered the room ")
                if("0" not in words[1]):
                    rpcupdate("in private room")
                elif("0" in words[1]):
                    rpcupdate("in lobby")
                print(f"{message}")
            elif("You were banned from KenuCord." in message):
                print(f"{message}")
                client.getpeername()
                client.close()
                exit()
            else:
                print(f"{message}")
        except Exception as e:
            sys.exit()

def rpcupdate(state, details = "Chatting on kenucord"):
    try:
        RPC.update(details=details, state = state, large_image="kenulogo", large_text=username)
    except Exception as e:
        return

def login():
    client.send(username.encode())
    client.send(password.encode())
    response = client.recv(1024).decode()
    print(response)
    if "Connected to the server. You can now chat with others." in response:
        rpcupdate("in lobby")

                
        return True
    else:
        return False

def start_client(server):
    try:
        global client
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((server, PORT))
        signin()
        if login() == False:
            print("Try again. \n")
            signin()
        receive_thread = threading.Thread(target=handle_receive)
        receive_thread.start()
    except Exception as e:
        HOST = "20.250.2.200"
        if(server != HOST):
            print("The kenu-1 server is offline due to an unknown reason. We are transferring you to the kenu-2 server.")
            connectserver(HOST)
        else:
            print("The server did not respond.")
        
        time.sleep(2)
        sys.exit()

    while True:
        try:
            message = input()
            client.send(message.encode())
        except KeyboardInterrupt:
            print("Closing connection...")
            client.close()
            sys.exit()
        except:
            client.close()
            sys.exit()

    

def connectserver(server, servername ="kenu-1"):
    print("Connecting to the server. - " + servername)
    connectserverld()
    start_client(server)

@loadwave.process
def connectserverld():
    time.sleep(3.5)