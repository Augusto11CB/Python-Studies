#
#
#
import sys

def main(argv):
    countries = ["Brazil", "Canada", "UK", "JAPAN", "USA", "MEXICO", "Brazil", "Canada", "UK", "JAPAN", "USA", "MEXICO",
                 "Brazil", "Canada", "UK", "JAPAN", "USA", "MEXICO"]
    countries_without_repetition = set(countries)
    countries_without_repetition
    print(countries_without_repetition)

    if("Japan" in countries):
        print("There is the string 'Japan' inside our set called countries")
    else:
        print("The could not find the string 'Japan' inside contries")

if __name__ == '__main__':
    main(sys.argv)


