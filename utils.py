def ports_range_to_list(start: int, end: int):
    ports = []
    for i in range(start, end + 1):
        if is_valid(i):
            ports.append(i)
    return ports


def get_all_ports(ports: list, start: int, end: int):
    all_ports = []

    for port in ports:
        if is_valid(port):
            all_ports.append(port)

    all_ports += ports_range_to_list(start, end)
    all_ports = sorted(all_ports)
    return list(set(all_ports))


def is_valid(port: int):
    return 0 <= port <= 65535


def print_header():
    print("IP\t\tPort\tProtocol")


def print_open_tcp_port(port: int):
    print("127.0.0.1\t" + str(port) + "\tTCP")


def print_open_udp_port(port: int):
    print("127.0.0.1\t" + str(port) + "\tUDP")


def print_error(port: int, exc):
    print(str(port) + "\n\t" + str(exc))
