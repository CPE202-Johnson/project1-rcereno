# string --> list of string(s)
# takes in a given string and returns its variety of permutations using recursion
def perm_gen_lex(a):
    # base cases
    if len(a) == 1:
        return [a]
    if a == '':
        return []
    # creating a list
    list = []
    # for loop to loop through the given string input
    for char in a:
        keep = char # stores the character that will eventually be removed temporarily
        newStr = a.replace(char, '') # removes the stored character
        reduced_result = perm_gen_lex(newStr) # reduced result
        # combined result
        for i in reduced_result:
            list.append(keep + i)
    return list




 