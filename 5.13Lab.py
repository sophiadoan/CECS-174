import math

val =int(input())
while math.sqrt(val) % 1 != 0:
    val = int(input())
else:
    print(int(math.sqrt(val)))
