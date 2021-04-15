NAME_LIST = ["Alice", "Bob", "Jeremy", "Sam", "Sarah", "Ashley"]


def arrayPrint():
    print("Prints Array list")
    # using for loop
    for name in NAME_LIST:
        print(f'Hello my name is {name} \n')


def arrayIntervalPrint():
    i = 0
    print("Prints Array with 2 step interval")
    # using while loop printing name with 2 step interval
    while(i < len(NAME_LIST)):
        print(NAME_LIST[i], end="\n")
        i += 2


def arrayPrintReverse():
    reversed_list = NAME_LIST[::-1]
    print("Prints Reversed Array list")
    for name in reversed_list:
        print(name)


def arrayPrintLast():
    print("Prints last element in Array list")
    print(NAME_LIST[len(NAME_LIST) - 1])


arrayPrint()
arrayIntervalPrint()
arrayPrintReverse()
arrayPrintLast()
