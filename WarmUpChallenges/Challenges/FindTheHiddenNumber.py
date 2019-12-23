def main():
    solution([1, 2, 3])

def solution(A):
    ordered_A = sorted(A)
    ordered_A = list(dict.fromkeys(ordered_A))
    print(ordered_A)
    for x in range(len(ordered_A)-1):
        number = ordered_A[x]
        print(str(number) + "number")
        next_number = ordered_A[x+1]
        if(number + 1 == next_number ):
            continue
        else:
            if(number + 1 > 0):
                print( number + 1 )


if __name__ == '__main__':
    main()