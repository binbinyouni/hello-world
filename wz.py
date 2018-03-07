from socket import *
from multiprocessing import Process


def deal(conn):
    recv_data = conn.recv(1024).decode('gb2312')
    print(recv_data)
    conn.send('HTTP/1.1 200 OK \r\n\r\n <h1>hello world</h1>'.encode('gb2312'))

def main():
    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(('',8000))
    s.listen(1023)

    while 1:
        conn, user_info = s.accept()
        print(user_info)
        p = Process(target=deal, args=(conn,))
        p.start()
        conn.close()


if __name__ == '__main__':
    main()