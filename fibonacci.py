def fib(N):
	if N == 0:
		return 1
	if N == 1:
		return 1
	return fib(N-1)+fib(N-2)
	
for i in range(8):	
	print(fib(i))
