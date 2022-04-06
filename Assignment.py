# Shermaine Peh
# BA201
dict = {}


def addcont():
    contact = {}
    global hobbieslist
    hobbieslist = []
    print("Add contact:")
    name = input("Please enter the contact name:")
    contact['name'] = name
    address = input("Please enter the contact's address:")
    contact['address'] = address
    mobile = input("Please enter the contact's mobile number:")
    contact['mobile'] = mobile
    while True:
        hobbies = input("Please enter hobby(Enter 'end' to stop adding):")
        if hobbies == 'end':
            break
        else:
            hobbieslist.append(hobbies)
            contact['hobbies'] = hobbieslist
    print("Contact added!\n")
    dict[name] = contact
    global numcontact
    numcontact += 1
    main()


def searchcont():
    print("Search contact:\nSearch By:\n1. Name\n2. Contact number\n3. Hobbies\n0. Return to main menu")
    choice = int(input("Your choice:"))

    if choice == 1:
        name = input("Please enter the name you wish to search by:")
        if name in dict:
            print("\nContact details:")
            print("Name: ", name)
            print("Address: ", dict[name]['address'])
            print("Mobile Number: ", dict[name]['mobile'])
            print("Hobbies: ", dict[name]['hobbies'])
            print('\n')
            searchcont()
        else:
            print("Contact not found!\n")
            print("\n")
            searchcont()
    elif choice == 2:
        mobile = input("Please enter the contact you wish to search by:")
        for x in dict:
            if dict[x]['mobile'] == mobile:
                print("\nContact details:")
                print("Name: ", dict[x]['name'])
                print("Address: ", dict[x]['address'])
                print("Mobile Number: ", dict[x]['mobile'])
                print("Hobbies: ", dict[x]['hobbies'])
                print('\n')
                searchcont()
        else:
            print('No contact with this number found!')
            searchcont()
            print("\n")

    elif choice == 3:
        cleared = 0
        counter = 0
        hobbies = input("Please enter the hobby you wish to search by:")
        for x in dict:
            counter += 1
            if hobbies in dict[x]['hobbies']:
                print("\nContact details:")
                print("Name: ", x)
                print("Address: ", dict[x]['address'])
                print("Mobile Number: ", dict[x]['mobile'])
                print("Hobbies: ", dict[x]['hobbies'])
                print('\n')
                cleared += 1
                continue
            elif cleared == 0 and counter == numcontact:
                print("No contact with this hobby found.")
                print("\n")
                break
            else:
                continue
        searchcont()
    elif choice == 0:
        main()
    else:
        print('Please enter a valid number')


def display():
    print("Display all contacts:\n")
    for x in dict:
        print("Contact details:")
        print("Name: ", x)
        print("Address: ", dict[x]['address'])
        print("Mobile Number: ", dict[x]['mobile'])
        print("Hobbies: ", dict[x]['hobbies'])
        print("\n")


def update():
    print('Update Contact:')
    name = input('Please enter the name of the contact you would like to update:')
    if name in dict:
        print("\nContact details:")
        print("Name: ", name)
        print("Address: ", dict[name]['address'])
        print("Mobile Number: ", dict[name]['mobile'])
        print("Hobbies: ", dict[name]['hobbies'])
        print('Contact Exist:\n1. Address\n2. Contact no\n3. Hobbies\n0. Exit')
        updateask = int(input('What would you like to update?'))
        if updateask == 1:
            address = input('Enter the new address:')
            dict[name]['address'] = address
            print('Address updated!\n')
        elif updateask == 2:
            mobile = input('Enter the new mobile number:')
            dict[name]['mobile'] = mobile
            print('Mobile Number updated!\n')
        elif updateask == 3:
            hobbieslist.clear()
            while True:
                hobbies = input("Please enter hobby(Enter 'end' to stop adding):")
                if hobbies == 'end':
                    print('Hobbies updated!\n')
                    break
                else:
                    hobbieslist.append(hobbies)
                    dict[name]['hobbies'] = hobbieslist
        elif updateask == 0:
            main()
    else:
        print('No such contact found.\n')


def remove():
    print('Remove Contact:')
    name = input('Please enter the contact name you want to remove:')
    if name in dict:
        print("\nContact details:")
        print("Name: ", name)
        print("Address: ", dict[name]['address'])
        print("Mobile Number: ", dict[name]['mobile'])
        print("Hobbies: ", dict[name]['hobbies'])
        deleteask = input('Is this the contact you want to remove? (Yes/No)')
        if deleteask.capitalize() == 'No':
            print('Contact was not removed!\n')
            main()
        elif deleteask.capitalize() == 'Yes':
            dict.pop(name)
            print('Contact removed!\n')
            global numcontact
            numcontact -= 1
            main()
        else:
            print('Please input only Yes or No')
    else:
        print('No such contact found.\n')


def main():
    while True:
        print("Welcome to My Phone Directory:")
        print("Number of contact in your directory:", numcontact)
        print("These are the functions available:")
        print("1. Add new contact\n2. Search for contact\n3. Display all contact details in directory\n4. Update existing contact details\n5. Remove existing contact\n0. Exit program")
        select = int(input("Your selection please:"))
        if select == 1:
            addcont()
        elif select == 2:
            if numcontact == 0:
                print("That selection is not valid as your contact list is empty")
            else:
                searchcont()
        elif select == 3:
            if numcontact == 0:
                print("That selection is not valid as your contact list is empty")
            else:
                display()
        elif select == 4:
            if numcontact == 0:
                print("That selection is not valid as your contact list is empty")
            else:
                update()
        elif select == 5:
            if numcontact == 0:
                print("That selection is not valid as your contact list is empty")
            else:
                remove()
        elif select == 0:
            exit()
        else:
            print('Please enter valid numbers only')


numcontact = 0
main()
