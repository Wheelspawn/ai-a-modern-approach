
import os
import sys
import socket
import select

# https://realpython.com/python-sockets
# python chat.py user1 5001 127.0.0.1:5002 127.0.0.1:5003
# python chat.py user2 5002 127.0.0.1:5001 127.0.0.1:5003
# python chat.py user3 5002 127.0.0.1:5001

# python chat.py user1 5001 127.0.0.1:5002
# python chat.py user2 5002 127.0.0.1:5001

def main():
    try:
        user = sys.argv[1]
        port = int(sys.argv[2])
        clients = sys.argv[3:]

        client_sockets=[]

        HOST = '127.0.0.1'

        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
            s.bind((HOST,port))
            print('end 0')

            for client in clients:
                new_s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                try:
                    new_s.connect((HOST, int(client.split(':')[-1])))
                    client_sockets.append(new_s)
                except ConnectionRefusedError:
                    print('Connection refused by ' + str(port))
            
            s.listen()
            
            print('end 1')

            conn, addr = s.accept()
            print('end 2 (accepted)')

            while True:
                ready_list,_,_ = select.select([s], [], [])
                print(ready_list)
                print('end 4')
                input()
                
                for r in ready_list:
                    if r == server_socket:
                        conn, addr = s.accept()
                    elif r == sys.stdin:
                        txt = input()
                    else:
                        pass
                    if not data:
                        break
                    data=r.recv(1024)
                    r.sendall(data)

    except KeyboardInterrupt:
        exit()

if __name__ == '__main__':
    main() # 'user1', 5001, ['127.0.0.1:5002', '127.0.0.1:5003'])
