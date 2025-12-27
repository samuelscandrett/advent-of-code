import argparse
import importlib
import sys

def extract_from_file(file):
    """
    Extract challenge data from file
    """
    try:
        file_contents = []
        with open(file) as f:
            for line in f:
                if line != "\n":
                    file_contents.append(line.rstrip())
    except FileNotFoundError:
        print("File does not exist at that location")

    file_contents = [int(x) for x in file_contents]
    return file_contents


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Advent of Code solutions.")
    parser.add_argument("--year", "-y", type=int, help="Enter the year to run.")
    parser.add_argument("--day", "-d", type=int, help="Enter the day to run.")
    parser.add_argument("--example", "-e", action='store_true', help="Use the example input rather than main (optional).")
    args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])

    #TODO enforce year as 4 figs
    # add help to command run without args

    year = f"{args.year}"
    day = f"{args.day:02}"

    input_file = f"inputs/{year}/day{day}.txt"
    if args.example:
        input_file = f"inputs/{year}/day{day}_example.txt"

    input_data = extract_from_file(input_file)

    challenge_file_mod = f"solutions.{year}.day{day}"
    mod = importlib.import_module(challenge_file_mod)

    for i in ("partone", "parttwo"):
        if not hasattr(mod, i):
            print(f"Solution does not have a function named {i}")
            continue
        print(f"--- {i} ---")
        print(getattr(mod, i), input_data)