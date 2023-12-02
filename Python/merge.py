#TODO return a list of merged and sorted numbers in ascending order with no duplicates

list1 = [9,1,2,3,4,5,6]
list2 = [4,4,5,6,7,8,9]



def mergeArrays(arrayA, arrayB = [1,2,3]):
    return sorted(set(arrayA + arrayB))


merged = mergeArrays(list1, list2)

print(merged)

print(mergeArrays(merged) + list1)