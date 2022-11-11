def insertionSort(arr):
    # Traverse through 1 to len(arr)
    print("insertion sort")
    for i in range(0, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
        print(arr)
    return


class MS:
    def __init__(self) -> None:    
        print("merge sort")
    def mergeSort(self, arr) -> list:
        if len(arr) > 1:
            mid = len(arr) // 2
    
            L = arr[:mid]
            R = arr[mid:]
    
            self.mergeSort(L)
            self.mergeSort(R)
    
            i = j = k = 0
    
            # compare two array, and save the values to tmp array
            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
    
            # check remaining elements
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
    
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
            print(arr)



if __name__ == '__main__':
    arr = [7,1,5,8,3,6,10,9,11]
    # run insertion sort
    insertionSort(arr)

    # run merge sort
    MS().mergeSort(arr)