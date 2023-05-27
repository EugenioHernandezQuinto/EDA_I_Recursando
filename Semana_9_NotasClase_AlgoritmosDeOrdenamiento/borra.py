def swap(x, y):
    temp = x
    x = y
    y = temp

def selectionSort(arr, 5):
    for i in range (0, 4):
        minimum = i 

        for j in range (i+1, 5): 
            if arr[j] < arr[minimum]: 
                minimun = j

        if minimun != i:
            swap(arr[minimun], arr[i])
