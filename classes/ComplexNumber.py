"""
>>> ComplexNumber(1,2) == ComplexNumber(1,2)
True
>>> ComplexNumber(2,1) == ComplexNumber(1,2)
False
"""


def isnum(var):
    if isinstance(var, int) or isinstance(var, float):
        return True
    else:
        return False

class ComplexNumber:
    def __init__(self, real_part=0, imaginary_part=0):
        if isnum(real_part) and isnum(imaginary_part):
            self.real_part = real_part
            self.imaginary_part = imaginary_part
        else:
            if (isnum(real_part) == False) and (isnum(imaginary_part) == False):
                raise ValueError("Invalid value for real and imaginary part")
            elif (isnum(real_part) == False):
                raise ValueError("Invalid value for real part")
            else:
                raise ValueError("Invalid value for imaginary part")
    def conjugate(self):
        return ComplexNumber(self.real_part, -1*self.imaginary_part)
    def __add__(self, other):
        return ComplexNumber(self.real_part+other.real_part, self.imaginary_part+other.imaginary_part)
    def __sub__(self, other):
        return ComplexNumber(self.real_part-other.real_part, self.imaginary_part-other.imaginary_part)
    def __mul__(self, other):
        a = self.real_part
        b = self.imaginary_part
        c = other.real_part
        d = other.imaginary_part
        return ComplexNumber(a*c-b*d, a*d+b*c)
    def __truediv__(self, other):
        a = self.real_part
        b = self.imaginary_part
        c = other.real_part
        d = other.imaginary_part
        if c == 0 and d == 0:
            raise ZeroDivisionError("division by zero")
        else:
            return ComplexNumber((a*c+b*d)/(c*c+d*d), (c*b-a*d)/(c*c+d*d))
    def __abs__(self):
        a = self.real_part
        b = self.imaginary_part
        return round((a*a+b*b)**(1/2), 3)
    def __eq__(self, other):
        a = self.real_part
        b = self.imaginary_part
        c = other.real_part
        d = other.imaginary_part
        if a==c and b==d:
            return True
        else:
            return False
    def __str__(self):
        img = self.imaginary_part
        real = self.real_part
        if img>=0:
            if img==0:
                img = ''
            else:
                if real == 0:
                    img = str(img)+'i'
                else:
                    img = '+'+str(img)+'i'
        else:
            img = str(img)+'i'
        if real == 0:
            if img == '':
                return '0'
            return str(img)
        else:
            real = str(self.real_part)
        return real+img


def default_test():
    c_1 = ComplexNumber(1, 2)
    c_2 = ComplexNumber(1, 2)
    check_equality = c_1 == c_2
    if check_equality:
        print('PASS')
    else:
        print('FAIL')
