class LearningZip():

    cars = ["GOLF", "M3", "RS6", "911"]
    price = ["$27K", "$60K", "$63K", "$90K"]

    # zip returns an iterator that combines multiple iterables into one sequence of tuples
    car_and_prices = zip(cars, price)

    for car, price in car_and_prices:
        print("Car {} is {} dollars".format(car, price))

    some_list = [('a', 1), ('b', 2), ('c', 3)]
    letters, nums = zip(*some_list) # you can also unzip a list into tuples using an asterisk. (*)
    print(letters)

class LearningEnumerate():
    #enumerate is a built in function that returns an iterator of tuples containing indices and values of a list.
    # You'll often use this when you want the index along with each element of an iterable in a loop.
    cars = ["GOLF", "M3", "RS6", "911"]
    for i, car in enumerate(cars):
        print("My {} car will be {}".format(i+1,car))



if __name__ == '__main__':
    LearningEnumerate()