from concurrent.futures._base import as_completed
from concurrent.futures.thread import ThreadPoolExecutor

import utils
from arg_parser import ArgumentParser
from scanner import scan_tcp_port, scan_upd_port, scan_tcp_ports_parallel, \
    scan_udp_ports_parallel

tcp_key = "TCP"
udp_key = "UDP"


if __name__ == "__main__":
    parser = ArgumentParser()

    ports = utils.get_all_ports(parser.get_port(), parser.get_start_range(), parser.get_end_range())

    answer = dict()
    answer[tcp_key] = []
    answer[udp_key] = []

    if parser.get_tcp():
        answer[tcp_key] = scan_tcp_ports_parallel(ports)
    if parser.get_udp():
        answer[udp_key] = scan_udp_ports_parallel(ports)
    if not parser.get_tcp() and not parser.get_udp():
        answer[tcp_key] = scan_tcp_ports_parallel(ports)
        answer[udp_key] = scan_udp_ports_parallel(ports)

    answer[tcp_key] = sorted(answer[tcp_key])
    answer[udp_key] = sorted(answer[udp_key])
    if len(answer[tcp_key]) > 0 or len(answer[udp_key]) > 0:
        utils.print_header()
    for port in answer[tcp_key]:
        utils.print_open_tcp_port(port)
    for port in answer[udp_key]:
        utils.print_open_udp_port(port)
