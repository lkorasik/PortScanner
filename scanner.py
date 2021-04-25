import socket


def scan_tcp_port(port: int):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(0.01)

        result = sock.connect_ex(("127.0.0.1", port))

    return result == 0


def scan_tcp_range(ports: list):
    open_ports = []

    for port in ports:
        result = scan_tcp_port(port)
        if result:
            open_ports.append(port)

    return open_ports
