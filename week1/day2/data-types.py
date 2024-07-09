#Data Types

#String

print("Hello"[1])

#Integer

print("123" + "345")

123_345_678

#Float
3.14159

#Boolean
True
False

# ==================== DATA TYPES EXERCISE =======================

# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

# Warning. Do not change the code on line 1. Your program should work for different inputs. e.g. any two-digit number.

# The last line of your program should print the result.

# Example 1 Input
# 39

# Example 1 Output
# 12

two_digit_number = input()
num1 = int(two_digit_number[0])
num2 = int(two_digit_number[1])
result = (num1 + num2)
print(result)


# ===================== NUMBER MANIPULATION ========================

print(int(8 / 3))
print(round(8 / 3))
print(8 // 3) #The answer would be an integer (whole number)
print(type(8 // 3)) # Integer
print(type(8 / 3)) # Float

result = 4 / 2
result /= 2
print(result) # Answer = 1



score = 0
height = 1.8
isWinning = True

print("Your score is: " + int(score))

# using f string

print(f"your score is: {score}, your height is {height}. Winning? {isWinning}")