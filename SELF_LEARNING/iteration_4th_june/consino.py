digit = int(input("enter the digit="))
s= str(digit)
l = len(str(abs(digit)))
#if (l == 0 ):
    #print("invalid digit ___")
if(l == 1):
    print(digit)
elif(l>=2):
    for i in range (0,l-1):
      if   s[i] <= s[i+1] :
        print("valid digit ")
