def f1(x):
    calculed= int(x-3)
    return calculed
def dichotomie(f,a,b, n):
    if f(a)*f(b) > 0:
        return "il n'existe pas au moins un reel c ∈ [a,b] tel que f(c) = 0"
    else:
        for i in range(a,b,n):
            m=(a+b)/2
            if f(m) == 0:
                return m
            elif f(b)*f(m) <= 0:
                a=m
            else:
                b=m
x1=dichotomie(f1,-1,4,65)
print(x1)
print(f1(x1))