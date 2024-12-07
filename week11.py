

def listInit():
    n = 1000
    lst = []
    while n > 0:
        lst.append(n)
        n -= 1
    return lst


def list100():
    lst = []
    for i in range(99, 0, -2):
        lst.append(i)
    return lst


def listOfSquares():
    n = int(input('enter the number: '))
    lst = []
    for i in range(1, n+1):
        lst.append(i**2)
    return lst


def isReverse(s1, s2):
    return s1 == s2[::-1]


def sorted(l1):
    l1 = l1[:]

    for i in range(len(l1)):
        for j in range(len(l1) - i - 1):
            if l1[j] > l1[j + 1]:
                l1[j], l1[j + 1] = l1[j + 1], l1[j]

    return l1


def listOfOddandEvenNumbers(l1):
    odd_numbers = sorted([num for num in l1 if num % 2 != 0])
    even_numbers = sorted([num for num in l1 if num % 2 == 0])
    return odd_numbers, even_numbers


def theLargestElement(l1):
    max_value = l1[0]
    for i in l1:
        if i > max_value:
            max_value = i
    return max_value


def reverseList(l1):
    return l1[::-1]


def checkOccurrence(l1, occurrence):
    return occurrence in l1


def elementsOnOdd(l1):
    l2 = []
    for i in range(len(l1)):
        if i % 2 != 0:
            l2.append(l1[i])
    return l2


def theSumOfNumbers1(l1):
    return sum(l1)


def theSumOfNumbers2(l1):
    s = 0
    for i in l1:
        s += i
    return s


def theSumOfNumbers3(l1):
    s = 0
    i = 0
    while i < len(l1):
        s += l1[i]
        i += 1
    return s


def concetenateTwoLists(l1, l2):
    return l1 + l2


def runningTotal(l1):
    total = 0
    result = []
    for num in l1:
        total += num
        result.append(total)
    return result


def on_all(function, elements):
    return [function(element) for element in elements]


def square(x):
    return x * x


def onAll():
    l1 = list(range(1, 21))
    perfect_squares = on_all(square, l1)
    print('Perfect squares:', perfect_squares)


def combine(l1, l2):
    res = []
    i = 0
    while i < (min(len(l1), len(l2))):
        res.append(l1[i] + l2[i])
        i += 1
    while i < len(l1):
        res.append(l1[i])
        i += 1
    while i < len(l2):
        res.append(l2[i])
        i += 1

    return res


def merge(l1, l2):
    merged = []
    while l1 and l2:
        if l1[0] < l2[0]:
            merged.append(l1.pop(0))
        else:
            merged.append(l2.pop(0))
    return merged


def rotate(l1, r):
    r %= len(l1)
    for i in range(r):
        l1.append(l1.pop(0))
    return l1


def compute():
    fib = []
    a, b = 0, 1
    while len(fib) < 100:
        fib.append(a)
        a, b = b, a + b
    return fib


def listOfDigits(n):
    return [int(digit) for digit in str(n)]


def avoids(word, forbidden):
    for letter in forbidden:
        if letter in word:
            return False

    return True


def main():
    print('List initialization:')
    print(listInit())

    print('\nList of first 100 odd numbers:')
    print(list100())

    print('\nList of squares:')
    print(listOfSquares())

    print('\nCheck if two strings are reverse of each other:')
    s1 = 'hello'
    s2 = 'olleh'
    print(isReverse(s1, s2))

    print('\nSort a list:')
    l1 = [4, 2, 9, 1, 5]
    print(sorted(l1))

    print('\nList of odd and even numbers:')
    odd_numbers, even_numbers = listOfOddandEvenNumbers(l1)
    print('Odd numbers:', odd_numbers)
    print('Even numbers:', even_numbers)

    print('\nThe largest element in the list:')
    print(theLargestElement(l1))

    print('\nReverse a list:')
    print(reverseList(l1))

    print('\nCheck if an element occurs in the list:')
    occurrence = 5
    print(checkOccurrence(l1, occurrence))

    print('\nElements on odd indices:')
    print(elementsOnOdd(l1))

    print('\nThe sum of numbers in the list using sum function:')
    print(theSumOfNumbers1(l1))

    print('\nThe sum of numbers in the list using a for loop:')
    print(theSumOfNumbers2(l1))

    print('\nThe sum of numbers in the list using a while loop:')
    print(theSumOfNumbers3(l1))

    print('\nConcatenate two lists:')
    l2 = [7, 8, 9]
    print(concetenateTwoLists(l1, l2))

    print('\nRunning total of numbers in the list:')
    print(runningTotal(l1))

    print('\nUsing on_all function to square all numbers in the list:')
    onAll()

    print('\nCombine two lists:')
    print(combine(l1, l2))

    print('\nMerge two sorted lists:')
    print(merge(l1, l2))

    print('\nRotate a list by a given number:')
    rotated = rotate(l1, 2)
    print('Rotated list:', rotated)

    print('\nGenerate a list of first 100 Fibonacci numbers:')
    print(compute())

    print('\nList of digits in a given number:')
    n = 12345
    print('Digits:', listOfDigits(n))

    print('\nCheck if a word avoids a given list of forbidden letters:')
    word = 'apple'
    forbidden = ['p', 'l']
    print(avoids(word, forbidden))


if __name__ == '__main__':
    main()
