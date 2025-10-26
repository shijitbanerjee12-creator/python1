amount=int(input("Enter amount to be withdrawn"))
note_1=amount//100
print("No. of Rs. 100 notes are",note_1)
note_2=(amount%100)//50
print("No. of Rs. 50 notes are",note_2)
note_3=((amount%100)%50)//10
print("No. of Rs 10 notes are",note_3)