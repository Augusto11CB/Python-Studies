import sys


def main(argv):
    step = input()
    path = input()
    print(climb_mountain(path))


def climb_mountain(step_list=str):
    number_of_valley = 0
    number_of_down_up = 0

    for letter in step_list:
        print(letter)
        if (letter == "U"):
            number_of_down_up = number_of_down_up + 1
        if (letter == "D"):
            new_value = number_of_down_up - 1
            if (new_value == -1 and number_of_down_up == 0):
                number_of_valley = number_of_valley + 1
            number_of_down_up = new_value

    return number_of_valley


if __name__ == '__main__':
    main(sys.argv)
