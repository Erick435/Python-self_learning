# For loop with range

# Using range, the 2nd number won't touch so it will stop at 10 instead of 11
# for number in range (1, 11):
#     print(number)

# total = 0
# for number in range(1, 101):
#     total += number
# print(total)

# you can add 3 parameters in range, the 3rd parameter is how many it will jump 

for number in range(0, 101, 5):
    print(number)
    
# starts from 0 and stops before 101 and JUMPS by 5