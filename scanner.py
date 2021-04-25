import socket
from concurrent.futures._base import as_completed
from concurrent.futures.thread import ThreadPoolExecutor

import utils


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


def scan_tcp_ports_parallel(ports: list):
    answer = []

    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(scan_tcp_port, port): port for port in ports}
        for future in as_completed(futures):
            port = futures[future]
            try:
                is_open = future.result()
            except Exception as exc:
                utils.print_error(port, exc)
            else:
                if is_open:
                    answer.append(port)
                    # utils.print_open_tcp_port(port)

    return answer


def scan_udp_ports_parallel(ports: list):
    answer = []

    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(scan_upd_port, port): port for port in ports}
        for future in as_completed(futures):
            port = futures[future]
            try:
                is_open = future.result()
            except Exception as exc:
                utils.print_error(port, exc)
            else:
                if is_open:
                    answer.append(port)
                    # utils.print_open_udp_port(port)

    return answer
