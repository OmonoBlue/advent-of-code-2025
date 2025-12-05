
def main():
    part1("../input/day01-1.txt")


def part1(filename: str):
    inputs: list[tuple[str, int]] = []
    with open(filename) as file:
        inputs = [(line[0], int(line[1:].rstrip()))
                  for line in file.readlines()]
    dial: int = 50
    zero_count: int = 0
    for (direction, amount) in inputs:
        amount = amount % 100
        if direction == "L":
            dial -= amount
            while dial < 0:
                dial = dial + 100
        else:
            dial += amount
            dial = dial % 100
        if dial == 0:
            zero_count += 1
    print(zero_count)


if __name__ == "__main__":
    main()
