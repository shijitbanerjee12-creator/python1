units=int(input("Enter number of units consumed"))
if (units<50):
    amt=units*2.60
    surcharge=25
elif (units<=100):
    amt=130+((units-50)*3.25)
    surcharge=35
elif (units<=200):
    amt=130+162.50+((units-100)*5.26)
    surcharge=45
else:
    amt=130+162.50+526+((units-200)*8.45)
    surcharge=75
t=amt+surcharge
print(" Electricity bill = %.2f" %t)