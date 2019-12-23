class LearningAboutIfElifElse():
    season = input("Enter with the season: ")

    if season == 'spring':
        print('plant the garden!')
    elif season == 'summer':
        print('water the garden!')
    elif season == 'fall':
        print('harvest the garden!')
    elif season == 'winter':
        print('stay indoors!')
    else:
        print('unrecognized season')

    is_cold = False
    if not is_cold:  ## is_cold == False
        print("Hmm it seems that is a little hot today, isn't it?")


class TruthValueTesting():
    # If we use a non-boolean object as a condition in an if statement in place of the boolean expression, Python will check for its truth value
    # By default, the truth value of an object in Python is considered True unless specified as False in the documentation.

    errors = 3
    if errors:
        print("You have {} errors to fix!".format(errors))
    else:
        print("No errors to fix!")


if __name__ == '__main__':
    LearningAboutIfElifElse()
