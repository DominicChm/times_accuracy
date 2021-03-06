import subprocess
import re


class Generator:
    enabled = False
    display_name = "R"

    @staticmethod
    def init_parser(parser):
        parser.add_argument('--R', action="store_true")

    @classmethod
    def init_args(cls, arg):
        cls.enabled = arg.R

    @staticmethod
    def process(case, dop):
        q, k, nu = case.q, case.k, case.v
        prc = subprocess.run(
            ['Rscript', 'generators/cdf/cdf_r.R', f'{q:.22f}', f'{k:.22f}',
             f'{nu:.22f}'],
            stdout=subprocess.PIPE,
            universal_newlines=True)

        # Parse the command line output, b/c why not.
        parts = re.split('\[|\]|"|,|\s', prc.stdout)
        parts = list(filter(None, parts))  # Filter blank fields
        return float(parts[1]), float(parts[2])
