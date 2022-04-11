import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("192.168.0.1", 80))
server.listen()

print("Aguardando...")

conexao, endereco = server.accept()

print("Sucesso, conexão estabelecida.", endereco)

while True:
    servidor = conexao.recv(2048)
    if servidor:        
        conexao.sendall(servidor)