import struct
import socket


class Udp():
    def __init__(self, port: int, addr: str, msg_size=4096, client=False):  # client true if receiving
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        self._sock.setblocking(False)
        self._sock.settimeout(0.1)

        self._msg_size = msg_size
        self._addr = addr
        self._port = port
        self._af_inet_addr_pair = (self._addr, self._port)

        if client:
            try:
                self._sock.bind(self._af_inet_addr_pair)
            except Exception as e:
                raise e

    def __del__(self):
        self._sock.shutdown(socket.SHUT_RDWR)
        self._sock.close()

    def get_sock_addr(self):
        return self._af_inet_addr_pair

    def send(self, data: list):
        struct_out = struct.pack('!' + 'f' * len(data), *data)
        self._sock.sendto(struct_out, self._af_inet_addr_pair)

    def receive(self):
        struct_out, _ = self._sock.recvfrom(self._msg_size)
        if struct_out == None:
            return None
        size = int(len(struct_out) / struct.calcsize('f'))
        return list(struct.unpack('!' + 'f' * size, struct_out))



