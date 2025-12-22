import os
import readline

def extract_from_file():
    """
    Extract challenge data from file
    """

    # Set tab complete
    readline.set_completer_delims(' \t\n=')
    readline.parse_and_bind("tab: complete")
    text_file = ""

    while os.path.exists(text_file) == False:
        try:
            text_file = str(input("Specify puzzle file path: "))
            file_contents = []
            with open(text_file) as f:
                for line in f:
                    if line != "\n":
                        file_contents.append(line.rstrip())
        except FileNotFoundError:
            print("File does not exist at that location")

    file_contents = [int(x) for x in file_contents]
    return file_contents