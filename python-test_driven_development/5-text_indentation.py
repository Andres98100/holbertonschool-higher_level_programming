#!/usr/bin/python3
'''function print a text in new lines'''


def text_indentation(text):
    '''validation'''
    if type(text) != str:
        raise TypeError("text must be a string")
    '''chars'''
    char = [".", "?", ":"]
    '''text iterates'''
    prev = 0
    for i in range(len(text)):
        '''validation'''
        if i == len(text) - 1:
            print(text[prev:i + 1], end="")
        elif text[i] in char:
            print(text[prev:i + 1], end="")
            print('\n')
            prev = i + 1
            while text[prev] == " ":
                prev += 1
