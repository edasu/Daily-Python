# Instructions
#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6#
#Format the result to 2 decimal places = 33.60
#Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.
print('Welcome to tip calculator')
bill = float(input('What was the total? £'))
persentages = int(input('What percentage tip would you like to give? '))
tip = int((bill * persentages) / 100)
total_bill = tip + bill
people_split = int(input('How mony people to split the bill? '))
result_pay = round(total_bill / people_split, 2)
print(f'Each person should pay: £{result_pay}') 