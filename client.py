
# Import socket module 
import socket                

# Message to send from client
MESSAGE = "Hello"

# Create a socket object 
s = socket.socket()          
  
# Define the port on which you want to connect 
port = 9500                
  
# connect to the server on local computer 
s.connect(('127.0.0.1', port)) 
  
s.send(MESSAGE.encode())
print('Client sent: ', MESSAGE)

# receive data from the server 
data = s.recv(1024).decode()
print('Server sent: ', data)
# close the connection 
s.close()   