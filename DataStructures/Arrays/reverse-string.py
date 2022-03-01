## Create a function that reverses a string
## 'Hi my name is Andrei' should return:
## 'ierdnA si eman ym iH'

from re import L


def reverse(string):
    """
    Reverse String Method

    - Receives a string and reverses it.
    - Returns the reversed string if is it a string
    - If not it will return the same value

    >>> reverse('Tell me why')
    'yhw em lleT'
    """

    if type(string) == str and len(string) > 1:
        new_string = ''
        for i in range(len(string)-1, -1, -1):
            new_string += string[i]
        return new_string

    return string

if __name__=='__main__':
    import doctest
    doctest.testmod()

print(reverse('a'))
print(reverse('10001'))
print(reverse(1))
