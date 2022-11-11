def get_magnitude(number):
   while True:
    maginput = float(input(f"Please enter the magnitude for earthquake {number}: "))
    if maginput < 0:
        continue
    else:
        return maginput

def compare_magnitudes(magnitude1, magnitude2):
    f = 10 ** (1.5 * (magnitude1 - magnitude2))
    # if magnitude1 < magnitude2:
    #     f = 1/f
    # else:
    #     f = f
    return f

def get_run_again():
    runagain = input("Try again? Type 1 for yes: ")
    if runagain == '1':
        return True
    else: 
        return False


# The main application
if __name__ == "__main__":
    while True:
        input1 = get_magnitude(1)
        input2 = get_magnitude(2)
        if input1 > input2:
            print(f"An earthquake of magnitude {input1} is {compare_magnitudes(input1, input2):.1f} times more powerful than an earthquake of magnitude {input2}.")
        else:
            print(f"An earthquake of magnitude {input2} is {1/compare_magnitudes(input1, input2):.1f} times more powerful than an earthquake of magnitude {input1}.")
        if get_run_again() == False:
            print("Bye!")
            break
        else:
            continue
    
    
