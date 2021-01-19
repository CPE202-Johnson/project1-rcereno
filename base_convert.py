#  integer --> string consisting of either an integer and/or letter (hex value)
# given an integer and a base number, this recursive function returns back a string of the remainder digits for base b number in the reversed order
def convert(num, b):
    """Recursive function that returns a string representing num in the base b"""
    # remainder calculation / converting num to base b
    remainder = num % b
    # base cases
    if num < b:
        if num >= 10 and num <= 15:
            num = convert_helper(remainder)
        return str(num)
    if b > 16 or b < 2:
        raise ValueError
    # quotient calculation / converting the quotient to base b
    quotient = num // b
    # reduced result
    reduced_result = convert(quotient, b)
    # combined result
    combined_result = reduced_result + str(remainder)
    return combined_result

# integer --> string
# if/elif/else statements for when the remainder is a hex value of A-F from 10-15 or if the remainder does not fit those conditions (else statement)
def convert_helper(remainder):
    if remainder == 10:
        return 'A'
    elif remainder == 11:
        return 'B'
    elif remainder == 12:
        return 'C'
    elif remainder == 13:
        return 'D'
    elif remainder == 14:
        return 'E'
    elif remainder == 15:
        return 'F'
    else:
        return str(remainder)

