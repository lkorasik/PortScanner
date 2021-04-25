import socket


def scan_tcp_port(port: int):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(0.01)

        result = sock.connect_ex(("127.0.0.1", port))

    return result == 0


def scan_upd_port(port: int):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.settimeout(0.01) # Maybe more???
        result = sock.connect_ex(("127.0.0.1", port))
        if result == 0:
            sock.send("Hello".encode("UTF-8"))
            try:
                sock.recvfrom(1024)
                return port
            except socket.timeout:
                return port
            except ConnectionResetError:
                return None
