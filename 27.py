eng=int(input("Enter marks in English"))
hin=int(input("Enter marks in Hindi"))
mat=int(input("Enter marks in Maths"))
sci=int(input("Enter marks in Science"))
sst=int(input("Enter marks in Social Science"))
tot=eng+hin+mat+sci+sst
avg=tot/5
if avg>90 and avg<100:
    print("A1")
elif avg>80 and avg<90:
    print("A2")
elif avg>70 and avg<80:
    print("B1")
elif avg>75 and avg<80:
    print("B2")
elif avg>65 and avg<75:
    print("C1")
elif avg>60 and avg<65:
    print("C2")
elif avg>55 and avg<60:
    print("D1")
elif avg>45 and avg<55:
    print("D2")
elif avg>30 and avg<45:
    print("E1")
elif avg>0 and avg<30:
    print("E2")
else:
    print("Invalid Input")