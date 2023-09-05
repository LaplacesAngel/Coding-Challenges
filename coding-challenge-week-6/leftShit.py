msg = "hello world"


def print_message(fname, lname):
    print(msg, "and", fname, lname)


print_message("Paul", "Lentz")


def countKids(*kids):
    print("The last kid entered is " + kids[len(kids) - 1])


countKids("Paul", "Eric", "Sharon")
