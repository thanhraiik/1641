ten = input("Type your name: ")
tuoi = int(input("Type your age: "))
entrance = int(input("Type your entrance: "))

namhoc =[ 2023 - entrance ]

def info(ten, tuoi, namhoc):
    print("Your name is", ten, ", you are", tuoi, "years old, you are", namhoc, "year student at Greenwich.")

info(ten, tuoi, namhoc)