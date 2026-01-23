test_dict={'codingal':2, 'is':2, 'best':2, 'for':2, 'coding':1}
print("The origional dictionary" + str(test_dict))
K=2
res=0
for Key in test_dict:
    if test_dict[Key] == K:
        res = res+1
print("Frequency of K is : " + str(res) )