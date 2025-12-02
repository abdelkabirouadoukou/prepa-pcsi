a = int(input("a: "))
b = int(input("b: "))

for i in range(min(a, b), 0, -1):
    if a % i == 0 and b % i == 0:
        print("Plus grand diviseur commun :", i)
        break

for i in range(1, min(a, b)+1):
    if a % i == 0 and b % i == 0:
        print("Plus petite diviseur commun :", i)
        break
