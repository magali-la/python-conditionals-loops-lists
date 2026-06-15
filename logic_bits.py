# this script uses bitwise operations to evaluate 5 and 3 in binary

# user inputs two number - 1 or 0
input1 = input("Pick a number. 1 or 0: ")
input2 = input("Pick a number. 1 or 0: ")

# convert the string into a number, then to booleans
input1_conv = bool(int(input1))
input2_conv = bool(int(input2))

# use operators to print results
print(f"{input1_conv} and {input2_conv} = {input1_conv and input2_conv}")
print(f"{input1_conv} or {input2_conv} = {input1_conv or input2_conv}")
print(f"not {input1_conv} = {not input1_conv}")

# Bitwise with 5 and 3
print(f"5 & 3 in binary - AND: {bin(5 & 3)}")
print(f"5 | 3 in binary - OR: {bin(5 | 3)}")
print(f"5 ^ 3 in binary - XOR: {bin(5 ^ 3)}")
print(f"~5 in binary - NOT: {bin(~5)}")
print(f"5 << 1 in binary - left shift: {bin(5 << 1)}")
print(f"5 >> 1 in binary - right shift: {bin(5 >> 1)}")
