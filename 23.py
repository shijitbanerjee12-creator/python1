ly=int(input("Enter an year"))
if (ly%400==0)or(ly%100!=0)and(ly%4==0):
   print("Leap year")
else:
   print("Not a leap year")