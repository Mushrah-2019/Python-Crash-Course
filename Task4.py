#Task4

#Question1...Hello there, how old are you?-What index will return "how old".
question = "Hello there, how old are you?"
print(question[13:20])


#Question2...story = "Python is awesome"-What is story [2:4] + story[-1]
story = "Python is awesome"
story1 = story[2:4]
story2 = story[-1]
story3 = (story1) + (story2)
print((f"Story1 is {story1}, while the story2 is {story2}, by concatenate the two, we will have {story3}"))


#Question3...mystring = "Python rocks"-What is len(mystring)
mystring = "Python rocks"
print(f"Len mymystring is: {len(mystring)}")


#Question4...flower = "Rose" What is flower[0]="P"; print (flower)? Will it return 'Pose'
flower = "Rose"
flower2 = flower[0]
flower4 = flower[1:4]
flower3 = "P"
print((flower3) + (flower4))


#Question5...word = "Python is cool"-What is word [-4] * 3
word = "Python is cool"
print(f"The word [-4] * 3 is: {word[-4] * 3}")


#Question6...Write a code that return "pepsi" as "PEPSI"
drink = "pepsi"
print(f"By using command .upper(), it will return {drink} as: {drink.upper()}")


#Question7...write a code that return "macdonald" as "MacDonald"
let_name1 = "mac"
let_name2 = "donald"
print(let_name1.title() + let_name2.title())


#Question8...Write a code that return "MUSHRAH" as "mushrah"
my_username = "MUSHRAH"
print(f"By using .lower() command, it will return {my_username} as {my_username.lower()}")


#Question9...Using the built-in method, how will you "Hello world" as a list?
greeting = "Hello World"
greeting.split()
print(greeting.split())


#Question10...How do I add a "-" in between every character in a string "Python is cool"
say = "Python is cool"
say1 = "-".join(say)
print(say1)


#Question11...How do I remove "Hello" from "Hello World"
welcome = "Hello World"
print(welcome[0:5])


#Question12...What is the index of the first character in a string?
answer = 0
print(f"The first index of the first character in a string is {answer}")


#Question13...Using one of the Built-in method, print out the numbers of 'o' are in python is sooo cool
truth_is = "python is so cool"
truth_is.count('o')
print(truth_is.count('o'))


#Question14
"""
If I want to write this string: "hello world!" welcome to Python" as a title case,
What inbuit method of python will I call?
"""
welcome_message = "hello world! welcome to Python"
print(f"The inbuilt method of python that will make the welcome message as title case is by using .title() command.")


#Question15...Convert this string to a title case: "Hello world!, welcome to python"
welcome_msg = "Hello world!, welcome to python"
print(f"One will use .title() command to convert this string to title case, and by doing that, we will have {welcome_msg.title()}")


