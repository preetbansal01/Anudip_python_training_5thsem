digit = int(input("enter the number "))
l = len(str(abs(digit)))
if ( l%2 =! 0 ):
    print("number is valid ")
else :
    print("invalid number ")
half =( l / 2) + 1
for i in range (0 , half):
    if l[i] <= l[i+1] :

    else :
        ("invalid number")

for i in range ( half , l +1):
    if l[i] >= l[i+1] :

    else :
        ("invalid input")