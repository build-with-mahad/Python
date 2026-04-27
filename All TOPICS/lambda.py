add = lambda a,b : a+b
print(add(3,4))

double = lambda n: n*2
print(double(10))

lst = [1,2,3,4,5,6]
sqaures = list(map(lambda x: x*x,lst))
print(sqaures)

lst1 = [1,2,3,4,5,6,7]
get = list(filter(lambda x: x%2 != 0, lst1))
print(get)