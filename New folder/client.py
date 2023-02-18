
import socket 
import select 
import sys 
  

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
  

IP_address = "127.0.0.1" 
Port = 9999
server.bind((IP_address, Port)) 

server.listen(10) 
list_of_clients = [] 

def broadcast(message, connection): 
    for clients in list_of_clients: 
        if clients!=connection: 
            try: 
                clients.send(message.encode()) 
            except: 
                clients.close() 
  
                if clients in list_of_clients: 
                    list_of_clients.remove(clients) 

while True: 
    conn, addr = server.accept() 
    list_of_clients.append(conn) 
    print(addr[0] + " connected")
    name_of_client = conn.recv(2048).decode()
    broadcast(name_of_client + " connected", conn) 
    while True: 
            try: 
                message = conn.recv(2048).decode() 
                if message: 
                    broadcast(name_of_client + ": " + message, conn) 
  
                else: 
                    remove(conn) 
  
            except: 
                continue
conn.close() 
server.close()