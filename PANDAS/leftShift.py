msg = "hello world"


def print_message(fname, lname):
    print(msg, "and", fname, lname)


print_message("Paul", "Lentz")


def lastKid(kids):
    print("The last kid entered is " +  kids[len(kids) - 1])

def middleChild(kids):
    print("the middle child is " + kids[len(kids)-2])

def firstKid(kids):
    print("The first kid is " + kids[0] )

lentzs = ["Sharon", "Eric", "Paul"]

firstKid(lentzs)
lastKid(lentzs)
middleChild(lentzs)