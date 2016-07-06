import datetime 

array = [50, 32, 2, 77, 25]

a = datetime.datetime.now()

def selection_sort(arr):
    changeling = 0
    while changeling < len(arr):
        for i in range(changeling, len(arr)):
            min = arr[changeling]
            if arr[i] < arr[changeling]:
                min = arr[i]
                arr[i] = arr[changeling]
                arr[changeling] = min
        changeling += 1
    return arr
    
print selection_sort(array)

b = datetime.datetime.now()

c = b - a

print c.microseconds