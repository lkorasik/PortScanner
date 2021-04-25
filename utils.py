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
