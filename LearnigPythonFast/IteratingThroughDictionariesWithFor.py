class IteratingThroughDictionariesWithFor():
    cast = {
        "Jerry Seinfeld": "Jerry Seinfeld",
        "Julia Louis-Dreyfus": "Elaine Benes",
        "Jason Alexander": "George Costanza",
        "Michael Richards": "Cosmo Kramer"
    }

    for key, value in cast.items():
        print("Actor: {}    Role: {}".format(key, value))

    students = {
        "Augusto": {
            "usp_number":"9779112",
            "subjects": "IA"
        },
        "Calado": {
            "usp_number":"9779112",
            "subjects": "AED"
        }
    }


    for key, value in students.items():
        print(key)
        print(value)
        print("Student:{}  USP Number:{} ".format(key, value.get("usp_number")))


if __name__ == '__main__':
    IteratingThroughDictionariesWithFor()
