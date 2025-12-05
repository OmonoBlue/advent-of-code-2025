import os


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "../input/day01-1.txt")
    part1(file_path)
    part2(file_path)


def getInputs(filename: str) -> list[tuple[str, int]]:
    inputs: list[tuple[str, int]] = []
    with open(filename) as file:
        inputs = [(line[0], int(line[1:].rstrip()))
                  for line in file.readlines()]
    return inputs


def part1(filename: str):
    inputs = getInputs(filename)
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


def part2(filename: str):
    inputs = getInputs(filename)
    dial: int = 50
    zero_count: int = 0
    for (direction, amount) in inputs:
        zero_count += amount // 100
        amount = amount % 100
        if direction == "L":
            dial -= amount
        else:
            dial += amount
        if dial < 0:
            if dial + amount != 0:
                zero_count += 1
            dial += 100
        elif dial > 99:
            zero_count += 1
            dial -= 100
        elif dial == 0:
            zero_count += 1
    print(zero_count)


if __name__ == "__main__":
    main()
