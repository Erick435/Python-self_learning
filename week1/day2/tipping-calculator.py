#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

total = 150
tip_percentage = 12
pay_per_person = float(total) / 5
new_total_tip_per_person = (float(pay_per_person) * int(tip_percentage)) / 100
new_total_per_person =  float(pay_per_person) + float(new_total_tip_per_person)
total_use = "{:.2f}".format(new_total_per_person)


print(f"Your total is {pay_per_person} and your tip is {new_total_tip_per_person}. Your new Total is {total_use}")