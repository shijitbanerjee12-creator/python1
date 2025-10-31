CP=int(input("Enter Cost Price"))
SP=int(input("Enter Selling price"))
if SP>CP:
    print("Profit")
    A=SP-CP
    print("Amount is",A)
else:
    print("Loss")
