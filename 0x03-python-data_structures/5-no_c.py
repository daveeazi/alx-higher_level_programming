#!/usr/bin/python3
def no_c(my_string):
    newStr = ""
    for letter in my_string:
        if (letter != 'c' and letter != 'C'):
            newStr += letter
    return (newStr)
