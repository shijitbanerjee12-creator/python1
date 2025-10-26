eng=int(input("Enter marks in English"))
hin=int(input("Enter marks in Hindi"))
mat=int(input("Enter marks in Maths"))
sci=int(input("Enter marks in Science"))
sst=int(input("Enter marks in Social Studies"))
s=eng+hin+mat+sci+sst
print("Sum is",s)
per=(s/500)*100
print("Total percentage is",per)