import math
def square(num):
    print(f"num = {num} inside the function")
    num = 9
    return(num * num)
def main():
    val = eval(input("please enter a vlue "))
    sval = square(val)
    print(sval)
if __name__ == "__main__":
    main()