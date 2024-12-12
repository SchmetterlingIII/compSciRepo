#string manipulation with functions
full_name = input("Enter your full name, with spaces: ")
nameList= full_name.split()
initials = nameList[0][0].upper() + nameList[1][0].upper()

totalNoChar = len(nameList[0] + nameList[1])
print(f' Your initials are: {initials}\n Total number of characters (exluding spaces): {totalNoChar}')

choiceGiven = input("Would you like your name in reverse order: (Y/N)").upper()

if choiceGiven == 'Y':
    reverseName = full_name[::-1]
    print(reverseName)
else:
    print("Thank you")
