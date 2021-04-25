from concurrent.futures._base import as_completed
from concurrent.futures.thread import ThreadPoolExecutor

import utils
from arg_parser import ArgumentParser
from scanner import scan_tcp_port, scan_upd_port


if __name__ == "__main__":
    parser = ArgumentParser()

    ports = utils.get_all_ports(parser.get_port(), parser.get_start_range(), parser.get_end_range())

    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(scan_tcp_port, port): port for port in ports}
        utils.print_header()
        for future in as_completed(futures):
            port = futures[future]
            try:
                is_open = future.result()
            except Exception as exc:
                utils.print_error(port, exc)
            else:
                if is_open:
                    utils.print_open_tcp_port(port)

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
                    utils.print_open_udp_port(port)
