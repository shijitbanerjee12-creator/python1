def total(bill,tip):
    tot=bill*(1+0.01*tip)
    tot=round(tot,2)
    print(f"Please pay ₹{tot}")
total(150,20)