import numpy as np
import matplotlib.pyplot as plt

def pgcd(a, b) :
    a = abs(a)
    b = abs(b)
    if a < b :
       a,b = b,a
    if b == 0 :
       return a
    else :
       return pgcd(b, a % b)
       
def avatar(n) :
    a = np.ones(n, dtype="int")
    for i in range(2, n) :
        d = pgcd(a[i-1], i)
        if d > 1 :
            a[i] = a[i-1] / d
        else :
            a[i] = a[i-1] + i + 1
    return a

# taken from https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188
def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n//3 + (n%6==2), dtype=bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0][1:]+1)|1)]


def f(n) :
    b = bin(n)[2:]  # b = binary form of n
    r = b[::-1]     # r = reverse of b
    m = int(r, 2)   # m = decimal value of the reverse
    return n - m

def binary_and_reverse(n) :
   primes = primesfrom2to(n)
   
   a = np.zeros(len(primes), dtype="int")
   for k in range(len(primes)) :
       a[k] = f(primes[k])
   return a

def graph(a) :
    n = len(a)
    x = np.arange(0, n)
    fig, ax = plt.subplots()
    fig.set_size_inches(12, 8)
    plt.scatter(x, a, s=50, marker="+")
    plt.show()
    return
    

print(primesfrom2to(100))
print(binary_and_reverse(100))

#graph(binary_and_reverse(500))
#graph(binary_and_reverse(5000))
graph(binary_and_reverse(50000))

#graph(avatar(500))
#graph(avatar(1000))


