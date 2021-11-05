#Task 3

#1
"""
What is the value of expession 100/25?
Write a program that prints out the result and his type.
"""
#Solution
#Let the first value be 100 and second value be 25

first_value = int(input("Type the first value: "))       
second_value = int(input("Type the second value: "))
third_value = (first_value) / (second_value)
print(f"The value of expression for 100/25 is: {third_value}, and its type is {type(third_value)}")


#2
"""
Write a program code to calculate simple interest.
Assuming Abu Sharifah took a loan of $5,000 to buy a dell laptop 
at the rate of 6 percent simple interest for the period of 2years.
"""
#Solution
#S.I = P * R * T, where P = Principal, R - Rate & T = Time

principal = int(input("Enter the value for principal in $: "))
rate = int(input("Enter the value for the rate in percentage: "))
time = int(input("Enter the value for the time in t: "))
simple_interest = ((principal) * (rate) * (time)) / 100
print (f"Simple interest is {simple_interest}")


#3
"""
Write a python script that returns a user full name by asking for the user's first name and second name
"""
#Solution
first_name = input("My first name is :" )
# the input function will always return its value as a str, so you don't have to coerce it by using str
second_name = input("My second name is :" )
print(f"My full name is {first_name} {second_name}")


#4
"""
Write a python code that calculates the average age of six boys in a secondary school.
"""
boy1 = 12
boy2 = 13
boy3 = 15
boy4 = 16
boy5 = 19
boy6 = 28
add_boys_age = (boy1 + boy2 + boy3 + boy4 + boy5 + boy6)
avg_age_of_six_boys = (add_boys_age / 6)
print (f"The average age of 6 boys in secondary school is {avg_age_of_six_boys}")


#5
"""
Write a python code that converts Celsius to Fahrenheit (formula: F = 1.8 C + 32)
"""
C = float(input("Enter the temperature of Celsius in °C: "))
F = (1.8 * C) + 32
print(f"Temperature in Fahrenheit is {F}")
