# Question 1
# take the following list and multiply all list items together.
part1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096] 
result = 1
for x in part1:
    result *= x

print(result)

# Question 2
# take the following list and add all list items together
part2 = [-1, 23, 483, 8573, -13847, -381569, 1652337, 718522177]
result = 0
for x in part2:
    result += x

print(result)

#Question 3
# take the following list and only add together those list items which are even. 
# You can use the following snippet of code to see if a number is even or odd. The % operation is called MODULE and is used to find the remainder after division of one number by another.
# We divide by 2 and look at the remainder; if there is NO remainder the number is EVEN, if there IS a remainder the number is ODD.
part3 = [146, 875, 911, 83, 81, 439, 44, 5, 46, 76, 61, 68, 1, 14, 38, 26, 21] 
result = 0
for x in part3:
    isEven = x % 2 == 0
    if isEven:
        result += x
    else:
        continue

print(result)
