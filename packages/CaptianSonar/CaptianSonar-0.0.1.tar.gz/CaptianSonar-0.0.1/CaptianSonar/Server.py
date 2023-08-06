import socket
from threading import Thread as T
from contextlib import suppress

FORMAT = 'utf-8'
PORT = 4445
IP = socket.gethostbyname('Awesome-Acer')
ADDR = (IP, PORT)

MyRooms = []
rooms = []
dictOfConns = {}

Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Server.bind(ADDR)

def handle_client(conn, addr):#sourcery skip
    password = conn.recv(2800).decode(FORMAT)
    if password != 'Caption Sonar SUPER SECRET SPECIAL password':
        conn.close()
        print(f"{'%'*33}\n"*3, end='')
        print(f'{addr} is probably a hacker and is now disconnected')
        print(f"{'%' * 33}\n" * 3)
    while True:
        try:
            fist_recv = conn.recv(8300)
            second_recv = fist_recv.decode(FORMAT)
            Message = eval(second_recv)
            if isinstance(Message, dict):
                try:
                    file = open('stats.txt', 'a')
                except FileNotFoundError:
                    file = open('stats.txt', 'w')
                file.write(f"{str(Message)}-")
                file.close()
                return

        except ConnectionResetError:
            break
        if Message[0] == 'Give Me Stats':
            with suppress(FileNotFoundError):
                file = open('stats.txt')
                conn.send(str(['Your Stats', file.read().removesuffix('-')]).encode(FORMAT))
                file.close()
        if Message[0] == 'TO MY PARTNER':
            Message.pop(0)
            msg = ['FROM YOUR PARTNER']
            for thing in Message:
                msg.append(thing)
            try:
                client = dictOfConns[conn][0]
            except TypeError:
                client = dictOfConns[conn]
            try:
                client.send(str(msg).encode(FORMAT))
            except OSError:
                dictOfConns[client].send(str(['FROM YOUR PARTNER', 'You Win']).encode(FORMAT))
        if Message[0] == 'JOINING GAME':
            for room in rooms:
                if room[1] == Message[1]:#The Requester has found his game
                    dictOfConns[MyRooms[rooms.index(room)][1]] = conn
                    dictOfConns[conn] = [MyRooms[rooms.index(room)][1]]
                    try:
                        MyRooms[rooms.index(room)][1].send(str(['Game Started']).encode(FORMAT))
                    except OSError:
                        conn.send(str(['FROM YOUR PARTNER', 'You Win']).encode(FORMAT))
                    MyRooms.pop(rooms.index(room))
                    rooms.remove(room)
        if Message[0] == 'New Game':
            rooms.append([Message[1], Message[2], Message[3], Message[4], Message[5], Message[6], Message[7], Message[8], Message[9]])
            MyRooms.append([Message[1], conn])
        if Message[0] == 'Give Me Rooms':
            conn.send(str(['Your Rooms', rooms]).encode(FORMAT))
    conn.close()
    print(f'{addr} has suddenly disconnected')

def start():
    print('[SERVER IS LISTENING]')
    Server.listen()
    while True:
        conn, addr = Server.accept()
        dictOfConns[addr] = conn
        print(f'[NEW CONNECTION] {addr[0]} connected')
        T(target=handle_client, args=(conn, addr[0])).start()

print('[SERVER IS STARTING]')
start()
