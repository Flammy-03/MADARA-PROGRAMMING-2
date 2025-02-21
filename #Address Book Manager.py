#Address Book Manager
#The user can input atleast 3 contacts
#The array that you should use is a nested dictionary

#Bonus if you would use a function


address_book = {}

def add_person_info():

    name = input("Enter Name: ")
    number = int(input("Enter Number: "))

    address_book[name] = {number}

for i in range(3):
    add_person_info()

print(f"{address_book}")

for name, info in address_book.items():
    print (f"Name: {name} : Phone number: {info} ")

lookup = input("Lookup Name: ")

if lookup in address_book:
    print (f"Number: {address_book[lookup]}")
else:
    print ("Contact does not exist.")
