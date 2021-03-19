import threading
import socket

name = input('Please Input Your Name ---> ')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 59000))

def client_receive():
    while True:
        try:
            messages = client.recv(1024).decode('utf-8')
            
            if messages == "Name?":
                client.send(name.encode('utf-8'))
            else:
                print(messages)
        except:
            print('Error !')
            client.close()
            break

def client_send():
    while True:
        messages = f'{name} : {input("")}'
        client.send(messages.encode('utf-8'))

receiving_thread = threading.Thread(target = client_receive)
receiving_thread.start()
sending_thread = threading.Thread(target = client_send)
sending_thread.start()