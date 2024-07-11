print("The Love Calculator is calculating your score...")
name1 = input("What is your name? \n") # What is your name?
name2 = input("What is your partners name? \n") # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

combined_names = name1 + name2

lower_case_names = combined_names.lower()

t = lower_case_names.count("t")
r = lower_case_names.count("r")
u = lower_case_names.count("u")
e = lower_case_names.count("e")
first_value = t + r + u + e

l = lower_case_names.count("l")
o = lower_case_names.count("o")
v = lower_case_names.count("v")
e = lower_case_names.count("e")
second_value = l + o + v + e

total_score = str(first_value) + str(second_value)

if (int(total_score) < 10 or int(total_score) > 90):
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif (int(total_score) >= 40 and int(total_score) <= 50):
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}.")