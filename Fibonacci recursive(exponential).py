import time, sys
sys.setrecursionlimit(10**6)
start=time.time()
def f(n):   #fibonacci
    if(n<0):
        print("Hatalı giriş")
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return f(n-1)+f(n-2)

    
a=f(40)  #exponential
stop=time.time()
print(a)
	
print(stop-start)
