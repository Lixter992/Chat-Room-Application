import threading
import socket

local_host = '127.0.0.1'
port = 59000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((local_host, port))
server.listen()

client_lists = []
name_lists = []

def broadcasting(messages):
    for client in client_lists:
        client.send(messages)

# This function is for handling the client connections
def handle_clients(client):
    while True:
        try:
            messages = client.recv(1024)
            broadcasting(messages)
        except:
            index = client_lists.index(client)
            client_lists.remove(client)
            client_lists.close()
            name = name_lists[index]
            broadcasting(f'{name} Left The Chat Room !'.encode('utf-8'))
            name_lists.remove(name)
            break

# This main function is for receiving the client connections
def receive():
    while True:
        print('Server is Running.....')
        client, address = server.accept()
        print(f'Connection is Established With {str(address)}')
        client.send('Name?'.encode('utf-8'))
        name = client.recv(1024)
        name_lists.append(name)
        client_lists.append(client)
        print(f'The Name of This Client is {name}'.encode('utf-8'))
        broadcasting(f'{name} Join The Chat Room !'.encode('utf-8'))
        client.send('You Have Join The Chat Room !'.encode('utf-8'))
        
        thread = threading.Thread(target = handle_clients, args = (client, ))
        thread.start()
        
if __name__ == "__main__":
    receive()