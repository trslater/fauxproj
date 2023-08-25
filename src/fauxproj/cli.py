import sys
import textwrap

import numpy as np

USAGE = textwrap.dedent("""\
    Usage: fauxproj N

        Returns the square root of N""")


def run():
    if len(sys.argv) < 2:
        print(USAGE)
        exit(1)

    try:
        n = float(sys.argv[1])

    except ValueError:
        print("ERROR: N must be a number", file=sys.stderr)
        print()
        print(USAGE)
        exit(1)

    if n < 0:
        print("ERROR: N non-negative", file=sys.stderr)
        print()
        print(USAGE)
        exit(1)

    print(np.sqrt(n))
