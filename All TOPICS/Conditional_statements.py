score = int(input ("Enter Your score :"))

if score >= 90:
    print("Grade A+")
elif score >= 80:
    print("Grade A")
else:
    print("Try again!")

age = int(input ("Enter your age:"))
if age >= 18:
    country = input("Enter Your country:")
    if country == "pakistan":
        print("You can vote in pakistan:")
    else:
        print("You cannot vote in pakistan")
else:
    print("You cannot vote")

age1 = int(input("Enter your age :"))
country1 = input("Entry Your Country :").capitalize()
if age1 >= 8 and country1 == "Pakistan":
    print("Eligible Vote")
else:
    print("Not eligible vote")

marks = int(input("Enter your marks:"))

if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B")
else :
    print("Fail")
 