import socket
import threading

nickname=input('Choose a nickname: ')

user=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
user.connect(('127.0.0.1', 55555))

def recieve():
     while True:
         try:
             message=user.recv(2048).decode('ascii')
             if message=='NICK':
                 user.send(nickname.encode('ascii'))
             else:
                 print(message)
         except:
            print('An error occured!')
            user.close()
            break

def write():
    while True:
        message=f'{nickname}: {input("")}'
        user.send(message.encode('ascii'))

recieve_thread=threading.Thread(target=recieve)
recieve_thread.start()

write_thread=threading.Thread(target=write)
write_thread.start()