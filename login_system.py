def contains_digit(s):
    flag = False
    for i in s:
        if i.isdigit():
            flag = True
            break
    return flag

def contains_special(s):
    flag = False
    for i in s:
        if i in '!@#$%^&*()_-./':
            flag = True
            break
    return flag

def contains_upper(s):
    flag = False
    for i in s:
        if i.isupper() and i.isalpha():
            flag = True
            break
    return flag

def contains_lower(s):
    flag = False
    for i in s:
        if i.islower() and i.isalpha():
            flag = True
            break
    return flag

