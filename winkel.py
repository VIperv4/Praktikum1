import math

p1x = float(input("Punkt 1 X-Koordinate: "))
p1y = float(input("Punkt 1 Y-Koordinate: "))
p2x = float(input("Punkt 2 X-Koordinate: "))
p2y = float(input("Punkt 2 Y-Koordinate: "))

if p2x>p1x:
    if p2y>p1y:
        smain = (p2x -p1x, p2y - p1y)
        s2 = (0,1)

        wt = smain[0] * s2[0] + smain[1] *s2[1] / math.sqrt(smain[0]**2 + smain[1]**2) * math.sqrt(s2[0]**2 + s2[1]**2)
        w = math.degrees(math.acos(wt))
        w = 90 - w

        print("Winkel: " + str(w))
        
    else:
        print("Fehler")
else:
        print("Fehler")