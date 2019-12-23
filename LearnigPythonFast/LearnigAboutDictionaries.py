class LearnigAboutDictionaries():
    empty_dict = dict()
    elements = {"hydrogen": 1, "helium": 2, "carbon": 6}
    print(elements.items())
    print(elements.keys())
    print("Added elements['lithium'] = 3")
    elements["lithium"] = 3
    print( elements)

# if we look up a value that isn't in the dictionary a KeyError occurs
# get() looks up values in a dictionary, but unlike looking up values with square brackets '[]', get() returns None

class LearnigAboutDictAndAnimals():
    animals = {'dogs': [20, 10, 15,"crazy big dog OMG", 32, 15], ('cat','lion'): [3, 4, 2, "it's work dude!@!", 2, 4], 'rabbits': [2, 3, 3],
               'fish': [0.3, 0.5, 0.8, 0.3, 1]}
    print(animals.get(('cat','lion'))[3])

if __name__ == '__main__':
    LearnigAboutDictionaries()
    LearnigAboutDictAndAnimals()
