# This Section will be my practice of Day 4 of 30 Days of Python Challenge


#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

part1 = 'Thirty'
part2 = 'Days'
part3 = 'Of'
part4 = 'Python'
result = part1 + ' ' + part2 + ' ' + part3 + ' ' + part4
print(result) #output: Thirty Days Of Python

#Declare a variable named company and assign it to an initial value "Coding For All".

part1 = 'Coding'
part2 = 'For'
part3 = 'All'

result = part1 + ' ' + part2 + ' ' + part3
print(result) #output: Coding For All

#Print the variable company using print().

Company = "Coding For All"
print(Company) #output: Coding For All


# Print the length of the company string using len() method and print().

print(len(Company)) #output: 14

# Change all the characters to uppercase letters using upper() method.

print(Company.upper()) #output: CODING FOR ALL


# Change all the characters to lowercase letters using lower() method.
print(Company.lower()) #output: coding for all

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.

print(Company.capitalize()) #output: Coding for all
print(Company.title()) #output: Coding For All
print(Company.swapcase()) #output: cODING fOR aLL

# Cut(slice) out the first word of Coding For All string.

print(slice := Company.split()[0]) #output: Coding

# Check if Coding For All string contains a word Coding using the method index, find or other methods.

index = Company.find('Coding')
print(index) #output: 0

# Replace the word coding in the string 'Coding For All' to Python.

replaced_string = Company.replace('Coding', 'Python')
print(replaced_string) #output: Python For All')

# Change "Python for Everyone" to "Python for All" using the replace method or other methods.

changed_string = 'Python for Everyone'.replace('Everyone', 'All')
print(changed_string) #output: Python for All


#  Split the string 'Coding For All' using space as the separator (split()) .

split_string = Company.split(' ')
print(split_string) #output: ['Coding', 'For', 'All']

# Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.

split_companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(', ')
print(split_companies) #output: ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# What is the character at index 0 in the string Coding For All.

character_at_index_0 = Company[0]
print(character_at_index_0) #output: C

# What is the last index of the string Coding For All.

last_index = len(Company) - 1
print(last_index) #output: 13

# What character is at index 10 in "Coding For All" string.

character_at_index_10 = Company[10]
print(character_at_index_10) #output: A

# Create an acronym or an abbreviation for the name 'Python For Everyone'.

create_acronym = 'Python For Everyone'
acronym = ''.join(word[0] for word in create_acronym.split())

# Create an acronym or an abbreviation for the name 'Coding For All'.

create_acronym_coding = 'Coding For All'
acronym_coding = ''.join(word[0] for word in create_acronym_coding.split())

# Use index to determine the position of the first occurrence of C in Coding For All.

index_of_C = Company.index('C')
print(index_of_C) #output: 0

# Use index to determine the position of the first occurrence of F in Coding For All.

index_of_F = Company.index('F')
print(index_of_F) #output: 7

# Use rfind to determine the position of the last occurrence of l in Coding For All People.

rfind_of_l = Company.rfind('l')
print(rfind_of_l) #output: 13

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

index_of_because = 'You cannot end a sentence with because because because is a conjunction'.find('because')
print(index_of_because) #output: 31

# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

rindex_of_because = 'You cannot end a sentence with because because because is a conjunction'.rindex('because')
print(rindex_of_because) #output: 43

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

slice_because = 'You cannot end a sentence with because because because is a conjunction'[31:44]
print(slice_because) #output: because because because

# Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))  # Output: 31

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence[31:54])  # Output: because because because


# Does 'Coding For All' start with a substring Coding?

company = 'Coding For All'
print(company.startswith('Coding'))  # Output: True


# Does 'Coding For All' end with a substring coding?

company = 'Coding For All'
does_end_with_coding = company.endswith('coding')
print(does_end_with_coding) #output: False

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.

company = '   Coding For All      '
print(company.strip())  # Output: Coding For All


# Which one of the following variables return True when we use the method isidentifier():

isidentifier1 = '30DaysOfPython'
isidentifier2 = 'thirty_days_of_python'

# 30DaysOfPython

print(isidentifier1.isidentifier())  # Output: False

# thirty_days_of_python

print(isidentifier2.isidentifier())  # Output: True

# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.

libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_libraries = ' # '.join(libraries)
print(joined_libraries)  # Output: Django # Flask # Bottle # Pyramid # Falcon

# Use the new line escape sequence to separate the following sentences.

new_line_string = "I am enjoying this challenge.\nJust wonder what is next."
print(new_line_string)  # Output:

# I am enjoying this challenge.



# just wonder what is next.



# Use a tab escape sequence to write the following lines.

# Name      Age     Country   City

# Asabeneh  250     Finland   Helsinki

# Use the string formatting method to display the following:

# radius = 10

# area = 3.14 * radius ** 2

# The area of a circle with radius 10 is 314 meters square.

Tab_sequence_string = "Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki"
print(Tab_sequence_string)  # Output:   Name    Age     Country City
# Asabeneh  250     Finland Helsinki   

# Make the following using string formatting methods:

# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144

string_formatting = f"8 + 6 = {8 + 6}\n8 - 6 = {8 - 6}\n8 * 6 = {8 * 6}\n8 / 6 = {8 / 6:.2f}\n8 % 6 = {8 % 6}\n8 // 6 = {8 // 6}\n8 ** 6 = {8 ** 6}"
print(string_formatting)  # Output:




