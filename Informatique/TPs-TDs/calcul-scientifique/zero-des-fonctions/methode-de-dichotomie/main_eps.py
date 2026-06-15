def f1(x):
    return x**2 -2
def Dichotomie(f,a,b,eps):
    if f(a)*f(b) > 0: return "il n'existe pas au moins un reel c ∈ [a,b] tel que f(c) = 0."
    while abs(f(m))>eps:
        m=(a+b)/2
        if f(m) == 0:
            return m
        elif f(a)*f(m) <= 0:
            b=m
        else:
            a=m
    return m
x1=Dichotomie(f1,0,3,20)
print(x1)
print(f1(x1))