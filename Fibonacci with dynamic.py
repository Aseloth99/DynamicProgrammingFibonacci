import time
import sys
sys.setrecursionlimit(2147000000)
start=time.time()
FibArray = [0, 1]
# Fibonacci Series using Dynamic Programming 
def f(n): 
	
	# Taking 1st two fibonacci numbers as 0 and 1 
	 
	
	while len(FibArray) < n + 1: 
		FibArray.append(0) 
	
	if n <= 1: 
		return n 
	else: 
		if FibArray[n - 1] == 0: 
			FibArray[n - 1] = f(n - 1) 

		if FibArray[n - 2] == 0: 
			FibArray[n - 2] = f(n - 2) 
			
	FibArray[n] = FibArray[n - 2] + FibArray[n - 1] 
	return FibArray[n] 

	
print(f(2990)) 
stop=time.time()
print(stop-start)
