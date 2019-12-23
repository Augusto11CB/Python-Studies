from builtins import print



def main():
    string = input()
    repetition = input()
    if(only_a(string) == 0):
        print(repetition)
    else:
        print(count_letter_a(int(repetition),string))


def only_a(string:str):
    my_string = list(string.split("a"))
    try:
        my_string.remove("")
        if(my_string is None):
            return 0
    except:
        return len(my_string)
    return len(my_string)

def count_letter_a(repetition, my_string):
    my_list_letter = list(my_string)

    number_letter_a = 0
    full_repetition = repetition // len(my_string)
    range(full_repetition)
    for _ in range(full_repetition):
        number_letter_a = number_letter_a + my_list_letter.count("a")

    rest = repetition % len(my_string)
    for i in range(rest):
        if my_list_letter[i] == "a":
            number_letter_a = number_letter_a + 1;

    return  number_letter_a

if __name__ == '__main__':
    main()
