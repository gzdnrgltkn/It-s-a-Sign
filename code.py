w1=str(input())
w2=str(input())
w3=str(input())
w4=str(input())

w1=list(w1) #Used liste function to make the word a list letter by letter
w2=list(w2)
w3=list(w3)
w4=list(w4)

w1r=w1[::-1] #these are the reverse orders of the letters
w2r=w2[::-1]
w3r=w3[::-1]
w4r=w4[::-1]

if w1r==w1 or w2r==w2 or w3r==w3 or w4r==w4: 
 print("Open")
else:
 print("Trash")
