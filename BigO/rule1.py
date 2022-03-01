#Worst Case Scenario 

def findNemo(arr):

    for i in arr:
        if i == "nemo":
            return "Found nemo!"

# We can find nemo on any index of the array so we say
# It is O(n) because we can find it on the end (n) of the array or at the start.
arr = ['a', 'a','a','a','a','a','a','a','a','nemo','a','a','a','a','a',]
print(findNemo(arr))