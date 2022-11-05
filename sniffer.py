import socket

# Get HOST IP address
HOST = socket.gethostbyname(socket.gethostname())

def main():
    # Create a raw socket and bind to it
    connection = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    connection.bind((HOST, 0))

    # Include IP Header
    connection.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    # Promiscuous Mode ON for all packets
    connection.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    print('Please enter the ammount of packets to be sniffed:\n')
    count = 0
    target = input()
    target = int(target)

    while count < target:
        buffer = connection.recvfrom(65565)
        print('\n')
        print(buffer)
        print('\n')
        count += 1
        
    # Promiscuous Mode OFF
    connection.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
    
main()