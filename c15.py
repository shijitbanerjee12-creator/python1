import array as arr
array_num=arr.array('i',[1,3,5,3,7,9,3])
print("Og array",str(array_num))
print("The number of occurences of the number 3 in the said array is :",str(array_num.count(3)))
array_num.reverse()
print("reverse the order of the items")
print(str(array_num))