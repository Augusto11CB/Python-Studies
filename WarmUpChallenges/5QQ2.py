import sys
def solution(A, K):
    max_num = max(A)
    string_max_num = str(max_num)
    max_len = len(string_max_num)
    my_out = buildLine(A,K,max_len)

    for line in my_out:

        #div = topAndDownConer(len(line)) + topAndDow(max_len) * int(K) + topAndDownConer(max_len)
        div = topAndDownConer(len(line))
        print(div)
        if my_out.index(line) == len(my_out) - 1:
            print(line)
            #print(topAndDownConer(max_len) + topAndDow(max_len) * len(line) + topAndDownConer(max_len))
            print(topAndDownConer(len(line)))
            continue

        print(line)


def buildLine(A,K,maxLen):
    my_out = list()
    rotation = 1
    temp_string = "|"
    for number in A:
        resultLen = maxLen - len(str(number))
        if rotation < K and A.index(number) != len(A) - 1:

            if rotation == 1:
                temp_string = temp_string  + " " * resultLen + str(number)
            else:
                temp_string = temp_string + "|" + " " * resultLen + str(number)
            rotation = rotation + 1
        else :
            if rotation == 1:
                temp_string = temp_string + " " * resultLen + str(number) +"|"
            else:
                temp_string = temp_string + "|" + " " * resultLen + str(number) +"|"
            my_out.append(temp_string)
            temp_string = "|"
            rotation = 1


    return my_out

def topAndDownConer(myLen):
    myLen = myLen -2
    tdc = "+" + "-" * myLen + "+"
    return tdc

def topAndDow(myLen):
    td = "-" * myLen
    return td



if __name__ == '__main__':
    #print(buildLine([1,2,44,5],2,2))
    print(solution([1,2,44,5],2))
