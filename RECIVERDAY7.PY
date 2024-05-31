import socket      #helps to access other network

s =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_address = ' 192.168.136.174'
port =8181
complete_add = (ip_address,port)
s.bind(complete_add)
while True:
    message = s.recvfrom(120)
    print(message)
    data = message[0]
    data = '\n'
    print(data.encode('ascii'))
    #print(data.encode('ascii'))


    # message =input("kya mssgae karu")
    # encript_message =message.encode("ascii")
    # s.sendto("encript_message,target")


# cli_ based    #sender  #port limit 0-65536(0 to 65536)
#ip_address = 192.168.136.174
#port =8888