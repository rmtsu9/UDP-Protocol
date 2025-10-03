from socket import *

# 1. Define server address and port
serverName = 'IP_ADDRESS'  # Replace 'IP_ADDRESS' with the actual server IP
serverPort = 12000
# 2. Create the client ’s UDP socket
# AF_INET means we are using IPv4
# SOCK_DGRAM means it is a UDP socket
clientSocket = socket( AF_INET , SOCK_DGRAM )
# 3. Get input from the user
message = input('Input lowercase sentence : ')
# 4. Send the message to the server
# The message must be encoded into bytes before sending
print (" Sending message to server ... ")
clientSocket.sendto ( message.encode() , ( serverName , serverPort ))
# 5. Receive the response from the server
# 2048 is the buffer size (how many bytes we can receive at once )
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
# 6. Print the decoded response
print ('Received from Server :', modifiedMessage.decode())
# 7. Close the socket
clientSocket.close()