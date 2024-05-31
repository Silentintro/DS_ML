import socket      #helps to access other network
try:
    s =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    ip_address = '192.168.233.149'
    port =8181
    target =(ip_address,port)
    message =input("kya mssgae karu")
    encript_message =message.encode("ascii")
    s.sendto("encript_message,target")
except Exception as e:      #to tell the user that i don't knoe the error you have to find it youreself
    print("mssage nhi h")

# cli_ based    #sender  #port limit 0-65536(0 to 65536)
#ip_address = 192.168.136.174
#port =8888