a = {30,40,70,20,80,50}
b = {20,50,60,40,90,10}
print("Original sets:")
print("A :",a)
print("B : ",b)
res1 = a.symmetric_difference(b)
print("\nSymmetric Difference of a - b:",res1)
res2 = b.symmetric_difference(a)
print("\nSymmetric Difference of b - a:",res2)