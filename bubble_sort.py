# script performing bubble sort
nums = [64, 25, 12, 22, 11]

# create loop which will run n times - thee length of the array to give each number a chance to swap
# most efficient way is to use a flag which determines if the loop went through without swapping anything

for i in range(len(nums)):
    # flag will change to true if the inner loop does any work
    is_swapped = False

    # nested loop goes through whole list - subtract so the last index visited is 3 so it doesn't go out of bounds when adding 1 to make 4
    for j in range(len(nums) - 1):
        # if curr > next, use destructuring assignment to swap it
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
            # change flag
            is_swapped = True
        
    # print pass
    print(f"List at iteration {i}: {nums}")
    
    # check at the end if the is_swapped flag is False to break the loop - it'll reset to false on the next iteration
    if not is_swapped:
        break

# print final list
print(f"Final sorted list: {nums}")