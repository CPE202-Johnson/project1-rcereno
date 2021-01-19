#  integer --> string consisting of either an integer and/or letter (hex value)
# given an integer and a base number, this recursive function returns back a string of the remainder digits for base b number in the reversed order
def convert(num, b):
    """Recursive function that returns a string representing num in the base b"""
    # base cases
    if num < b:
        return str(num)
    if b > 16 or b < 2:
        raise ValueError
    # remainder calculation / converting num to base b
    remainder = num % b
    # quotient calculation / converting the quotient to base b
    quotient = num // b
    # if/elif/else statements for when the remainder is a hex value of A-F from 10-15 or if the remainder does not fit those conditions (else statement)
    if remainder == 10:
        remainder = 'A'
    elif remainder == 11:
        remainder = 'B'
    elif remainder == 12:
        remainder = 'C'
    elif remainder == 13:
        remainder = 'D'
    elif remainder == 14:
        remainder = 'E'
    elif remainder == 15:
        remainder = 'F'
    else:
        remainder = str(remainder)
    # reduced result
    reduced_result = convert(quotient, b)
    # combined result
    combined_result = reduced_result + remainder
    return combined_result

