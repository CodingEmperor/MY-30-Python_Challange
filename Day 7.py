In this project, I will be showing my knowledge of Sets

Exercises: Level 1

Find the length of the set it_companies

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = {22, 19, 24, 25, 26, 24, 25, 24}

print (len(it_companies))


Add 'Twitter' to it_companies

it_companies.add('Twitter')
print(it_companies)

Insert multiple IT companies at once to the set it_companies

it_companies.update(['LinkedIn', 'Snapchat'])
print(it_companies)

Remove one of the companies from the set it_companies

it_companies.remove('IBM')
print(it_companies)

What is the difference between remove and discard

s ={1, 2, 3, 4, 5}
s.remove(99) # This will raise a KeyError because 99 is not in the set
s.discard(99) # This will not raise an error, it will simply do nothing 


Exercises: Level 2
     

Join A and B

join_ab = A.union(B)
print(join_ab)
output: {19, 20, 22, 24, 25, 26, 27, 28}

Find A intersection B

intersection_ab = A.intersection(B)
print(intersection_ab)
Output: {19, 20, 22, 24, 25, 26}

Is A subset of B

are_disjoint = A.isdisjoint(B)
print(are_disjoint)
Output: False

Are A and B disjoint sets

they share alot of numbers so its False

Join A with B and B with A

join_ab = A.union(B)
join_ba = B.union(A)
print(join_ab)
print(join_ba)
Both will output: {19, 20, 22, 24, 25, 26, 27, 28}

What is the symmetric difference between A and B

sym_diff = A.symmetric_difference(B)
print(sym_diff)
Output: {27, 28}

Delete the sets completely

del A
del B

Exercises: Level 3

Convert the ages to a set and compare the length of the list and the set, which one is bigger?

age = [22, 19, 24, 25, 26, 24, 25, 24] # Example list from the challenge
age_set = set(age)

print(len(age))       # Output: 8
print(len(age_set))   # Output: 5 (duplicates removed)


Explain the difference between the following data types: string, list, tuple and set

sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.split() # Splits the string into a list of words
unique_words = set(words) # Converts list to set to remove duplicates

print(len(unique_words)) 
# Output: 10 (The unique words are: 'I', 'am', 'a', 'teacher', 'and', 'love', 'to', 'inspire', 'teach', 'people.')


