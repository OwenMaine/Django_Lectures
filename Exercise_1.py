s= 'django'
print(s[0])
print(s[2])
print(s[:4])
print(s[1:4])
print(s[4:])
def reverse(s):
    if len(s)==0:
        return s
    else:
        return reverse(s[1:]) + s[0]

s= "django"
print("This is reversed using recursion :", end="")
print(reverse(s))


list = [3,7,[1,4,'hello']]
list[2][2]= 'goodbye'
print(list)

d1 = {'simple_key':'hello'}

d2 = {'k1':{'k2':'hello'}}

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}

print(d1['simple_key'])
print(d2['k1']['k2'])
print(d3['k1'][0]['nest_key'][1])

mylist = set([1,1,1,1,1,2,2,2,2,3,3,3,3])
print(mylist)

age= 4
name= 'sammy'

x='The name of my dog is: {name} He is :{age} years old'.format(name='sammy',age=4)
print(x)
