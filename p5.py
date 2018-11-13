# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
# For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

# Given this implementation of cons:

# def cons(a, b):
#     def pair(f):
#         return f(a, b)
#     return pair
# Implement car and cdr.

def main():
  testCar()
  testCdr()

def cons(a, b):
  def pair(f):
      return f(a, b)
  return pair

def car(pairFunc):
  return pairFunc(lambda a,b: a)

def cdr(pairFunc):
  return pairFunc(lambda a,b: b)

def testCar():
  result = car(cons(3,4))
  assert result == 3

def testCdr():
  result = cdr(cons(3,4))
  assert result == 4

main()