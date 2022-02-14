my_string= 'abcdefg' #basics
print(my_string[0]) #indexing a string
print(my_string[2:]) #slicing
print(my_string[2:5])
print(my_string[:])
print(my_string[::2])
x= my_string.split('e') #split
print(x)

x= 'Insert another string here: {}'.format('INSERT ME') #formatting
print(x)

x="Item one: {y} item two: {x}".format(x="dog",y="cat")
print(x)
