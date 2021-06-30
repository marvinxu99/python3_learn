# Class Attribute Functions - computed attributes
'''
object.__getattirbute__(self, attr)     ; called when object.attr
object.__getattr__(self, attr)          ; called when object.attr
object.__setattr__(self, attr, val)     ; object.attr = val
object.__delattr__(self)                ; del object.attr

'''

class myColor():
    def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 100

    # TODO: use getattr to dynamically return a value
    def __getattr__(self, attr):
        if attr == 'rgbcolor':
            return (self.red, self.green, self.blue)
        elif attr == 'hexcolor':
            return '#{0:02x}{1:02x}{2:02x}'.format(self.red, self.green, self.blue)
        else:
            raise AttributeError

    # TODO: use setattr to dynamically return a value
    def __setattr__(self, attr, val):
        if attr == 'rgbcolor':
            self.red = val[0]
            self.green = val[1]
            self.blue = val[2]
        else:
            super().__setattr__(attr, val)

    # TODO: use dir to list the available properties
    def __dir__(self):
        return ('red', 'green', 'blue')

def main():
    # create an instance of myColor
    cls1 = myColor()

    # TODO: print the value of a computed attribute
    print(cls1.rgbcolor)
    print(cls1.hexcolor)

    # TODO: set the value of a computed attribute
    cls1.rgbcolor = [125, 200, 86]
    print(cls1.rgbcolor)
    print(cls1.hexcolor)

    # TODO: access a regular attribute
    print(cls1.red)

    # TODO: list the available attributes
    print(dir(cls1))


if __name__ == "__main__":
    main()
