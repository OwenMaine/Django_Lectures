my_stuff= {'key1': 1234, 'key2': 'pairs','key3': {'1,2,3' : [1,2,3, 'grabme']}}
print(my_stuff ['key3'] ['1,2,3'][3].upper())

my_stuff= {'food':'pizza','bfast': 'egg'}
my_stuff['food']='Egusi'
print(my_stuff['food'])

#tuple
t= ('a','1,2,3',123,True)
print(t[1]) #N:B tuple is immutable

#set: They are unordered collection of unique elements
x= set()

x.add(1)
x.add(2)
x.add(0.1)
x.add('Numbers')
print(x)

#sets only identify unique Numbers
converted = set([1,1,1,1,2,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5])
print(converted)
