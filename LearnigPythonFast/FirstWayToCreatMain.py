import sys

def main(argv):
    my_name = ["Augusto","Calado","Bueno"]
    augusto_name = my_name
    augusto_name[0] = "Augustop"
    print(augusto_name)
    print(my_name)
# Beside the way to create a Main file, here we can see that when a list is assigned to a new variable, both the oldest
# and the newest share the same list object in memory

if __name__ == '__main__':
    main(sys.argv)