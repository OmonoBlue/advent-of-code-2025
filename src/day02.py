import os


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "../input/day02-1.txt")
    print(getInputs(file_path))


def getInputs(filename: str) -> list[tuple[str, str]]:
    inputs: list[tuple[str, str]] = []
    with open(filename) as file:
        inputs = [tuple(segment.split('-'))
                  for segment in file.readline().strip().split(',')]
    return inputs


if __name__ == "__main__":
    main()
