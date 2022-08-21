import socket

url = input('Enter URL of service: ')

try:
    host_name = url.split('/')[2]
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host_name, 80))
    cmd = f"GET http://{host_name} HTTP/1.0\r\n\r\n'".encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(), end='')
except:
    print('INCORRECT SERVICE NAME')
finally:
    mysock.close()

