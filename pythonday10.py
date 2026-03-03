# matplotlib is used to create a charts like line ,bar, pie,histogram,scatler plots 
import matplotlib.pyplot as plt

# x = [1,2,3,4]
# y = [10,20,25,30]
# plt.plot(x,y)
# plt.show()


#plot()
#show()


# days= ['sun','mon','tue','wen','the','fri','sat']
# x = [1,2,3,4,5,6,7]
# plt.plot(days,x)
# plt.show()
# plt.title("days vs study hours")
# plt.xlabel(days)
# plt.ylabel(x)



# months = ['jan','feb','mar','apr','may','jun','july','aug','sep','oct','nov','dec']
# sales = [121321,1212,1212232,3221,2434,4567,5667,67889,1234,4567,6789,9453]
# plt.plot(months,sales)
# plt.title("months vs sales")
# plt.xlabel(months)
# plt.ylabel(sales)
# plt.show()



# plt.bar(["python","SQL","linxe"],[80,70,90])
# plt.title("subject marks comparison")
# plt.xlabel("sub")
# plt.ylabel("mark")
# plt.show()



# plt.bar(["sarthak","shrikar","arfine"],[80,70,10])
# plt.title("subject marks comparison")
# plt.xlabel("sub")
# plt.ylabel("mark")
# plt.show()


# plt.bar(["shamp","band","hair fall"],[21213,12170,212110])
# plt.title("sales of the product")
# plt.xlabel("product")
# plt.ylabel("sales")
# plt.show()



# plt.bar(["windows","android","linex"],[21213,12170,212110])
# plt.title("no of users per platform")
# plt.xlabel("platform")
# plt.ylabel("users")
# plt.show()



# plt.pie([60,23,44,56],labels=["python",'java',"c++","js"])
# plt.title("programing lang usage ")
# plt.xlabel("size")
# plt.ylabel("prpgam")
# labels = ["study","sleep","entertainment","exercise"]
# sizes = [6,8,4,2]
# plt.pie(sizes,labels=labels,autopct = "1.1f%%")
# plt.title("dailt activity distribution")
# plt.show()



# plt.pie(labels=["rent","food","travel","shopping"],expenses=[40,25,20,15])
# plt.title("programing lang usage ")
# # plt.xlabel("size")
# # plt.ylabel("prpgam")
# labels = ["study","sleep","entertainment","exercise"]
# sizes = [6,8,4,2]
# # plt.pie(labels,labels=labels,autopct = "1.1f%%")
# plt.title("dailt activity distribution")
# plt.show()




# height = [150,160,165,170,175]
# weight = [50,60,65,70,75]

# plt.scatter(height,weight)
# plt.title("height vs weight")
# plt.xlabel("height" )
# plt.ylabel("marks")
# plt.show()



# expeniences = [15000,16000,16500,17000,17500]
# salary = [50000,60000,65000,70000,75000]

# plt.scatter(expeniences,salary)
# plt.title("expeniences vs salary")
# plt.xlabel("expeniences" )
# plt.ylabel("salary")
# plt.show()




# temperature = ["20 c","25c","36c","40c","45c"]
# ice_cream = [50000,60000,65000,70000,75000]

# plt.scatter(temperature,ice_cream)
# plt.title("temperature vs icecream")
# plt.xlabel("temperature" )
# plt.ylabel("ivecream")
# plt.show()



marks = [40,59,40,50,45,65,70,72,80]
plt.hist(marks)
plt.xlabel("marks pange")
plt.ylabel("number of students")
plt.title("marks disstribution")
plt.show()