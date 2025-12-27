import sys
import os
import readline

# Extract from file
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


def partone(data):

    n = 0
    index = 0
    gamma_string = ""
    epsilon_string = ""
    while n < len(data) * len(data[0]):
        zero_count = 0
        one_count = 0
        for numbers in data:
            if numbers[index] == '1':
                one_count += 1
            elif numbers[index] == '0':
                zero_count += 1
            n += 1
        if one_count > zero_count:
            gamma_string += "1"
            epsilon_string += "0"
        else:
            gamma_string += "0"
            epsilon_string += "1"

        index += 1

    gamma_decimal = int(gamma_string, 2)
    epsilon_decimal = int(epsilon_string, 2)
    partone_ans = gamma_decimal * epsilon_decimal

    print("The gamma string: %s, the gamma decimal: %s" % (gamma_string, gamma_decimal))
    print("The epsilon string: %s, the epsilon decimal: %s" % (epsilon_string, epsilon_decimal))
    print("Part one answer - %s x %s = %s" % (gamma_decimal, epsilon_decimal, partone_ans))
            


def parttwo():
    print("")


# Get user part to execute
part_number = ""
while part_number is not int:
    try:
        while part_number != 1 or part_number != 2:
            run_number = int(input("Select which part to run: "))
            if run_number == 1:
                partone(file_contents)
                break
            if run_number == 2:
                parttwo(file_contents)
                break
            print("There are only two parts!")
        
        break
    except ValueError:
        print("That isn't a number, try again!")

