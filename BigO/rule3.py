# Different terms for inputs

# If we have 2 different inputs each one should be handled differently

def sumBoxes(boxes, boxes2):
    sum = 0
    sum2 = 0
    for i in boxes:
        sum += i

    for i in boxes2:
        sum2 += i


# The worst case of each is O(n)
# But boxes could be 5 and boxes 2 could be 10
# So boxes != boxes2 so O(n) != O(m)
# Big o should be O(n + m) 