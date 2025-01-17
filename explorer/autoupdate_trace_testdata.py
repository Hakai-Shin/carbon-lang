#!/usr/bin/env python3

"""Updates the CHECK: lines in tests with an AUTOUPDATE line."""

__copyright__ = """
Part of the Carbon Language project, under the Apache License v2.0 with LLVM
Exceptions. See /LICENSE for license information.
SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
"""

import subprocess
import sys
from pathlib import Path


def main() -> None:
    # Subprocess to the main script in order to avoid Python import behaviors.
    this_py = Path(__file__).resolve()
    autoupdate_py = this_py.parent.parent.joinpath(
        "testing", "scripts", "autoupdate_testdata_base.py"
    )

    args = [
        str(autoupdate_py),
        # Flags to configure for explorer testing.
        "--tool=explorer",
        "--testdata=explorer/trace_testdata",
        "--autoupdate_arg=--trace_file=-",
        "--autoupdate_arg=-trace_phase=all",
        "--extra_check_replacement",
        r".+Time elapsed in (\S+): (\d+)ms",
        r"Time elapsed in (\S+): (\d+)ms",
        r"Time elapsed in \1: {{[0-9]+}}ms",
        # Do not perform line number replacement.
        "--line_number_pattern",
        "(?!)",
    ] + sys.argv[1:]
    exit(subprocess.call(args))


if __name__ == "__main__":
    main()
