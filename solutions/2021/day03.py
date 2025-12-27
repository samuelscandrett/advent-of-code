def part_one(data):

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
            


def part_two():
    print("")