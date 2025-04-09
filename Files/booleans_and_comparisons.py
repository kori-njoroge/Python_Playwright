# Booleans
# integers
print(2 == 2)
print(2 != 2)
print(2 > 3)
print(2 <= 3)
print(2.9 <= 2.3)

# strings - this is case sentitive (pythin is UTF8 encoded)
print('s' == 's')
print('s' == 'S')
print('s' > 'S')

print( "Gideon" ==  "gideon")

# boolean Logic
print ("************Boolean Logic***********")
a = 1
b = 2
c = 3

# and - all the values have to be true for the statement to return a true.
print(a == 11 and b == 21 and c == 33)
print(a == 1 and b == 2 and c == 3)

# or - either of the statements have to be true to return a true
print(a == 1 or b == 21 or c == 3)
print(a == 1 or b == 21 or c == 37)


print("***Combining them all together+***")
#Combining 'or' and 'and'
print(a == 1 or b == 21 and c == 37)
print(a == 1 or b == 21 and c == 3)
print(a == 1 or ( b == 21 and c == 3))
print((a == 1 or b == 21 )and c == 31)


