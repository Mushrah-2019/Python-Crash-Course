#Question1 - Create a list that contains at least one string, one integer and one float.
my_list = ["Rice", 32000 , 50.5 ]
print(f"The price of {my_list[0]} in the market is #{my_list[1]} and it weight {my_list[2]}kg, therefore, my_list consist of {type(my_list[0])}, {type(my_list[1])} and {type(my_list[2])}")


#Question2 - How do I index a nested list? For example I want to grab 2 from [1,1,[1,2]]
my_list2 = [1,1,[1,2]]
print(f"One can index a nested list by using multiple indices to reference items within a nested list")
print(f"{my_list2[2][1]}")


#Question3 - If lst = [0,1,1]. What is the result of lst.pop()
lst = [0,1,1]
print (f"The result of lst.pop is {lst.pop()}, because pop() removes the last item in the list if no index is specified")


#Question4 - List can have multiple objects/data type?
#Yes


#Question5 - if lst = ['a','b','c'], what is the result of lst[1:]
lst = ['a','b','c']
print(f"The result of lst[1:] is {lst[1:]}") 


#Question6 - When do we choose a list and when do we use dictionary?
print(f"One choose a list if one have an ordered collection of items and one use dictionary if one have a set of unique keys that map to values.")


#Question7 - Create a dictionary with three key value pair
my_dict = {'first_name': 'Musharraf', 'Last_name': 'Sulayman', 'Age': 32 }
print(my_dict['first_name']) #Example


#Question8 - Create a dictionary where all the keys are strings, and all the values are integers.
my_dict2 = {'no_of_people_in_python_crash_course': 11, 'no_of_female_in_the_class': 1, 'no_of_evicted_student':1}
print(my_dict2['no_of_people_in_python_crash_course'])



#Question9 - Dictionaries retain order and are a sequence.
print(f"The statement is wrong because dictionary only retain order but its NOT a sequence")


#Question10 - Given d = {'k1':[1,2,3]}. What is the output of d['k1'][1]
d = {'k1':[1,2,3]}
print(f"The output of d['k1'][1]  is {d['k1'][1]}")


#Question11 - Dictionary are immutable?
print(f"No, they are mutable")


#Question12 - d = {'simple_key': 'hello'}. Grab 'Hello'
d = {'simple_key': 'hello'}
print(d['simple_key'])


#Question13...my_dict = {'k1':{'k2': 'Hello'}} ....Grab Hello
my_dict = {'k1':{'k2': 'Hello'}} 
print(my_dict['k1']['k2'])


#Question14...my_dict = {'k1':[{'nest_key':['this is deep',['hello']]}]} ... Grab Hello
my_dict = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(my_dict['k1'][0]['nest_key'][1])


"""
#Question15...my_dict = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}...Grab hello
my_dict = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(my_dict['k1'][1][1])   
#This question is tooooo tough.
"""