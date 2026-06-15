# script which prints a list and sorts it as a shallow copy
list_orig = [39, 8, 20, 100, 65]

print(f"Original list: {list_orig}")

# shallow copy of the original list, sorted
list_sorted = sorted(list_orig)
print(f"Sorted list copy: {list_sorted}")

# in place sorting of the original list
list_orig.sort()
print(f"Original list sorted: {list_orig}")

# push to the list
list_orig.append(1)
print(f"Original list adding 1: {list_orig}")

# remove from the list
list_orig.remove(100)
print(f"Original list removing 100: {list_orig}")

# reverse the list
list_orig.reverse()
print(f"Original list reversed: {list_orig}")