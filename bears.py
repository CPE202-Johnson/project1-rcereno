# integer --> boolean
# a number is given as an input argument which will then return a boolean on whether that number will equal to 42 while possibly going through 3 conditions to reduce it

def bears(n):
    """A True return value means that it is possible to win
    the bear game by starting with n bears. A False return value means
    that it is not possible to win the bear game by starting with n
    bears."""
    # base cases
    if n == 42:
        return True
    if n < 42:
        return False
    # initially setting result to False
    res = False
    # condition one if n is an even number
    if n % 2 == 0:
        returning = (n//2)
        res = bears(returning) # reduction result with new n value
    # condition two if n is divisible by 3 or 4
    returning = n % 10 * ((n // 10) % 10)
    if (n % 3 == 0 or n % 4 == 0) and res == False and returning != 0:
        res = bears(n - returning) # reduction result with new n value
    # condition three if n is divisible by 5
    if (n % 5 == 0) and res == False:
        res = bears(n-42) # reduction result with new n value
    return res




