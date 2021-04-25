import argparse


class ArgumentParser:
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.description = "Сканер портов"

        parser.add_argument(
            "-r",
            "--range",
            help="Указать диапазон портов",
            nargs=2,
            dest="range",
            type=int,
            metavar=("START", "END")
        )
        parser.add_argument(
            "-p",
            "--port",
            help="Указать конкретные порты",
            dest="port",
            type=int,
            nargs="+",
            default=[]
        )

        self._args = parser.parse_args()

    def get_port(self):
        return self._args.port

    def get_start_range(self):
        if self._args.range is not None:
            v0 = self._args.range[0]
            v1 = self._args.range[1]
            return min(v0, v1)
        else:
            return -1

    def get_end_range(self):
        if self._args.range is not None:
            v0 = self._args.range[0]
            v1 = self._args.range[1]
            return max(v0, v1)
        else:
            return -1
