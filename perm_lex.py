# string --> string(s)
def perm_gen_lex(a):
    if len(a) == 1:
        return [a]
    if a == '':
        return []
    list = []
    for char in a:
        keep = char
        newStr = a.replace(char, '')
        reduced_result = perm_gen_lex(newStr)
        for i in reduced_result:
            list.append(keep + i)
#        list.append(keep + str(reduced_result))
    return list




 