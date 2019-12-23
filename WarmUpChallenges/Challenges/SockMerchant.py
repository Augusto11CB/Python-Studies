import sys


def building_a_set(colors):
    print("building_a_set")
    my_set = set()
    for color in colors:
        print(int(color))
        print(colors.count(color))
        my_set.add((color, colors.count(color)))
    return my_set


def generate_my_list(string_colors=""):
    numbers = string_colors.split(" ")
    print(numbers)
    list_with_colors = list(map(int, numbers))
    for i in list_with_colors:
        print(i)
    print(list_with_colors)
    return list_with_colors


def main(argv):
    number_of_socks = input("Type the number of socks")
    number_of_socks = int(number_of_socks)
    print(number_of_socks)

    colorsInput = input("Type the List with colors:")
    list_with_colors = generate_my_list(colorsInput)
    print(list_with_colors)

    set_with_colors = building_a_set(list_with_colors)

    print(set_with_colors)

    number_of_pairs = sock_merchant(7, set_with_colors)

    print("The number of pairs is:" + str(number_of_pairs))


def sock_merchant(number_socks, sock_colors=set()):
    number_of_pairs = 0
    for color, units in sock_colors:
        print(int(color))
        print(int(units))
        if (units != 0 and units % 2 == 0):
            number_of_pairs = number_of_pairs + (units / 2)
        else:
            units = units - 1
            if (units > 1):
                number_of_pairs = number_of_pairs + (units / 2)

    return number_of_pairs


if __name__ == '__main__':
    main(sys.argv)
