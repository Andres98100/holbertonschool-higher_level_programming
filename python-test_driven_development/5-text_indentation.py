#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new_text = []
    char = [".", "?", ":"]
    aux = ""
    for i in text:
        aux += i
        if i in char:
            new_text.append(aux)
            aux = ""
            print(aux)
    for aux in new_text:
        print(aux)
