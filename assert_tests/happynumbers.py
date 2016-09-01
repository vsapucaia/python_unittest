"""
A number is considered happy when:
1. Given a specific integer number
2. Replace the number with the sum of the square of its digits. 47 = 4² + 7²
3. If it ends resulting 1, the number is happy
4. If not, repeat the process indefinitely

1, 7, 10, 13, 19: happy
"""


def happy_number(number):
    next_ = sum([int(char) ** 2 for char in str(number)])
    return number in (1, 7) if number < 10 else happy_number(next_)


if __name__ == '__main__':
    for n in range(200):
        print(str(n) + ': ' + ('happy' if happy_number(n) else 'not happy'))

