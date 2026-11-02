#!/usr/bin/env python3
"""Send a desktop reminder to study programming."""

import subprocess
import sys


def main() -> int:
    try:
        result = subprocess.run(
            [
                "notify-send",
                "--app-name=Study reminder",
                "--urgency=normal",
                "Programming study time",
                "Take a few minutes to study programming.",
            ],
            check=False,
        )
    except FileNotFoundError:
        print("notify-send was not found; install libnotify.", file=sys.stderr)
        return 1

    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
