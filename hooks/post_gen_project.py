from subprocess import check_call


def main() -> None:
    data: str
    with open("scripts/remodel.py") as file:
        data = file.read()
    with open("scripts/remodel.py", "w") as file:
        file.write(data.replace("  # --\n", "\n"))
    check_call(("make",))
    check_call(("hatch", "fmt", "--formatter"))


if __name__ == "__main__":
    main()
