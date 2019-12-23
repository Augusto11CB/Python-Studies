def solution(T):
    second = int(T)
    my_minute, my_second = divmod(second, 60)
    my_hour, my_minute = divmod(my_minute, 60)
    print("{}h{}m{}s".format(my_hour, my_minute, my_second))

if __name__ == '__main__':
    solution("83643")