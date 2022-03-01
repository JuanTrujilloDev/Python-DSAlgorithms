# Given 2 sorted arrays: [1,2,3] - [2,3,4,5]
# Return merged sorted array [1,2,2,3,3,4,5]

def mergeSorted(array1, array2):
    '''
    
    '''
   
    i = 0
    j = 0
    l = []
    ended = 0
    while i < len(array1) and j < len(array2):

        if array1[i] <= array2[j]:
            l.append(array1[i])
            i+=1
        else:
            l.append(array2[j])
            j+=1

        if i == len(array1):
            ended = 1

    if ended == 1:
        for index in range(j, len(array2)):
            l.append(array2[index])

    else:
        for index in range(i, len(array1)):
            l.append(array1[index])

    return l


        

print(mergeSorted([2,3,5, 7], [3,4,5, 9, 10]))
