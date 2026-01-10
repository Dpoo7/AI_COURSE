
"""
file:
project:
Author:
Version:
Etc:
"""

#sequential datatypes

"""
    1.List - []
        - mutable
        - any datatye is supported

    2. Tuple - ()
        -immutable

    3. Set - {}
        - Stores only unique values

    4. Dictionary
        -mutable
        -{key: value}
"""

num = [1,2,3]

cart=["pc","book",10,False,None,{1:"a"},num]
print(cart)
cart[0]="phone"

print(cart)
print(type(cart))

marks = (55,66,22,77,88)
print(marks)

#marks[0] = 60
#print(marks)
print(type(marks))