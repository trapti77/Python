password=input("Enter Password : ")

pl=len(password)

if pl<=6:
    print("week")
elif pl>=8 and pl<=10:
    print("medium")
else:
    print("strong")