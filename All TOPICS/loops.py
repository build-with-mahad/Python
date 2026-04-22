#for loop 

for i in range(3):
    print("Hello kids")
for char in "python":
    print(char)

#While loop 
count = 1
while count <=5:
    print (count)
    count+=1

#nested loops
for i in range (3):
    print("outer loop")

    for j in range (3):
        print("  inner loop")

i = 4
rows = i 
cols = i

matrix = []
for r in range(rows):
    row = []
    for c in range(cols):
        row.append(0)
    matrix.append(row)

for row in matrix:
    print(' '.join(map(str,row)))

#Looping over data structure - strings

count = 0
for char in "strawberry":
    if char == "r":
        count+=1
print(count)

#looping over data structure - dictionaries

dict = {
    "name" : "John dalton",
    "age" : 20,
    "city": "London"
}

for key in dict:
    print(key)

for value in dict:
    print(dict[value])

stud_lit = [
    { "name" : "Ali","grade":"3","age" : 12},
    { "name" : "sara","grade":"10","age" : 18}
]
for std in stud_lit:
    print(f"Name : {std.get('name', " ")} | Grade : {std.get("grade", " ")} | Age : {std.get("age", " ")}")
    