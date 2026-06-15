# script to running sum of even numbers 1-50

# sum variable
num_sum = 0

# FOR LOOP VERSION
# loop through numbers
for num in range(1, 51):
    # check if modulo 2 is 0 for an even number
    if num % 2 == 0:
        num_sum += num

print(f"The sum of even numbers from 1 to 50 is {num_sum}.")

# WHILE LOOP VERSION
# reset it to 0 for the while loop version
num_sum = 0
# i for the loop
i = 1
while i <= 50:
    if i % 2 == 0:
        num_sum += i
    
    # increment
    i += 1

print(f"The sum of even numbers from 1 to 50 is {num_sum}.")

# both loops produce a sum of 650. the for loop sets an explicit range and has less lines of code. there is no need to set an increment. the while loop can be beneficial too, but not so much for the use case of simply going up by numbers. there shouldn't be a reason to evaluate an expression at every iteration of a while loop for a simple count.