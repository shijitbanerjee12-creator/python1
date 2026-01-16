L=[2,3,4,7,5,8,9,1,3]
print("Origional list", L)
count=0
for i in L:
    count +=i
avg=count/len(L)
print("Sum =",count)
print("Average = ",avg)
L.sort()
print("Smallest element is",L[0])
print("Largest element is",L[-1])