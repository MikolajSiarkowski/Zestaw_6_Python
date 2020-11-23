import math
import unittest
class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):        # zwraca string "(x, y)"
        x = self.x
        y = self.y
        return "({0},{1})".format(x,y)

    def __repr__(self):       # zwraca string "Point(x, y)"
        return "Point({0},{1})".format(self.x,self.y)
    
    def __eq__(self, other):  # obsługa point1 == point2
        return (self.x==other.x and self.y==other.y)

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):   # v1 + v2
        x = self.x + other.x
        y = self.y + other.y
        v3 = Point(x,y)
        return v3
    def __sub__(self, other):   # v1 - v2
        x = self.x - other.x
        y = self.y - other.y
        v3 = Point(x,y)
        return v3

    def __mul__(self, other):   # v1 * v2, iloczyn skalarny
        return (self.x*other.x)+(self.y*other.y)
    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D
        return self.x * other.y - self.y * other.x

    def length(self):           # długość wektora
        return math.sqrt(pow(self.x,2) + pow(self.y,2))
        
        
# Kod testujący moduł.



class TestPoints(unittest.TestCase):

    def setUp(self):
        self.zero = Point(0,0)
    def test_str(self):
        self.assertEqual(str(Point(2,1)), '(2,1)')
    def test_print(self):
        self.assertEqual(repr(Point(2,1)), 'Point(2,1)')
    def test_cmp(self):
        self.assertTrue(Point(2,1) == Point(2,1));
        self.assertFalse(Point(2,5) == Point(3,5))
        self.assertTrue(Point(2,4) != Point(3,5))
        self.assertFalse(Point(1,3) != Point(1,3))
        

    def test_add(self):   
        self.assertEqual(Point(1,2) + Point(3,2), Point(4,4))
    def test_sub(self):
        self.assertEqual(Point(1,2) - Point(3,2), Point(-2,0))
    def test_mul(self):
        self.assertEqual(Point(1,2) * Point(3,2), 7)
    def test_cross(self):
        self.assertEqual(Point(1,2).cross(Point(3,2)), -4)
    def test_length(self):
        self.assertEqual(Point(4,0).length(), 4)
    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # wszystkie testy
