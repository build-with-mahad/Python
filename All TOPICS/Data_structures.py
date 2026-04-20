#list are order and mutable
lst = [12,13,14,15,16]
print (lst)
lst[1:4] = [45,1]
print(lst , len(lst))
lst[3] = 56
print (lst)

print("****************")
#methods in list

lst.append(20)
print (lst)
lst.insert(0,10)
print(lst)
lst.remove(10)
print(lst)
lst.pop()
print(lst)
lst.sort()
print(lst)

print("****************")

for i in lst:
    print(i)
print("****************")

#tuple are ordered and immutable

tpl = ("karachi","islamabad","lahore")
print(tpl)
# tpl[0]="faislabad" -> this will throw an error bc tuples are immutable
# print(tpl)

#methods in Tuple

print(tpl.count("karachi"))
print(tpl.index("lahore"))

print("****************")

# Sets are unordered and unique

st = {1,3,2,4,5}
st1 = {4,6,1,7,3}
st.add(10)
print(st)
st1.remove(4)
print(st1)

#methods in sets 

print(st.union(st1))
print(st.intersection(st1))
print(st.difference(st1))

print("****************")

#dictionary 

details = {
    "product" : "Wheat",
    "price" : 120,
    "vendor" : "Imtiaz Super Market",
    "WholeSale Price" : 80,
    "Area" : "Korangi"
}
print(details)
print(details["product"])

details["InStock"] = True # add one more key and value
print(details)

print("****************")

#looping over dictionary
for key,value in details.items():
    print(key, ":" , value)

print("****************")

for key in details:
    print (key)
print("****************")

for value in details:
    print(details[value])
 