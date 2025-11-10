<img width="1919" height="1078" alt="Screenshot 2025-11-05 095643" src="https://github.com/user-attachments/assets/4b2df75e-f1dd-446f-bd59-db4e4799609e" />
<img width="1919" height="1078" alt="Screenshot 2025-11-05 095632" src="https://github.com/user-attachments/assets/6253df33-468b-4ee1-9737-6974872e0a28" />
<img width="1919" height="1078" alt="Screenshot 2025-11-05 095632" src="https://github.com/user-attachments/assets/a9c17810-c607-41df-8b9b-783bd5474e97" />
<img width="1919" height="1078" alt="Screenshot 2025-11-05 095643" src="https://github.com/user-attachments/assets/8aef5b0a-0b3d-4657-9114-36572ccecbec" />
<img width="1916" height="456" alt="Screenshot 2025-11-05 095654" src="https://github.com/user-attachments/assets/bdb60d05-198a-48fc-8bee-74f07baaf186" />
# 🔒 TLS Encrypted Multi-Client Chat (Secure Chat)

This project is a **Python-based secure chat system** that uses **TLS encryption** to provide safe, private, and real-time communication between multiple clients connected to a server.

---

## 🧠 Overview

The goal of this project is to create a **secure client-server chat application** where:
- Multiple clients can connect to a single server.
- All messages are encrypted using **TLS (Transport Layer Security)**.
- Each client can send and receive encrypted messages securely.

---

## 🚀 Features

✅ **End-to-End Encryption** – All communication uses TLS to prevent eavesdropping.  
✅ **Multi-Client Support** – Multiple users can chat simultaneously through sockets.  
✅ **Server & Client Authentication** – Uses `.crt` and `.key` certificates.  
✅ **Real-Time Chat** – Messages are broadcast instantly to all connected clients.  
✅ **Cross-Platform** – Works on any system with Python 3.8+.

---

## ⚙️ How It Works

1. The **server** creates a TLS socket using a certificate (`server.crt`) and key (`server.key`).  
2. Each **client** connects using a TLS-encrypted socket.  
3. Messages from one client are broadcast securely to all others.  
4. Data remains encrypted during the entire transmission.

---

📦 TLS-encrypted-Multi-Client-Chat-secure-chat
┣ 📜 client.py
┣ 📜 server.py
┣ 🔑 server.crt
┣ 🔑 server.key
┣ 📜 README.md
┗ 📜 requirements.txt


---

## 🧰 Requirements

- Python 3.8 or higher  
- OpenSSL (for generating certificates)  
- Basic knowledge of sockets and encryption  

To install required packages (if any):
```bash
pip install -r requirements.txt

▶️ How to Run
🖥️ 1. Start the Server

Run:

python server.py


This launches the server, which listens for client connections using TLS.

💻 2. Start the Clients

Run the following in separate terminals or machines:

python client.py


Each client connects to the server over TLS and can chat securely with others.

💬 Example Output
🖥️ Server Running and Waiting for Connections
<img width="1919" height="1078" alt="Server Screenshot" src="https://github.com/user-attachments/assets/4b2df75e-f1dd-446f-bd59-db4e4799609e" />
💻 Client Connecting to Server
<img width="1919" height="1078" alt="Client Connection" src="https://github.com/user-attachments/assets/6253df33-468b-4ee1-9737-6974872e0a28" />
💬 Chat Session Between Multiple Clients
<img width="1919" height="1078" alt="Multi Client Chat" src="https://github.com/user-attachments/assets/a9c17810-c607-41df-8b9b-783bd5474e97" />
🔐 Encrypted Communication Log on Server
<img width="1919" height="1078" alt="Server Logs" src="https://github.com/user-attachments/assets/8aef5b0a-0b3d-4657-9114-36572ccecbec" />
📡 Secure Message Exchange Example
<img width="1916" height="456" alt="Message Example" src="https://github.com/user-attachments/assets/bdb60d05-198a-48fc-8bee-74f07baaf186" />
🔑 TLS Certificate Details

If you need to create your own TLS certificate and key, use OpenSSL:

openssl req -new -x509 -days 365 -nodes -out server.crt -keyout server.key


server.crt → Public certificate

server.key → Private key (keep secure!)

🧪 Future Improvements

✅ Add GUI with Tkinter or PyQt for easier chat interaction

✅ Add user authentication and nicknames

✅ Enable message logging and history

✅ Add file-sharing capability

✅ Containerize with Docker for deployment

👨‍💻 Author

Japesh21
🔗 GitHub Profile

🪪 License

This project is open-source under the MIT License.
You are free to use, modify, and share it.
