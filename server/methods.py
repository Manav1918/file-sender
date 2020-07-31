import socket
import os

import buffer
def send():
    HOST = '127.0.0.1'
    PORT = 2345
    connection = False
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c = s.connect((HOST, PORT))
    print(c)

    with s:
        sbuf = buffer.Buffer(s)

        hash_type = input('Enter hash type: ')

        files = input('Enter file(s) to send: ')
        files_to_send = files.split()

        for file_name in files_to_send:
            print(file_name)
            sbuf.put_utf8(hash_type)
            sbuf.put_utf8(file_name)


            file_size = os.path.getsize(file_name)
            print("{:.2f} MB".format(file_size/(1024*1024)))
            sbuf.put_utf8(str(file_size))

            with open(file_name, 'rb') as f:
                sbuf.put_bytes(f.read())
            print('File Sent')

def recieve():
    HOST = ''
    PORT = 2345

    # If server and client run in same local directory,
    # need a separate place to store the uploads.
    try:
        os.mkdir('downloads')
    except FileExistsError:
        pass

    s = socket.socket()
    s.bind((HOST, PORT))
    s.listen(10)
    print("Waiting for a connection.....")

    while True:
        conn, addr = s.accept()
        print("Got a connection from ", addr)
        connbuf = buffer.Buffer(conn)

        while True:
            hash_type = connbuf.get_utf8()
            if not hash_type:
                break
            print('hash type: ', hash_type)

            file_name = connbuf.get_utf8()
            file_size = int(connbuf.get_utf8())
            if not file_name or not file_size:
                print("Wrong file or connection closed.")
                break
            file_name = file_name.split('/')[-1]
            file_name = os.path.join('downloads/',file_name)
            print('file name: ', file_name) 
            print('file size: {:.2f} MB'.format(file_size/(1024*1024)))

            with open(file_name, 'wb') as f:
                remaining = file_size
                while remaining:
                    chunk_size = 4096 if remaining >= 4096 else remaining
                    chunk = connbuf.get_bytes(chunk_size)
                    if not chunk: break
                    f.write(chunk)
                    remaining -= len(chunk)
                    #print("\rSent: {:.2f} MB".format((file_size-remaining)/(1024*1024)))
                if remaining:
                    print('File incomplete.  Missing',remaining,'bytes.')
                else:
                    print('File received successfully.')
        print('Connection closed.')
        conn.close()

if __name__ == "__main__":
    ask = int(input("What do you want?\n1. Send\n2. Recieve\n\n"))
    if ask is 1:
        send()
    elif ask is 2:
        recieve()
