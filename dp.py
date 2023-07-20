def Alter(P=15,Q=10):
    P =P * Q

    Q = P / Q

    print ( P ,"#",Q)

    return Q

A = 100

B = 200

A = Alter(A, B)

print( A ,"$" ,B)
B=Alter(B)
print( A ,"$", B)

A = Alter(A)

print (A,"$",B)
