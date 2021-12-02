# Name: Quang Le
# Student ID: 1768324


if __name__ == "__main__":
    cup_juice = float(input("Enter amount of lemon juice (in cups):\n"))
    cup_water = float(input("Enter amount of water (in cups):\n"))
    cup_nectar = float(input("Enter amount of agave nectar (in cups):\n"))
    serv = float(input("How many servings does this make?\n"))
    print()
    print("Lemonade ingredients - yields {:.2f} servings".format(serv))
    print("{:.2f} cup(s) lemon juice".format(cup_juice))
    print("{:.2f} cup(s) water".format(cup_water))
    print("{:.2f} cup(s) agave nectar".format(cup_nectar))
    print()
    serv1 = float(input("How many servings would you like to make?\n"))
    cup_juice1 = serv1*0.333333
    cup_water1 = serv1 * 2.666666
    cup_nectar1 = serv1 * 0.416666
    print()
    print("Lemonade ingredients - yields {:.2f} servings".format(serv1))
    print("{:.2f} cup(s) lemon juice".format(cup_juice1))
    print("{:.2f} cup(s) water".format(cup_water1))
    print("{:.2f} cup(s) agave nectar".format(cup_nectar1))
    print()
    cup_juice2 = cup_juice1/16
    cup_water2 = cup_water1/16
    cup_nectar2 = cup_nectar1/16
    print("Lemonade ingredients - yields {:.2f} servings".format(serv1))
    print("{:.2f} gallon(s) lemon juice".format(cup_juice2))
    print("{:.2f} gallon(s) water".format(cup_water2))
    print("{:.2f} gallon(s) agave nectar".format(cup_nectar2))
