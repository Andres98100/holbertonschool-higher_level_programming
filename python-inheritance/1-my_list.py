#!/usr/bin/python3
'''class list'''


class MyList(list):
    '''Public instance method'''
    def print_sorted(self):
        self.list = sorted(self)
        '''return a list sorted'''
        return print(self.list)
