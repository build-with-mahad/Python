try:
    num = int(input("Enter a Number:"))
    print(10/num)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("That's not a Number!")
except Exception as e:
    print(f" An unexpected error Occured {e}")

try:
    print("Running Code")
except:
    print("Error Occured")
else: 
    print("No Error Found")
finally:
    print("Done!")

#Raising Exception
class InvalidAgeError(Exception):
    pass
try:
    age = int(input("Enter Your Age"))
    if age<0 :
        raise InvalidAgeError(f"Age cannot be Negative , {age}")
except InvalidAgeError as e:
    print(e) 