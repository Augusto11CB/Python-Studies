class LearningForWithRangeMethod():
    cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
    capitalized_cities = []

    for city in cities:
        capitalized_cities.append(city.title())

    for number in range(0,50,10): #range(start, stop, factorToIncrease/Decrease the number)
        print(number)

if __name__ == '__main__':
    LearningForWithRangeMethod()