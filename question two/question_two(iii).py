# all numbers from 1 t0 100 are not visible by 2
for num in range(1, 101):
    # Check if the number is not divisible by 2
    if num  % 2 != 0:
        # Print the number
        print(num)

# Print all odd numbers from 1 to 100
print(*range(1, 101, 2), sep='\n')

