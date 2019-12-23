def main():
    string = input()
    repetition = input()
    if(only_a(string) == 0):
        print(repetition)
    print(bla(int(repetition), string))

def only_a(string:str):
    my_string = list(string.split("a"))
    try:
        my_string.remove("")
        if(my_string is None):
            return 0
    except:
        return len(my_string)
    return len(my_string)

def bla(repetition:int, string:str):
    my_list = list(string)
    is_there_a = my_list.count("a")
    if(is_there_a > 0):
        return round(my_list.count("a")*(repetition/len(string)))


if __name__ == '__main__':
    main()
