a = "hello"
print(a[::-1])


b = [1,2,3,476,5,9]
print(max(b))


monday= 45
tuesday = 56
avg = (monday+tuesday)/2
print(avg)

# aList = [123,'xyz','zara','abc']
# aList[2] = 58 +34

# aList = "sharikar"
# aList.append(2006)
# print("after",aList)



# print("popped elements",aList.pop())
# print("list after pop",aList)


list = [123,'xyz','tommy','abc',123]
list.reverse()
print(list)







blist =[6,7,8,9]
blist.sort()
print(blist)
blist.sort(reverse=True)
print(blist)


clist = [123,"shrikar",234,"shrikar",123]
print(clist.count(123))


list1 = [1,2,3]
list2 = [1,2,3]

print(1+2)
print('a'+'b')

list3 = list1 +list2
print(list3)


print(list1 * 3)
dir(list)


tup1 = ()
tup1

tup1 = (50, )
print(tup1 [1:5])

tup1 = (12,34.56)
tup2 = ('abc','xyz')

tup3 = tup1 + tup2
print(tup3)


tup = (1,2,3,4,5,2,2)
print(tup.index(2))
print(tup)

del()
print(tup)



# dir(tuple)
# help(tuple)

dict1 = {'name':'aditya','age':40,'bike':'honda'}
print(dict1['name'])
print(dict1['age'])

dict1['age'] = 9
dict1['school'] = "DPS School"
dict1['Salary'] = 50000


print(dict1['age'])
print(dict1['school'])
print(dict1["Salary"])



# print(dict1)

print(dict1.keys())
print(dict1.values())
print(dict1.items())



del(dict1['name'])
dict1



dict1.clear()
print(dict1)


normal_set = {'a','b','c','d'}
print(normal_set)

normal_set.add("d")
print(normal_set)



set1 = {1,2,3}
set2 = {1,9,0}
intersection_set = set.intersection(set2)
print(intersection_set)
set3 = set1 & set2


print("union of set & se2 is : set3 =",set3)

