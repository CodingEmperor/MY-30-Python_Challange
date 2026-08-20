# This is my interpratation of how to use pythons basic functions and operators

print ('Addition: ', 1 + 3)
print ('Subtraction: ', 5 - 2)
print ('Multiplication: ', 4 * 6)
print ('Division: ', 10 / 2) #The division operator (/) returns a float value   
print ('Floor Division: ', 10 // 2) #The floor division operator (//) returns an integer value
print ('Modulus: ', 10 % 3) #The modulus operator (%) returns the remainder of the division
print ('Exponentiation: ', 2 ** 3) #The exponentiation operator (**) returns the result of raising the first operand to the power of the second operand


#The next part is me show answering a question from the 30 days of python challenge by  Asabeneh#455

# Write a Python script that displays the following table

# 1 1 1 1 1     
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

for n in range (1, 6):
    print(n, 1, n, n**2, n**3)
    









