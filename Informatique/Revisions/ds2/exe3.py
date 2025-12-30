x=float(input("x: "))
n=int(input("n: "))
if x <= 0 or n <= 0:
    print("Valeurs invalides")
else:
    RESULTA=0

    for i in range(1,n+1,1):
        terms_i= (-1)**(i+1)*(((x-1)**i)/i)
        RESULTA += terms_i

    print(RESULTA)