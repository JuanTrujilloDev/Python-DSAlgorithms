# Space complexity of O(1) because it only uses i
# In the loop

def booo(n):
    for i in range(0, len(n)-1):
        print("Booo!")


booo([1,2,3,4,5])

# Consumes n space inside the array
# Depending what the number in n is.

def arrayOfHiNTimes(n):
    arr = []
    for i in range(0, n):
        arr.append('Hi!')
    
    return arr

print(arrayOfHiNTimes(5))