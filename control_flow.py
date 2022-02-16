if 1<2:
    print("First block")
    if 20<3:
        print("second block")

if 1>2:
    print('yes')
elif 3==3:
    print("elif ran")
else:
    print("No")

#for loops
seq= [1,2,3,4,5,7,8]
for item in seq:
    #code block
    print(item)

#Using for loops in Dictionary
d={"sam":1, "David":2, "Owen":3}
for k in d:
    print(k)
    print(d[k])

mypairs= [(1,2),(3,4),(5,6)]
for (tup1,tup2) in mypairs:
    print(tup1)
    print(tup2)

#While Loops, it allows you to perform an action until the condition becomes true
i= 3
while i<10:
    print("i is: {}".format(i))
    i+=1

#range, helps us in getting integers: The first parameter is starting index position and the last parameter is ending index position
list(range(0,5))
list(range(0,20,2))

for item in range(10):
    print(item)

#list comprehension
x= [1,2,3,4,5]

out=[num**2 for num in x]
print(out)
