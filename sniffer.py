import socket
import struct



def main():
    connection = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

    while True:
        raw_data, address = connection.recvfrom(65536)
        destination_mac, source_mac, eth_protocol, data = ethernet_frame(raw_data)
        print('\nEthernet Frame: ')
        print('Destination: {}, Source: {}, Protocol: {}'.format(destination_mac, source_mac, eth_protocol))

#Break down the ethernet frame
def ethernet_frame(data):
    destination_mac = struct.unpack('! 6s', data[:6])
    source_mac = struct.unpack('! 6s', data[7:12])
    protocol = struct.unpack('! H', data[13:14])
    return get_mac_address(destination_mac), get_mac_address(source_mac), socket.htons(protocol), data[14:]

#Get human readable MAC address (AA:BB:CC:DD:EE:FF)
def get_mac_address(bytes):
    byte_str = map('{:02X}'.format, bytes)
    mac_address = ':'.join(byte_str)
    return mac_address

main()