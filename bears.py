def bears(n):
    if n == 42:
        return True
    if n < 42:
        return False
    res = False
    if n % 2 == 0:
        returning = (n//2)
        res = bears(returning)
    returning = n % 10 * ((n // 10) % 10)
    if (n % 3 == 0 or n % 4 == 0) and res == False and returning != 0:
        res = bears(n - returning)
    if (n % 5 == 0) and res == False:
        res = bears(n-42)
    return res




