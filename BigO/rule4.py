# Drop non-dominant terms.
# We should care of more important terms
# For example: O(n^2) is more important than O(n)

def pairSum(arr):

    # O(n)
    print("This are the numbers")
    for i in arr:
        print(i)

    # O(n^2)
    print("This are the sums:")
    for i in arr:
        for j in arr:
            print(i+j)

    # It is more important and impactful O(n^2) than O(n)
    # So we leave O(n^2)