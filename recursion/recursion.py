"""
Recursion:
    - Recursion is a common mathematical and programming concept.
    - In programming, it refers to a coding technique in which a function calls itself.
    - This has the benefit of meaning that you can loop through data to reach a result.
"""

# 1) Count down to 0
def countdown_loop(n):
    for i in range(n, -1, -1):
        print(i)

def countdown_recur(n):
    if n < 0:
        return
    elif n == 0:
        print(0)
    else:
        print(n)
        countdown_recur(n - 1)

# test
# countdown_loop(5)
# countdown_loop(0)
# countdown_loop(-1)
# countdown_recur(5)
# countdown_recur(0)
# countdown_recur(-1)


# 2) Calculate factorial of natural number (inc. 0)
def factorial_loop(n):
    res = 1
    for i in range(2, n + 1):
        res = res * i

    return res

def factorial_recur(n):
    if n <= 1: # 0 or 1
        return 1
    else:
        return n * factorial_recur(n - 1)

# test
# print(factorial_loop(0))
# print(factorial_loop(1))
# print(factorial_loop(5))
# print(factorial_recur(0))
# print(factorial_recur(1))
# print(factorial_recur(5))


# 3) Fibonacci sequence
#    Find nth (from 0) number in fibonacci sequence
def fibonacci_loop(n):
    if (n == 0):
        return 0
    if (n == 1):
        return 1

    n1 = 0
    n2 = 1
    nth = 0
    for i in range(2, n + 1):
        nth = n1 + n2
        n1 = n2
        n2 = nth

    return nth
    
def fibonacci_recur(n):
    if (n == 0 or n == 1):
        return n
    
    return fibonacci_recur(n - 1) + fibonacci_recur(n - 2)

# test
# print(fibonacci_loop(0))
# print(fibonacci_loop(1))
# print(fibonacci_loop(3))
# print(fibonacci_loop(10))
# print(fibonacci_recur(0))
# print(fibonacci_recur(1))
# print(fibonacci_recur(3))
# print(fibonacci_recur(10))
    

# 4) Detect palindromes
def is_palindrome_loop(word):
    for i in range(len(word) // 2):
        if (word[i] != word[len(word) - i - 1]):
            return False
    return True

def is_palindrome_recur(word):
    if len(word) <= 1:
        return True
    else:
        return word[0] == word[-1] and is_palindrome_recur(word[1:-1])

# test
# print(is_palindrome_loop(""))
# print(is_palindrome_loop("A"))
# print(is_palindrome_loop("recursion"))
# print(is_palindrome_loop("civic"))
# print(is_palindrome_recur(""))
# print(is_palindrome_recur("A"))
# print(is_palindrome_recur("recursion"))
# print(is_palindrome_recur("civic"))