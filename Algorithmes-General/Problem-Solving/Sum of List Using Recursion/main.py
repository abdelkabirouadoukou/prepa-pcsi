def test(n):
    if 1<=n<=100:
        if n%2 != 0:
            return "Weird"
        elif 2<=n<=5 and n%2==0:
            return "Not Weird"
        elif 6<=n<=20 and n%2==0:
            return "Weird"
        elif n>=20 and n%2==0:
            return "not Weird"
            
print(test(42))