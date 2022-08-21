import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/mbox.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

count = 0

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break

    line = data.decode()
    count += len(line.strip().split())

    if count >= 3000:
        end = 3000 - len(line.strip().split())
        print(line[:end])
        break

    print(line)


print(count)
        

mysock.close()

