num = 10

if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")



num = 15

if num > 0:
    if num % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
else:
    print("Number is not positive")



num = int(input("Enter a number: "))

if num > 0:
    print("Number is Positive")
elif num < 0:
    print("Number is Negative")
else:
    print("Number is Zero")


l = [1, 2]
l.append(3)
print(l)

l = [1, 2]
l.extend([3, 4])
print(l)

l = [1, 3]
l.insert(1, 2)
print(l)

l = [1, 2, 3]
l.remove(2)
print(l)

l = [1, 2, 3]
l.pop()
print(l)

l = [1, 2, 3]
l.clear()
print(l)

l = [10, 20, 30]
print(l.index(20))

l = [1, 2, 2, 3]
print(l.count(2))

l = [3, 1, 2]
l.sort()
print(l)

l = [1, 2, 3]
l.reverse()
print(l)

l = [1, 2, 3]
new_l = l.copy()
print(new_l)
