# def cal_avg(a,b,c):
#     sum = a+b+c
#     avg=sum/3
#     print(avg)
#     return avg
# cal_avg(1,2,3)


def converter(usdval):
    inrval = usdval * 83
    print(usdval,"USD =",inrval,"INR")

converter(23)






def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
show(5)