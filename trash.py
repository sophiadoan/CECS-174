# count = 0
# inputcount = 0

# while inputcount < 5:
#     user_input = int(input())
#     if user_input > 0:
#         count += 1
#     inputcount += 1
# print(count)

# def calculate_num_gallons(gas_price, num_gal):
#     gallons = gas_price * num_gal
#     return gallons
# user_input_price = float(input())

# user_input_gal = float(input())
# print(calculate_num_gallons(user_input_price, user_input_gal))

# z=0
# i=36
# while i>1:
#     i-=1
#     z+=1
#     if i == 19:
#         break
    
# print(z)

def complementary_nucleotide(nucleotide):
    if nucleotide == 'A':
        nucleotide = nucleotide.replace('A', 'T')
    elif nucleotide == 'T':
        nucleotide = nucleotide.replace('T', 'A')
    elif nucleotide == 'G':
        nucleotide = nucleotide.replace('G', 'C')
    elif nucleotide == 'C':
        nucleotide = nucleotide.replace('C', 'G')
    return nucleotide
    
def complementary_sequence(dna_sequence):
    complementary_sequence = ''
    for i in dna_sequence:
        complementary_sequence += complementary_nucleotide(i)
    return complementary_sequence

dnaseq = 'ATGCTCGTCCGCGCCCTA'
print(complementary_sequence(dnaseq))

