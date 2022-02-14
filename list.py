mylist= ['stryhfgr', 1,2,3,4,0.2, True, [5,6,7]]
print(mylist)

mylist= [1,2,3]
print(len(mylist))

mylist=['a','b', 'c', 'd']
print('before reassignment')
print(mylist)

mylist[0]= 'New Item'
print('after reassignment')
print(mylist)

mylist.append("Old Item")
print(mylist)

listtwo= ['x', 'y', 'z']
mylist.extend(listtwo)
print(mylist)

mylist.pop(0)
Item= mylist.pop(0)
print(mylist)
print(Item)

mylist.reverse()
print(mylist)

mylist=[1,2,5,7,8,5]l = [3,7,[1,4,'hello']]

mylist.sort()
print(mylist)

mylist=[2,4,6,['x','y','z']]
print(mylist[3][2])

matrix=[[1,4,5],[5,6,8],[6,7,4]]
first_col= [row[0] for row in matrix]
print(first_col)
