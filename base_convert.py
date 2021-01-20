# integer --> string consisting of either an integer and/or letter (hex value)
# given an integer and a base number, this recursive function returns back a string of the remainder digits for base b number in the reversed order

def convert(num, b):
    """Recursive function that returns a string representing num in the base b"""
    # remainder calculation / converting num to base b
    remainder = num % b
    # base cases
    if b > 16 or b < 2:
        raise ValueError('base out of range')
    if num < b:
        if num >= 10 and num <= 15:
            num = convert_helper(remainder)
        return str(num)
    # quotient calculation / converting the quotient to base b
    quotient = num // b
    # if the remainder is within 10 and 15 then it will go through the helper function to convert those numbers to hex values
    if remainder >= 10 and remainder <= 15:
        remainder = convert_helper(remainder)
    # reduced result
    reduced_result = convert(quotient, b)
    # combined result
    combined_result = reduced_result + str(remainder)
    return combined_result

# integer --> string
# helper function with if/elif statements for when the remainder is a hex value of A-F from 10-15
def convert_helper(remainder):
    """Helper function for convert to convert numbers from 10-15 to their respective hex value/character"""
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

