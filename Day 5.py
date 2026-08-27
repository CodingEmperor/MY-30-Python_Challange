This is a list of exercises to practice Python list operations.


Declare an empty list

list1 = []

Declare a list with more than 5 items

list2 = [1, 2, 3, 4, 5, 6]

Find the length of your list

length = len(list1)


Get the first item, the middle item and the last item of the list

first_item = list2[0]
middle_item = list2[len(list2) // 2]
last_item = list2[-1]

Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

mixed_data_types = ["John", 30, 5.9, "Single", "123 Main St"]

Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

Print the list using print()

print(it_companies)

Print the number of companies in the list

print(len(it_companies))

Print the first, middle and last company

print(it_companies[0])
print(it_companies[len(it_companies) // 2])
print(it_companies[-1])

Print the list after modifying one of the companies

it_companies[0] = "Meta"

Add an IT company to it_companies

it_companies.append("Tesla")

Insert an IT company in the middle of the companies list

it_companies.insert(len(it_companies) // 2, "SpaceX")

Change one of the it_companies names to uppercase (IBM excluded!)
                                                   
it_companies[1] = it_companies[1].upper()
                                                   

Join the it_companies with a string '#;  '

with_joined_string = '#; '.join(it_companies)

Check if a certain company exists in the it_companies list.

if "Google" in it_companies:
    print("Google exists in the list.")
    

Sort the list using sort() method

list2.sort()

Reverse the list in descending order using reverse() method

reverse_list = list2[::-1]

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.reverse()
print(it_companies)


Slice out the first 3 companies from the list

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
first_three = it_companies[:3]


Slice out the last 3 companies from the list

last_three = it_companies[-3:]

Slice out the middle IT company or companies from the list

middle_company = it_companies[len(it_companies) // 2]

Remove the first IT company from the list

del it_companies[0]

Remove the middle IT company or companies from the list

del it_companies[len(it_companies) // 2]

Remove the last IT company from the list

del it_companies[-1]

Remove all IT companies from the list

it_companies.clear()

Destroy the IT companies list

del it_companies

Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB'] 
full_stack = front_end + back_end
full_stack.insert(full_stack.index('Redux') + 1, 'Python')
full_stack.insert(full_stack.index('Python') + 1, 'SQL')

Exercises: Level 2
The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]


Sort the list
ages.sort()
print("Sorted ages:", ages)  # [19, 19, 20, 22, 24, 24, 24, 25, 25, 26]

Min and Max ages
min_age = min(ages)
max_age = max(ages)
print("Min age:", min_age)  # 19
print("Max age:", max_age)  # 26

Sum of min and max
print("Sum of min and max:", min_age + max_age)  # 45

Median age (average of two middle numbers)
n = len(ages)  # 10
middle1 = ages[n // 2 - 1]  # 24
middle2 = ages[n // 2]      # 24
median = (middle1 + middle2) / 2
print("Median age:", median)  # 24.0

Average age
average = sum(ages) / len(ages)
print("Average age:", average)  # 22.8

Range of ages (max - min)
range_age = max_age - min_age
print("Range of ages:", range_age)  # 7