import socket
import ssl
import threading

HOST = '127.0.0.1'
PORT = 5555

# Create TLS/SSL context
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE  # disable certificate verification for testing

# Create normal socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
secure_sock = context.wrap_socket(sock, server_hostname=HOST)
secure_sock.connect((HOST, PORT))

print("🔐 Connected securely to the chat server.")
print("Type your message and press Enter (type 'exit' to quit)")

# Function to receive and print messages from server
def receive_messages():
    while True:
        try:
            data = secure_sock.recv(1024)
            if data:
                print(data.decode())
        except:
            break

threading.Thread(target=receive_messages, daemon=True).start()

while True:
    msg = input("")
    if msg.lower() == "exit":
        break
    secure_sock.send(msg.encode())

secure_sock.close()
