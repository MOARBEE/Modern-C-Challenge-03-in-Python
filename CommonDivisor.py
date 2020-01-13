def getfirstnumber():
    return int(input("Enter the first positive integer: "))


def getsecondnumber():
    return int(input("Enter the second positive integer: "))


def calculations():
    num1 = getfirstnumber()
    num2 = getsecondnumber()
    if(num1 > num2):
        greatest = num1
    else:
        greatest = num2
    while(True):
        greatest += 1
        if(greatest % num1 == 0 and greatest % num2 == 0):
            lcm = greatest
            break
    print("The lowest common multiple is " + str(lcm))


if __name__ == "__main__":
    calculations()

