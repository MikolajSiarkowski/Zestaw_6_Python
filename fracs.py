import math
import unittest
def NWW(a,b):
        return int(abs(a*b / math.gcd(a,b)))
class Frac:
    """Klasa reprezentująca ułamek."""

    def __init__(self, x=0, y=1):
        self.x = x
        self.y = y

    def simplify(self):
        dziel = math.gcd(self.x,self.y)
        x = int(self.x/dziel)
        y = int(self.y/dziel)
        Fx=Frac(x,y)
        return Fx
    
    
    def __str__(self):         # zwraca "x/y" lub "x" dla y=1
        if(self.y == 1):
            return "{0}".format(self.x)
        else:
            return "{0}/{1}".format(self.x,self.y)
    def __repr__(self):       # zwraca "Frac(x, y)"
        return "Frac({0},{1})".format(self.x,self.y)
    # Python 2
    #def __cmp__(self, other): pass  # cmp(frac1, frac2)

    # Python 2.7 i Python 3
    def __eq__(self, other):
        f1 = self.simplify()
        f2 = other.simplify()
        
        return f1.x == f2.x and f1.y == f2.y

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):        #self < other
        wiel = NWW(self.y,other.y)
        x1 = self.x * (wiel/self.y)
        x2 = other.x * (wiel/other.y)
        return (x1 < x2)

    def __le__(self, other):    #self <= other
        wiel = NWW(self.y,other.y)
        x1 = self.x * (wiel/self.y)
        x2 = other.x * (wiel/other.y)
        return (x1 <= x2)
    #def __gt__(self, other): pass

    #def __ge__(self, other): pass

    def __add__(self, other):   # frac1 + frac2
        wiel = NWW(self.y,other.y)
        x1 = self.x * (wiel/self.y)
        x2 = other.x * (wiel/other.y)
        y1 = wiel
        Fx = Frac(int(x1+x2), int(y1))
        Fx = Fx.simplify()
        return Fx
    
    def __sub__(self, other):  # frac1 - frac2
        wiel = NWW(self.y,other.y)
        x1 = self.x * (wiel/self.y)
        x2 = other.x * (wiel/other.y)
        y1 = wiel
        Fx = Frac(int(x1-x2), int(y1))
        Fx = Fx.simplify()
        return Fx
    
    def __mul__(self, other):   # frac1 * frac2
        x1 = self.x * other.x
        y1 = self.y * other.y
        Fx = Frac(x1,y1)
        Fx = Fx.simplify()
        return Fx
               
    def __div__(self, other):   # frac1 / frac2
        x1 = self.x * other.y
        y1 = self.y * other.x
        Fx = Frac(x1,y1)
        Fx = Fx.simplify()
        return Fx
    
    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):  # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):  # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    def __float__(self):       # float(frac)
        return self.x/self.y
# Kod testujący moduł.

class TestFractions(unittest.TestCase):

    def setUp(self): 
        self.zero = Frac(0,1)
    def test_print(self):
        self.assertEqual(repr(Frac(2,1)), 'Frac(2,1)')
    def test_cmp(self):
        self.assertTrue(Frac(2,1) == Frac(4,2))
        self.assertFalse(Frac(2,5) == Frac(3,5))
        self.assertTrue(Frac(2,4) != Frac(3,5))
        self.assertFalse(Frac(2,6) != Frac(1,3))
        self.assertTrue(Frac(4,6) < Frac(3,1))
        self.assertFalse(Frac(4,5) < Frac(3,5))
        self.assertTrue(Frac(2,2) <= Frac(3,1))
        self.assertFalse(Frac(4,1) <= Frac(3,3))

    def test_add(self):   
        self.assertEqual(Frac(1,2) + Frac(3,2), Frac(2,1))
    def test_sub(self):
        self.assertEqual(Frac(1,2) - Frac(3,2), Frac(-1,1))
    def test_mul(self):
        self.assertEqual(Frac(1,2) * Frac(3,2), Frac(3,4))
   # def test_div(self):
    #    self.assertEqual(Frac(1,2) / Frac(3,2), Frac(1,3))
    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # wszystkie testy
