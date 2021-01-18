
def convert(num, b):
    """Recursive function that returns a string representing num in the base b"""
    if num < b:
        return str(num)
    if b > 16 or b < 2:
        raise ValueError
    remainder = num % b
    quotient = num // b
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
    reduced_result = convert(quotient, b)
    combined_result = reduced_result + remainder
    return combined_result

