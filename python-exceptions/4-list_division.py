#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    aux = []
    for i in range(list_length):
        result = 0
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            aux.append(result)
    return aux
