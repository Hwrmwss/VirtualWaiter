import socket

indirizzo_server = '127.0.0.1'
porta_server = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((indirizzo_server, porta_server))

server_socket.listen(1)

print("In attesa di ordini...")

while True:
    conn, addr = server_socket.accept()
    print('Connesso a:', addr)

    ordine = conn.recv(1024).decode()
    print("Nuovo ordine:", ordine)

    conferma_ordine = "Ordine ricevuto e in preparazione!"
    print(conferma_ordine)

    conn.sendall(conferma_ordine.encode())

    conn.close()
