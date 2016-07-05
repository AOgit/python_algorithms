
array = [6, 5, 3, 1, 8, 7, 2, 4]

def bubble_sort(arr):
    changeling = len(arr)-1
    while changeling > 0:
        for i in range(0, changeling):
            while arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
        changeling -= 1
    return arr 
    
print bubble_sort(array)