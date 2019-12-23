def generate_list(clouds):
    my_list = clouds.split(" ")
    list_with_clouds = list(map(int, my_list))
    return list_with_clouds


def main():
    number_of_jump = input()
    clouds = input()
    list_of_clouds = generate_list(clouds)
    print(jump_through_cloud(int(number_of_jump), list_of_clouds))


def jump_through_cloud(number_of_clouds, type_of_cloud=list()):
    number_of_jumps = 0
    my_turn = 0
    while (my_turn < number_of_clouds -1 ):
        if (((my_turn + 2) <  number_of_clouds) and type_of_cloud[my_turn + 2] == 0):
            my_turn = my_turn + 2
            number_of_jumps = number_of_jumps + 1

        else:
            my_turn = my_turn + 1
            number_of_jumps = number_of_jumps + 1

    return number_of_jumps


#

if __name__ == '__main__':
    main()
