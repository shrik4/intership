name = input("Enter your name: ")
print("Hello", name)

age = int(input("Enter your age: "))
print("Your age is", age)


name = "Rahul"
age = 20
print(f"My name is {name} and I am {age} years old.")


a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)



result = 10 + 2 * 5
print(result)   # Output: 20


a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True (values are same)
print(a is b)  # False (different objects in memory)




x = 5
x += 3   # x = x + 3
print(x) # 8



a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)





print(5 > 3)   # True




num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")




num = int(input("Enter a number: "))

if num > 100:
    print("It is a big number")
else:
    print("It is not a big number")
