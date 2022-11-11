# Prompt the user to input an integer between 32 and 126, a float, a character, and a string, storing each into separate variables. Then, output those four values on a single line separated by a space. 
integer_value = int(input("Enter integer (32 - 126): "))
float_value = float(input("Enter float: "))
character = str(input("Enter character: "))
string = str(input("Enter string: "))

print(f"{integer_value} {float_value} {character} {string}")

#output in reverse

print(f"{string} {character} {float_value} {integer_value}")

int_to_char = chr(integer_value)

print(f"{integer_value} converted to a character is {int_to_char}")

# char to int use ord()