import time
start=time.time()

# Function for nth fibonacci number - Space Optimisataion

def f(n): 
    a = 0
    b = 1
    if n < 0: 
        print("Incorrect input") 
    elif n == 0: 
        return a 
    elif n == 1: 
        return b 
    else: 
       for i in range(2,n+1): 
            c = a + b 
            a = b 
            b = c 
    return b 

print(f(2990))
stop=time.time()
print(stop-start)
