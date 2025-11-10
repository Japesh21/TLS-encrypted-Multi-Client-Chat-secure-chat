import socket
import ssl
import threading

HOST = '127.0.0.1'   # localhost
PORT = 5555          # port for chat

# Create SSL context (TLS)
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="server.crt", keyfile="server.key")

# Create normal TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"🔒 Secure Chat Server started on {HOST}:{PORT}")

clients = []  # store active client connections

# Function to handle each connected client
def handle_client(conn, addr):
    print(f"✅ {addr} connected securely.")
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            message = f"{addr}: {data.decode()}"
            print(message)
            # Broadcast message to other clients
            for c in clients:
                if c != conn:
                    c.send(message.encode())
    except Exception as e:
        print(f"⚠️ Connection error with {addr}: {e}")
    finally:
        conn.close()
        clients.remove(conn)
        print(f"❌ {addr} disconnected.")

# Accept and wrap clients with TLS
while True:
    client_socket, addr = server_socket.accept()
    secure_conn = context.wrap_socket(client_socket, server_side=True)
    clients.append(secure_conn)
    threading.Thread(target=handle_client, args=(secure_conn, addr)).start()
