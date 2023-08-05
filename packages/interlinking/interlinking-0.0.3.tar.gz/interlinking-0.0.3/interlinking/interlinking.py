import socket
import os
import tqdm
import pickle
import time
import threading

class Server:
    def __init__(self,output=True, port=5000,format="ascii",host=socket.gethostbyname(socket.gethostname())):
        super(Server, self).__init__()
        self.connections = []
        self.format = format
        self.host = host
        self.port = port
        self.output = output
        self.running = True
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.conn,self.addr = None, None
        def check():
            while True:
                for x in self.connections:
                    data = x[0].recv(1024)
                    if data == b"":
                        self.connections.remove(list([x[0],x[1],x[2]]))
                time.sleep(1)
    
        def x():
            while True:
                self.server.listen()
                self.conn, self.addr = self.server.accept()
                message = ""
                while not message.startswith("$"):
                    message = self.conn.recv(1024).decode(self.format)
                if message.split("$")[2] != "!AUTHORIZE":
                    self.conn.shutdown(socket.SHUT_RDWR)
                    self.conn.close()
                    continue
                self.connections.append(list([self.conn, self.addr, message.split("$")[1]]))
                
        t = threading.Thread(target=x)
        t.start()
        t2 = threading.Thread(target=check)
        t2.start()
        self.messages = []
        return
    def recive_msg(self):
        def recive(conn, addr):
            message = ""
            while message == "":
                try:
                    message = conn.recv(1024).decode(self.format)
                except ConnectionResetError:
                    for x in self.connections:
                        try:
                            x.find(conn)
                            self.connections.remove(list([conn, addr, x[2]]))
                            break 
                        except:
                            continue
            final_msg = message
            message = message.split("$")
            check_message = message
            message = message[2]
            if "!USER" in message:
                message, user = message.split("!USER")
                for clients in self.connections:
                    if clients[2] == user.strip():
                        try:
                            clients[0].sendall(final_msg.encode(self.format))
                            break
                        except:
                            try:
                                self.connections.remove(list([conn, addr, check_message[1]])) 
                                continue
                            except:
                                continue
                return
            if self.output == True:
                print(f"[CLIENT] {addr[0]} -- {message}")
            self.messages.append(message)
        self.check = []
        while True:
            if len(self.connections) > 0:
                for i in range(len(self.connections)):
                    try:
                        if list([self.connections[i][0], self.connections[i][1]]) not in self.check:
                            t = threading.Thread(target=recive, args=(self.connections[i][0], self.connections[i][1],))
                            t.start()
                            self.check.append(list([self.connections[i][0], self.connections[i][1]]))
                    except IndexError:
                        continue
    def stop_server(self):
        self.running == False
        self.server.shutdown(socket.SHUT_RDWR)
        self.server.close()
        return
    def recive_file(self, name=None):
        check = False
        for x in self.connections:
            if x[2] == name.strip():
                check = True
                conn, addr = x[0], x[1]
            if name == None:
                break
        if check == False:
            while self.conn == None and self.addr == None:
                conn, addr = self.conn, self.addr
        self.recived = False
        file_name = conn.recv(1024).decode(self.format)
        file_name = conn.recv(1024).decode(self.format)
        file_size = conn.recv(1024).decode(self.format)
        file = open(file_name, "wb")
        file_bytes = b""
        done = False
        progress = tqdm.tqdm(unit="B", unit_scale=True, unit_divisor=1000,total=int(file_size))
        while not done:
            data = conn.recv(1024)
            if file_bytes[-5:] == b"<END>":
                done = True
            else:
                file_bytes += data
            progress.update(1024)
        file_bytes = file_bytes.split(b"<END>")[0]
        file.write(file_bytes)
        file.close()
        self.recived = True
    def recive_data(self, name=None):
        check = False
        for x in self.connections:
            if x[2] == name.strip():
                check = True
                conn, addr = x[0], x[1]
            if name == None:
                break
        if check == False:
            while self.conn == None and self.addr == None:
                conn, addr = self.conn, self.addr
        data = conn.recv(1024)
        try:
            data = pickle.loads(data)
            return data
        except AttributeError:
            print("[SERVER] -- use brackets -- ")
            return "ERROR"

        
class Client:
    def __init__(self,name,output=True, recive=True,host=socket.gethostbyname(socket.gethostname()), port=5000, format="ascii"):
        super(Client, self).__init__()
        self.host = host
        self.name = name
        self.port = port
        self.format = format
        self.output = output
        self.recive = recive
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected = True
        self.client.connect((self.host, self.port))
        def x():
            self.client.send(f"${self.name}$!AUTHORIZE".encode(self.format))
        t = threading.Thread(target=x)
        t.start()
        t.join()
        time.sleep(0.2)
        
        self.mess = None
        def recive_msg():
            while self.recive:
                try:
                    message = self.client.recv(1024).decode(self.format)
                except:
                    break
                if message == "":
                    message = self.client.recv(1024).decode(self.format)
                msg = message.split("$")
                m = msg[2].split("!USER")[0]
                if self.output:
                    print(f"{msg[1]} > {m}")
                self.mess = f"{msg[1]} > {msg[2]}"
        
        t = threading.Thread(target=recive_msg)
        t.start()
        
    def stop_client(self):
        self.recive = False
        self.client.shutdown(socket.SHUT_RDWR)
        self.client.close()
    def send_msg(self, message):
        message = f"${self.name}${message}"
        self.client.send(message.encode(self.format))
    def send_file(self, filename, send_filename=None):
        if send_filename == None:
            send_filename = filename
        try:
            file = open(filename, "rb")
            file_size = os.path.getsize(filename)
        except:
            print("[SERVER] -- filename doesnt exist -- ")
        self.client.send(send_filename.encode(self.format))
        self.client.send(str(file_size).encode (self.format))
        data = file.read()
        self.client.sendall(data)
        self.client.send(b"<END>")
        file.close()
    def send_data(self, data):
        data = pickle.dumps(data)
        self.client.send(data)
        
