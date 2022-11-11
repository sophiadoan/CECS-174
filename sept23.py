a = 1
b = 2
c = 3
print(a, b, c, sep = 'p')

mul = int(input("what time table do you want to see? "))
print(f"1 x {mul} = {1 * mul}")
print(f"2 x {mul} = {2 * mul}")
print(f"3 x {mul} = {3 * mul}")
print(f"4 x {mul} = {4 * mul}")

count = 1
while count <= 13:
    print(f"{count} x {mul} = {count * mul}")
    count += 1
print("Done...")

