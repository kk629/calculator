def Add(a, b):
    a = int(a)
    b = int(b)
    c = a + b
    return c


def Subtract(a, b):
    a = int(a)
    b = int(b)
    c = b - a
    return c


def Multiply(a, b):
    a = int(a)
    b = int(b)
    c = a * b
    return c


def Divide(a, b):
    a = int(a)
    b = int(b)
    c = b / a
    c = round(c, 9)
    return c


def Square(a):
    a = int(a)
    c = a ** 2
    return c


def Square_root(a):
    a = int(a)
    c = a ** 0.5
    if c > 10:
        c = round(c, 8)
    else:
        c = round(c, 9)

    return c


class Calculator:
    result = 0

    def __init__(self):
        pass

    def Add(self, a, b):
        self.result = Add(a, b)
        return self.result

    def Subtract(self, a, b):
        self.result = Subtract(a, b)
        return self.result

    def Multiply(self, a, b):
        self.result = Multiply(a, b)
        return self.result

    def Divide(self, a, b):
        self.result = Divide(a, b)
        return self.result

    def Square(self, a):
        self.result = Square(a)
        return self.result

    def Square_root(self, a):
        self.result = Square_root(a)
        return self.result