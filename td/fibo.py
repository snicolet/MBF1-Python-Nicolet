
appels = 0

def fibo(n) :
   global appels
   appels += 1
   if n == 0 :
      return 1
   if n == 1 :
      return 1
   return fibo(n-1) + fibo(n-2)
   
for i in range(0, 100):
   appels = 0
   f = fibo(i)
   print(f, appels / f)