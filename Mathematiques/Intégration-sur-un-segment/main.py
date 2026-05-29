# exe 1
def Rmoins(n):
    laSommes=0
    for k in range(0,n+1):
        k_term=1/(k+n)
        laSommes=laSommes+k_term
    return laSommes
# ona
print("Rmoins(100)",Rmoins(100))
print("Rmoins(1000)",Rmoins(1000))
print("Rmoins(10000)",Rmoins(10000))
print("Rmoins(100000)",Rmoins(100000))
# donc Rmoins(1000) plus prices que Rmoins(100)

# exe 2
def f(x):
    if not 0<=x<=1: return "domain indefiner"
    return 1/(1+x)
def Tn(n):
    laPSommes=0

    for k in range(1,n):
        k_term= f(k/n)
        laPSommes= laPSommes+k_term
    moyen= (f(0)+f(1))/2
    laSommes=(1/n)*(moyen+laPSommes)
    return laSommes
# la valuer attendu 0.6931471 (calcule par l'integrale)
print("la valuer attendu 0.6931471 (calcule par l'integrale)")
print("Tn(1000)", Tn(1000))
print("Rmoins(1000)",Rmoins(1000))