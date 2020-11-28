# Created by Larry Nkengbeza
# Created on November 2020
# This program calculates permieter of an equilateral triangle with user input


def main():
    # this function calculates perimeter
    # Input
    Length = int(input("Enter length of side a (cm): "))

    # Process
    perimeter = 3*Length

    # Output
    print("")
    print("perimeter is {}cm".format(perimeter))


if __name__ == "__main__":
    main()
