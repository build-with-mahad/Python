file = open("demo.txt","r")
print(file.read())
file.close()
file = open("demo.txt","w")
file.write("New file added More!")
file = open("demo.txt","a")
file.write("\nOne More File Added")
# print(file.read())
file.close()

with open ("demo.txt","r") as file:
    data = file.read()
    print(data)
with open ("missing.txt","r") as file:
    data = file.read()
    print(data)

try:
    with open("missing.txt","r") as fout:
        data = fout.read()
        print(data)
except FileNotFoundError:
    print("File Not found")

filename = "missing.txt"
name = "George Bailey"
age = 25

try:
    with open(filename,"r") as fout:
        print(fout.read())
except FileNotFoundError:
    with open(filename,"w") as fout:
        fout.write(f"hi my name is {name} and my age is {age}\n")
    with open(filename,"r") as fout:
        print(fout.read())


try:
    file = open("missing.txt","r") 
    print(file.read())
except FileNotFoundError:
    print("file Not found")

filename  = "missing.txt"
try:
    with open("missing.txt","r") as file:
        print(file.read())
except FileNotFoundError:
    with open("missing.txt","w") as file:
        file.write("This is a first paragraph")
    with open ("missing.txt","r") as file:
        print(file.read())
