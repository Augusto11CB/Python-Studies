import sys
''' Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.'''

def main():
    #string_a = input("Input String A: ")
    #string_b = input("Input String B: ")
    #print("String A ** {} ** and String B ** {} **".format(string_a, string_b))
    return buddyStrings2("ab", "ab")

def buddyStrings2(A: str, B: str) -> bool:

    if len(A) != len(B):
        return False

    len_string = len(A)
    list_string = list(A)
    for slot in range(len_string):
        print("change")
        for slot_to_change in range(len_string):
            if slot >= slot_to_change or list_string[slot] == list_string[slot_to_change]:
                continue;
            else:
                new_list_string = list_string.copy()
                new_list_string[slot_to_change] = list_string[slot]
                new_list_string[slot] = list_string[slot_to_change]
                new_string = "".join(new_list_string)
                print(new_string)
                if new_string == B:
                    return True
    if (len(set(A)) == 1 and len(set(B)) == 1) and set(A) == set(B):
        return True

    return False

def buddyStrings(A: str, B: str) -> bool:
    print("buddyStrings")

    set_of_a = set(A)
    set_of_b = set(B)

    if (len(A) != len(B) or ((len(set_of_a) > 1 and len(set_of_b)>1 and A == B ))):
        return False


    if(set_of_a == set_of_b):
        return True


    string_a_sorted = sorted(A)
    string_b_sorted = sorted(B)
    if (string_a_sorted == string_b_sorted):
        return True
    else:
        return False

if __name__ == '__main__':
    resp = main()
    print(resp)