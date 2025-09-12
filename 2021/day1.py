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

file_contents = [int(x) for x in file_contents]

def partone(data):
    status_dict = {"Increased":0,
                   "Decreased":0,
                   "No change":0}

    for index, each in enumerate(data):
        if index != 0: # if it isnt the first as that cannot be compared
            previous = data[index-1]
            if int(each) > int(previous):
                status = "Increased"
                status_dict["Increased"] += 1
            elif int(each) < int(previous):
                status = "Decreased"
                status_dict["Decreased"] += 1
            elif int(each) == int(previous):
                status = "No change"
                status_dict["No change"] += 1
        else:
            status = "Not comparable"

        print(each, status)
    print(status_dict)


def parttwo(data):
    status_dict = {"Increased":0,
                   "Decreased":0,
                   "No change":0}
    
    frame_sum_list = []

    for index,each in enumerate(data):
        frames = data[index:index+3]
        # Create sum of 3 frames
        if len(frames) == 3:
            frame_sum = sum(frames)
            frame_sum_list.append(frame_sum)

    for index, each in enumerate(frame_sum_list):
        if index != 0: # if it isnt the first as that cannot be compared
            previous = frame_sum_list[index-1]
            if int(each) > int(previous):
                status = "Increased"
                status_dict["Increased"] += 1
            elif int(each) < int(previous):
                status = "Decreased"
                status_dict["Decreased"] += 1
            elif int(each) == int(previous):
                status = "No change"
                status_dict["No change"] += 1
        else:
            status = "Not comparable"

        print(each, status)
    print(status_dict)


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