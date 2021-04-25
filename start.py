import utils
from arg_parser import ArgumentParser
from scanner import scan_tcp_range

if __name__ == "__main__":
    parser = ArgumentParser()

    ports = utils.get_all_ports(parser.get_port(), parser.get_start_range(), parser.get_end_range())

    print(scan_tcp_range(ports))
