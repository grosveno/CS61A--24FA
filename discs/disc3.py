def swipe(n):
    """Print the digits of n, one per line, first backward then forward.

    >>> swipe(2837)
    7
    3
    8
    2
    8
    3
    7
    """
    if n < 10:
        print(n)
    else:
        "*** YOUR CODE HERE ***"
        digits_but_last, last = n // 10, n % 10
        print(last)
        swipe(digits_but_last)
        print(last)


def skip_factorial(n):
    """Return the product of positive integers n * (n - 2) * (n - 4) * ...

    >>> skip_factorial(5) # 5 * 3 * 1
    15
    >>> skip_factorial(8) # 8 * 6 * 4 * 2
    384
    """
    if n <= 1:
        return 1
    else:
        return n * skip_factorial(n - 2)
    

def is_prime_helper(i, n):
    """If i == n, return True,
       Else, check if n % i == 0, if is 0, return False, else check i + 1"""
    if i == n:
        return True
    else:
        return n % i != 0 and is_prime_helper(i + 1, n)

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    return is_prime_helper(2, n)


def hailstone(n):
    """Print out the hailstone sequence starting at n, 
    and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    print(n)
    if n % 2 == 0:
        return even(n)
    else:
        return odd(n)

def even(n):
    return 1 + hailstone(n // 2)

def odd(n):
    "*** YOUR CODE HERE ***"
    if n == 1:
        return 1
    else:
        return 1 + hailstone(3 * n + 1)
    

def sevens(n, k):
    """Return the (clockwise) position of who says n among k players.

    >>> sevens(2, 5)
    2
    >>> sevens(6, 5)
    1
    >>> sevens(7, 5)
    2
    >>> sevens(8, 5)
    1
    >>> sevens(9, 5)
    5
    >>> sevens(18, 5)
    2
    """
    def f(i, who, direction):
        """Says i is who
           If i == n, just return,
           else simulate i + 1"""
        if i == n:
            return who
        "*** YOUR CODE HERE ***"
        if has_seven(i) or i % 7 == 0:
            direction = -direction
        who += direction
        if who == k + 1:
            who = 1
        elif who == 0:
            who = k
        return f(i + 1, who, direction)
    return f(1, 1, 1)

def has_seven(n):
    if n == 0:
        return False
    elif n % 10 == 7:
        return True
    else:
        return has_seven(n // 10)