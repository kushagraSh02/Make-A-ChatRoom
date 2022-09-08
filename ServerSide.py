import socket
import threading

host='127.0.0.1'
port=55555

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

users=[]
nick=[]

def broadcast(message):
    for user in users:
        user.send(message)

def handle(user):
    while True:
        try:
            message=user.recv(2048)
            broadcast(message)
        except:
            index=users.index(user)
            users.remove(user)
            user.close()
            nickname = nick[index]
            broadcast(f'{nickname} left the chat'.encode('ascii'))
            nick.remove(nickname)
            break

def recieve():
    while True:
        user, address=server.accept()
        print('<' + str(address) + '>' + ' Connected!')

        user.send('NICK'.encode('ascii'))
        nickname=user.recv(2048).decode('ascii')
        nick.append(nickname)
        users.append(user)

        print(f'Nickname of user is {nickname}!')
        broadcast(f'{nickname} Joined the chat!'.encode('ascii'))
        user.send('Connected to the server'.encode('ascii'))

        thread=threading.Thread(target=handle, args=(user,))
        thread.start()


recieve()