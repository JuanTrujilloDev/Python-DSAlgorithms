# Remove constants


def sumPairsAnd100(arr):

    # We should remove constant time on the Big O

    for i in arr:
        for j in arr:
            print(i+j)
    
    # This loop is constant so we remove it
    for i in range(0,100):
        print(i)


# O(n + 100) should be O(n)