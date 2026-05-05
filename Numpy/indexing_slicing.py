import numpy as np
import time
arr = np.array([[10,20,30],
                [40,50,60],
                [70,80,90],
                [100,110,120],
                [130,140,150]])

print(arr[3,2])
print(arr[4,1])

print(arr[-3,-2])
print(arr[-5,-3])

print(arr[0:4,0:3])
print(arr[1:3,1:2])

print(arr[::2,::2])
print(arr[::3,::2])

slice_arr = arr[0]
slice_arr[0] = 100
print(arr[0])

copy = arr[3].copy()
copy[2] = 550
print(copy)