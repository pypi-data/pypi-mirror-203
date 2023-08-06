# Interlinking

In development - some bugs will be fixed in next version
Connect between servers or computers and send messages, files or raw python data.

## How to use

Server

```python
from interlinking import Server

#Start server. Output: True/False, port, format to encode - default ascii, host
server = Server()

#Server reciving from clients.
server.start_server()

#show all current connections
print(server.connections)
#returns True/False 
print(server.recived_data)
#return data
print(server.data)
```

Client

```python
from interlinking import Client

#Start reciving messages from another clients 
#name is required, host - server ip, port - server port, output,recive - if recive is enable, encode format - default ascii
client = Client("name")
#send message to server
client.send_msg("msg")
#send message to another client with name (!USER name - must be at the end)
client.send_msg("msg !USER name")
#send file
client.send_file("current file", "filename for server")
#send data (lists, classes, functions, etc.)
client.send_data(data)
#stop client
client.stop_client()
```