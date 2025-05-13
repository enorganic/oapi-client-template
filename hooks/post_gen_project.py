from subprocess import check_call


def main() -> None:
    check_call(("make",))


if __name__ == "__main__":
    main()
