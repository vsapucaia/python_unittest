"""
Fizzbuzz robot rules:

1. if the number is multiple of 3: say fizz
2. if the number is multiple of 5: say buzz
3. if the number is multiple of 3 and 5: say fizzbuzz
4. if any other number: say the number

"""

from functools import partial


multiple_of = lambda base, num: num % base == 0
multiple_of_3 = partial(multiple_of, 3)
multiple_of_5 = partial(multiple_of, 5)


def robot(pos):
    say = str(pos)

    if multiple_of_3(pos) and multiple_of_5(pos):
        say = 'fizzbuzz'
    elif multiple_of_3(pos):
        say = 'fizz'
    elif multiple_of_5(pos):
        say = 'buzz'

    return say
