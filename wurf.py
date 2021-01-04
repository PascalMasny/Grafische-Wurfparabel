#Wurfparabel

#https://repl.it/languages/python3

#imports

import time
import math
import decimal
datei = open('data.dat','w')


#counter
t = 0

#Gx0,5
g= 4.5
#counter
n = 0

#Hello and inputs
print("Wurfparabel Rechner by Pascal Masny")
print("")
b=float(input("Wurfwinkel Beta (Grad):"))
v=float(input("Wurfgeschwindigkeit(m/s):"))
z=float(input("Starthöhe (m):"))
t2=float(input("Zeitspanne der Wurfs (s):"))
s=float(input("Schritweite (Bsp. 1, 0.1, 0.01):"))
print("")
time.sleep(1)

#Cos/sin

cos = math.cos(math.radians(b))
sin = math.sin(math.radians(b))

#counter
print("X:                    Y:")

while n < t2:
    
    n = n + s
    t = t + s
    
    x = t * v * cos
    y = t * v * sin + z - g * t * t

    print(x ,"  " ,y)

    datei.write("\n")
    datei.write(str(x))
    datei.write("   ")
    datei.write(str(y))
print("")