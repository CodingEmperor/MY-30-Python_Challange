# In this mini project, I will demonstrate how to use Tuples in Python. Tuples are immutable sequences, meaning that once they are created, their elements cannot be changed. They are defined by enclosing elements in parentheses `()`.


from typing import Unpack


Exercises: Level 1
Create an empty tuple

emdpty_tuple = ()

Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)

brothers = ("John", "Mike", "David")
sisters = ("Anna", "Emily", "Sophia")

Join brothers and sisters tuples and assign it to siblings

siblings = brothers + sisters

print(siblings)


How many siblings do you have?

siblings_count = len(siblings)

print(siblings_count) #output 6

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members

modified_siblings = siblings + ("Father", "Mother")


Exercises: Level 2

Unpack siblings and parents from family_members

unpacked_siblings = modified_siblings[:-2]
unpacked_parents = modified_siblings[-2:]




Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.

fruits = ("apple", "banana", "orange")
vegetables = ("carrot", "broccoli", "spinach")
animal_products = ("milk", "eggs", "meat")

food_stuff_tp = fruits + vegetables + animal_products

# Change the about food_stuff_tp tuple to a food_stuff_lt list

food_stuff_lt = list(food_stuff_tp)

Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.

# Calculate the middle index
middle_index = len(food_stuff_tp) // 2

# Check if odd or even number of items
if len(food_stuff_tp) % 2 == 1:  # Odd number (9 items)
    middle_item = food_stuff_tp[middle_index]
    print("Middle item:", middle_item)  # 'spinach'
else:  # Even number
    middle_items = food_stuff_tp[middle_index - 1:middle_index + 1]
    print("Middle items:", middle_items)


Slice out the first three items and the last three items from food_stuff_lt list

first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print("First three items:", first_three)
print("Last three items:", last_three)

Delete the food_stuff_tp tuple completely

del food_stuff_tp


Check if an item exists in tuple:

if 'apple' in food_stuff_lt:
    print("Apple is in the list.")
else:
    print("Apple is not in the list.")



Check if 'Estonia' is a nordic country

if 'Estonia' in ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden'):
    print("Estonia is a Nordic country.")


Check if 'Iceland' is a nordic country     

if 'Iceland' in ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden'):
    print("Iceland is a Nordic country.")

    