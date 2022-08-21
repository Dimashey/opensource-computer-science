import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

resp = []

while True:
    data = mysock.recv(200)
    if not data: break  
    resp.append(data.decode())

mysock.close()

resp = "".join(resp)
body = resp.partition('\r\n\r\n')[2]
print(body)
