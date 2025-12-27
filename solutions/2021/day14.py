def polymerisation(polymer_template, no_runs):
    count = 0
    while count < no_runs:
        print(count)
        new_template = ""
        for index, char in enumerate(polymer_template):
            char_in_two = polymer_template[index:index+2]
            if len(char_in_two) == 2:

                for k,v in conversion_dict.items():
                    if k == char_in_two:
                        
                        # Construct new string triplet with value inbetween two chars
                        constructed_string = char_in_two[0] + v + char_in_two[-1]

                        # Last char of the three will be the first of the next three
                        # so remove from any sets after first insertion
                        if len(new_template) < 3:
                            new_template += constructed_string
                        else:
                            new_template += constructed_string[1:]

        polymer_template = new_template
        count += 1

    return polymer_template


def abundance_counter(input_str):
    abund_dict = {}
    for char in input_str:
        if char not in abund_dict.keys():
            abund_dict[char] = 0
        abund_dict[char] += 1
    return abund_dict

# Extract from file
readline.set_completer_delims(' \t\n=')
readline.parse_and_bind("tab: complete")
text_file = ""
while os.path.exists(text_file) == False:
    try:
        text_file = str(input("Specify polymer information file path: "))
        file_contents = []
        with open(text_file) as f:
            for line in f:
                if line != "\n":
                    file_contents.append(line.rstrip())
    except FileNotFoundError:
        print("file does not exist at that location")
#text_file = "puzzle_text_files/day14_example.txt"


# Grab template from start of file
template = file_contents[0]

#remove polymer template from file contents list before transformation into dict
del file_contents[0]

conversion_dict = {}
for each in file_contents:
    all=each.split()
    conversion_dict[all[0]] = all[-1]

# Get number of runs from user
run_number = ""
while run_number is not int:
    try:
        run_number = int(input("Select number of runs: "))
        break
    except ValueError:
        print("That isn't a number, try again!")

# Run functions
resulting_template = polymerisation(template,run_number)
counter = abundance_counter(resulting_template)

# Find minimum key,val
minval = min(counter.values())
min_element = [k for k, v in counter.items() if v==minval]
# Find Max key,val
maxval = max(counter.values())
max_element = [k for k, v in counter.items() if v==maxval]

# Output info:
print("After %s runs the resulting string has a length of: %s" % (run_number, len(resulting_template)))
print("The most common element is %s, occurring %s times" % (max_element,maxval))
print("The least common element is %s, occurring %s times" % (min_element, minval))
print("%s - %s = %s" % (maxval, minval, (maxval-minval)))