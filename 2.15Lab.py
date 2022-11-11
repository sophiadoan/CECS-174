# MUSICAL NOTE FREQUENCIES

import math

f0 = int(input("What is the frequency of the initial note? "))

r = math.pow(2, 1/12)

f1 = f0 * math.pow(r, 1)
f2 = f0 * math.pow(r, 2)
f3 = f0 * math.pow(r, 3)
f4 = f0 * math.pow(r, 4)

print(f"{f0} {f1:.2f} {f2:.2f} {f3:.2f} {f4:.2f}")