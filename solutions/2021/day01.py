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

