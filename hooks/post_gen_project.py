#!/usr/bin/env python3
from subprocess import CalledProcessError, check_call
from contextlib import suppress


def main() -> None:
    check_call(("make",))
    with suppress(CalledProcessError):
        check_call(("make", "remodel"))


if __name__ == "__main__":
    main()
