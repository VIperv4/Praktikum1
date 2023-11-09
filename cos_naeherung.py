import math

x = float(input("X:"))
n = int(input("N:"))

z = 1
fmain = 1
f = 2
x1 = 1
n = n-1

while n !=0:
  f1 = f-1
  fmain = fmain*f1*f
  fmain = fmain * (-1)
  x1 = x1*x*x
  z = z + (1/(fmain))*x1
  n = n-1
  f = f+2
  
print ("Cos: " + str(math.cos(x)))  
print("Naeherung: " + str(z))
print("Fehler: " + str(math.cos(x)-z))