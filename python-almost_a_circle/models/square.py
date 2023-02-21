#!/usr/bin/python3
'''import'''
from models.rectangle import Rectangle
'''class'''


class Square(Rectangle):
    '''method init'''
    def __init__(self, size, x=0, y=0, id=None):
        '''method super'''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''return'''
        return self.width

    @size.setter
    def size(self, value):
        '''validation'''
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        '''assignment'''
        self.width = value
        self.height = value

    def __str__(self):
        '''return'''
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y,
                        self.width))

    '''method assignment'''
    def update(self, *args, **kwargs):
        '''iterates args'''
        for i in range(len(args)):
            '''assignment'''
            if i == 0:
                self.id = args[i]
            elif i == 1:
                self.width = args[i]
            elif i == 2:
                self.x = args[i]
            elif i == 3:
                self.y = args[i]
        if len(args) == 0:
            pass
        '''assignment key and value'''
        for key, value in kwargs.items():
            if key == "id":
                self.id = value
            elif key == "size":
                self.size = value
            elif key == "x":
                self.x = value
            elif key == "y":
                self.y = value

    def to_dictionary(self):
        '''return'''
        return {"id": self.id, "size": self.size, "x": self.x,
                "y": self.y}
