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

    fwd_list = []
    up_list = []
    down_list = []
    instructions = {'forward':fwd_list,
                    'up':up_list, 
                    'down':down_list}

    # Change into dict for forward up and down
    for contents in data:
        both = contents.split()
        if both[-1]:
            for instruction, destination_list in instructions.items():
                if both[0] == instruction:
                    destination_list.append(int(both[-1]))

    # the foward represents horizontal position and added together
    # the down represents depth and is added 
    # the up also represents depth and is subtracted to decrease depth
    # Multiply horizontal and depth to get answer

    horizontal = sum(fwd_list)
    depth = (sum(down_list) - sum(up_list))
    puzzle_ans = horizontal * depth
    print("Depth = %s" % (depth))
    print("Horizontal = %s" % (horizontal))
    print("Depth x horizontal = %s" % (puzzle_ans))


def parttwo(data):
#     # down X increases your aim by X units.
#     # up X decreases your aim by X units.
#     # forward X does two things:
#     # It increases your horizontal position by X units.
#     # It increases your depth by your aim multiplied by X.

#     # FILE ORDER MATTERS
    horizontal = 0
    depth = 0
    aim = 0

    for contents in file_contents:
        both = contents.split()
        if both[0] == 'forward':
            horizontal += int(both[-1])
            if aim != 0:
                depth += int(both[-1]) * aim 

        elif both[0] == 'down':
            aim += int(both[-1])

        elif both[0] == 'up':
            aim -= int(both[-1])


    puzzle_ans = horizontal * depth
    print("Depth = %s" % (depth))
    print("Horizontal = %s" % (horizontal))
    print("Depth x horizontal = %s" % (puzzle_ans))


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