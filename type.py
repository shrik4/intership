# var1 = "hello world!"
# print("hi "+ var1[0:6]+"python " +var1[6:8]+"R"+ var1[9:])

name = 'shrikar'
name.center(30)
print(name.center(30))


string = "yashvi is a trainer "
substring = "i"
count = string.count(substring)
print("the count is:",count)



string = "who is he "
print(string.count('i'))



string = "yashi is a trainer "
print(string.count('i',7,19))



string1 = 'thisis34'
print(string1.isalnum())

string2 = "whatisthiswewlief jweihfowue1212313"
print(string2.isalnum())

string3 = "what@wht"
print(string3.isalnum())


num = "this is string examole "
print(num.isalnum())


num2 = "this_is_string_explain!!"
print(num2.isalnum())

number = "12@1"
print(number.isdigit())


string = "indhushree"
print(string.capitalize())


string6 ="shrikar" 
print(string6.upper())

app = "arfian"
print(app.swapcase())


splite = "indu shree ramya"
print(splite.split())
print(splite.split(' ',1))




splite1 = "line1-abcdef line2-abc  \nline4-abcd"
print(splite1)





reply = "shrikar is number 1"
print(reply.replace("shrikar","sarthak"))



print(":".join(reply))