import socket
import time

def invia_ordine(ordine):
    indirizzo_server = 'indirizzo_ip_cucina'
    porta_server = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((indirizzo_server, porta_server))
        client_socket.sendall(ordine.encode())

        conferma = client_socket.recv(1024).decode()
        print(conferma)

    except ConnectionRefusedError:
        print("Impossibile connettersi al server: connessione rifiutata.")
    except socket.timeout:
        print("Timeout durante la connessione al server.")
    except Exception as e:
        print("Errore durante la connessione al server:", e)

    finally:
        client_socket.close()

def main():
    print("Benvenuto al Ristorante!")
    time.sleep(1)
    print("Ecco il menu:")
    time.sleep(1)
    menu = ["Pizza Margherita", "Spaghetti alla Carbonara", "Insalata mista"]
    for piatto in menu:
        print("- " + piatto)
    time.sleep(1)

    while True:
        ordine_cliente = input("Cosa desideri ordinare? ")
        if ordine_cliente.strip():
            break
        else:
            print("Inserisci un ordine valido!")

    print("Invio l'ordine alla cucina...")
    invia_ordine(ordine_cliente)


if __name__ == "__main__":
    main()
