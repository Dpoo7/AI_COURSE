#elif

a= [10,20,30]
b=[11,22,33]
c=[111,222]

if(len(a) > len(b)) and (len(a) > len(c)):
    print("List A is Maximum")

elif(len(b)>len(a)) and (len(b)>len(c)):
    print("List B is Maximum")

elif(len(c)>len(a)) and (len(c)>len(b)):
    print("List C is Maximum")

else:
    print("All are equale")