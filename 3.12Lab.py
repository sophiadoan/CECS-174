# remove gray from RGB

r = int(input())
g = int(input())
b = int(input())


if r < g and r < b:
    g = g - r  
    b = b - r
    r = r - r
if g < r and g < b: 
    r = r - g
    b = b - g
    g = g - g
if b < r and b < g:
    g = g - b
    r = r - b
    b = b - b
if r == b == g: 
    r = 0
    b = 0
    g = 0

print(r, g, b)