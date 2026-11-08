from sympy import *
import matplotlib.pyplot as plt



def eulerProd():
    ergebnis = 1
    speicher = list()
    for i in range(100000):
        if isprime(i):
            ergebnis *= (1-1/i)**(-1)
            speicher.append((i,ergebnis))
    print(ergebnis)
    return speicher

'''
plot vom Eulerprodukt gegen einen logarithmus

lot = eulerProd()
X, Y = map(list, zip(*lot))
k = plt.plot(X,Y,'ko')
Y2 = [1.5*log(x) for x in X]
k += plt.plot(X,Y2,'--')
plt.show()
'''

def mobius(N) :
     
    # Base Case
    if (N == 1) :
        return 1
 
    # For a prime factor i
    # check if i^2 is also
    # a factor.
    p = 0
    for i in range(1, N + 1) :
        if (N % i == 0 and
                isprime(i)) :
 
            # Check if N is
            # divisible by i^2
            if (N % (i * i) == 0) :
                return 0
            else :
 
                # i occurs only once,
                # increase f
                p = p + 1
 
    # All prime factors are
    # contained only once
    # Return 1 if p is even
    # else -1
    if(p % 2 != 0) :
        return -1
    else :
        return 1

'''
Moebius Funktion bei werten -1  anschauen vergleich zusammengesetzte zahlen blau vs primzahlen
in lila

valueMoebius = [mobius(n) for n in range(1,1000)]
k = plt.plot([x for x in range(1,1000)], valueMoebius,'o')
primetrue=[]
for i in range(1,1000):
    if isprime(i):
        primetrue.append(1)
    else:
        primetrue.append(0)
k += plt.plot([x for x in range(1,1000)], [valueMoebius[i]*primetrue[i] for i in range(0,999)],'bo')        
plt.show()
'''
def poly1(x):
    return x**4+1
def poly2(x):
    return x**5+1
def w(t):
    return log(poly1(t))*log(poly2(t))
X = [x for x in range(1,100)]
Y1 = [w(t) for t in range(1,100)]
Y2 = [20*log(x)**2 for x in range(1,100)]
k = plt.plot(X,Y1,'ro')
k += plt.plot(X,Y2,'bo')
plt.show()