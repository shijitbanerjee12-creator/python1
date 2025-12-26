def find_first_set_bit(n):
    if n==0:
        return -1
    position =0
    while (n & 1)==0:
        n>>=1
        position += 1
        return position
    

number=3
first_set_bit_position = find_first_set_bit(number)
print(f"First_set_bit_position:{first_set_bit_position}")