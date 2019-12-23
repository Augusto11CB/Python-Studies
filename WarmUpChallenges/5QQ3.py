def solution(A):
    anwer = 0
    for i in range(0,(len(A)),2):
        for j in range (i+2, (len(A)),2):
            if(A[i] == A[j]):
                anwer = anwer + 1
    return anwer


if __name__ == '__main__':
    print(solution([5,4,-3,4,-3,5,-3,5]))