a = [1,2,3,4,5]
# O(n^2)
def pairs(a):
    for i in a:
        for j in a:
            print(i,j)

# Nested loops because for each term
# It will loop n times
# n * n