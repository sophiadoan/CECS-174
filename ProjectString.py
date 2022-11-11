
def num_char(user_input): # 1
    num_char = len(user_input)
    return num_char 

def num_e(user_input): # 3
    num_e = 0
    for char in user_input:
        if char == 'e':
            num_e += 1
    return num_e

def first_word(user_input): # 5 display first word
    space = user_input.find(' ')
    first_word = user_input[0:space]
    return first_word

def cap_vowels(user_input): # 7 return capitalized vowels 
    vowels = ['a', 'e', 'i', 'o', 'u']
    newstring = ''
    for char in user_input: 
        if char in vowels:
            char = char.upper()
        newstring += char
    return newstring 

def string_padding(user_input): # 8
    string_padding = user_input.center(50, '~')
    string_padding1 = string_padding.center(70, '+')
    return string_padding1

if __name__ == "__main__":
    name = input("Please enter your name: ")

    # print(num_char(name))
    # print(num_e(name))
    # print(first_word(name))
    #print(cap_vowels(name))
    print(string_padding(name))








print('hi')
# hello