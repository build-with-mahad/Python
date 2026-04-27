# 1. Write a program that takes salary as input. Using conditional statements, calculate the final tax 
# based on the following rules:                                                                                        
# If the salary is less than 30,000 → Tax rate is 5%  
# If the salary is between 30,000 and 70,000 → Tax rate is 15%  
# If the salary is greater than 70,000 → Tax rate is 25%

salary = int(input("Enter your Salary for Calculating tax."))
if salary > 70000:
    print("Your Final Tax rate is 25%")
elif salary >= 30000 and salary <= 70000:
    print("Your Final Tax rate is 15%")
else:
    print("Your Final Tax rate is 5%")
    
# 2. Given a list of words: words = ["apple", "banana", "kiwi", "cherry", "mango"]           
# Create a dictionary that maps each word to its corresponding length. 
# Example Output: ({"apple": 5, "banana": 6, "kiwi": 4, "cherry": 6, "mango": 5})

lst = ["apple","banana","kiwi","cherry","mango"]
dct = {}
for word in lst:
    dct[word] = len(word)
print(dct)