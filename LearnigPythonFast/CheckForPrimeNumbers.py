class CheckPrime():
    number = 73
    for n in range(2,number):
        if(number % n) == 0:
            print("This number is not prime")
            break
        if(n == (number - 1)):
            print("This number is prime!!!!")

if __name__ == '__main__':
    CheckPrime()