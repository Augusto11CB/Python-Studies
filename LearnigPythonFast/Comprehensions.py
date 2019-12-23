class Comprehensions():
    names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

    first_names = [name.split(" ")[0].lower() for name in names]
    print(first_names)


class ComprehensionWithConditionals():
    """ we can also add conditionals to list comprehensions (listcomps) """
    squares = [x ** 2 for x in range(9) if x % 2 == 0]
    print(squares)

    squares2 = [x ** 2 if x % 2 == 0 else x + 3 for x in range(9)]
    print(squares2)

    scores = {
        "Rick Sanchez": 70,
        "Morty Smith": 35,
        "Summer Smith": 82,
        "Jerry Smith": 23,
        "Beth Smith": 98
    }

    passed = [name for name, score in scores.items() if score >= 65]
    print(passed)


if __name__ == '__main__':
    Comprehensions()
