from scipy.stats import hypergeom
import matplotlib.pyplot as plt
# Diskrete Verteilungen
# komb.u. perm. u. hypergeom. Verteilung

def main():
    zahl = 5
    # Random Program-Durchlaeufe
    print(factorial(zahl))
    print(comb(12, 30))
    print(comb(30, 12))
    print(perm(20, 2))
    print(hypergeom(6, 1, 4, 60))
    plt.show()
    exit(0)


# Fakultaet nach Produktregel
def factorial(n):
    x = 1
    for i in range(1,n+1):
        x *= i
    return x


# Kombination ohne Wdhl.
def comb(n, k):
    if n < k:
        return "N < K"
    else:
        noverk = (factorial(n) / (factorial(k) * (factorial(n - k))))
        return int(noverk)

# Permutation
def perm(n, k):
    if n < k:
        return "N < K"
    else:
        return int((factorial(n))/(factorial(n-k)))


# n - Stichprobenumfang; k - Erfolge; M - Eigenschaft; N - Gesamtumfang
def hypergeom(n, k, M, N):
    nom = (comb(M, k) * (comb((N - M), (n - k))))
    denom = comb(N, n)
    return float(nom / denom)


main()
