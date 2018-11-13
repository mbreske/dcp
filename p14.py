# The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

# Hint: The basic equation of a circle is x2 + y2 = r2.

#Let r = 1. A = π. x2 + y2 = 1.
#Integrate unit circle from (0,1) - mulitply by 4 to get π

from random import uniform

def main():
  viaMonteCarlo()

def viaMonteCarlo():
  iterations = 10**6
  in_circle = 0
  for _ in range(iterations):
    if isInCircle(getRandomPoint()):
      in_circle += 1
  print (4*in_circle/iterations)
  

def getRandomPoint():
  return (uniform(0,1), uniform(0,1))

def viaIntegration():
  dx = 0.01
  interval = [dx*i for i in range(0,int(1/dx)+1)]
  area = 0
  for i in range(0, len(interval)-1):
    x0 = interval[i]
    x1 = interval[i+1]
    y0 = circle(x0)
    y1 = circle(x1)
    a_i = dx*(min(y0,y1)) + 0.5*dx*abs(y1-y0)
    area += a_i
  print (4*area)

def isInCircle(point):
  return point[0]**2 + point[1]**2 < 1

def circle(x):
  return (1-x**2)**0.5

main()