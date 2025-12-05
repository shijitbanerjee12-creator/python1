string=input("Enter your own word")
chr=input("Enter your charachter")
i=0
count=0
while(i<len(string)):
    if(string[i]== chr):
        count=count+1
    i=i+1
print("The total number of times",chr,"has occured is",count)