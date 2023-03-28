# (a+bi)(c+di) = (ac−bd) + (ad+bc)i

class Complex:
    def __init__(self, r, i):
        self.real = r 
        self.imaginary = i

    def __add__(self, c):
        
        real=self.real+c.real
        imag=self.imaginary+c.imaginary
        c1=Complex(real,imag)
        return c1
      
    def __mul__(self, c):
        mulReal =  self.real*c.real - self.imaginary*c.imaginary
        mulImg =  self.real*c.imaginary + self.imaginary*c.real
        c2=Complex(mulReal, mulImg)
        return c2
        
    def __str__(self):
        if self.imaginary<0:
            return f"{self.real} - {-self.imaginary}i"
        else:
            return f"{self.real} + {self.imaginary}i"

c1 = Complex(1, -4)
c2 = Complex(331, -37)
print(c1 + c2)
print(c1 * c2)