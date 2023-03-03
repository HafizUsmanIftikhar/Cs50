# Implements a phone book

# from cs50 import get_string

people = {
    "Carter": "+1-617-495-1000",
    "David": "+1-949-468-2750"
}


# Search for name
name = input("Name: ")
if name in people:
    print(f"Number: {people[name]}")



# for k,v in people.items():
#     print("key= {},Value ={}".format(k,v))
# print(people["David"])
