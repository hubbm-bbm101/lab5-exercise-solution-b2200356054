checkbox = []
email = str(input("enter an email\n "))
for letteret in email:
    if letteret == "@":
        checkbox.append(letteret)
        break
for letterdot in email:
    if letterdot == ".":
        checkbox.append(letterdot)
        break
if len(checkbox) < 2:
    print("this is not a valid email")
else:
    print("this is a valid email")