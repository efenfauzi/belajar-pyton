memo = {0:0, 1:1}
def fib(n):
	if not n in memo:
		memo[n] = fib(n-1) + fib(n-2)
    	return memo[n]

print fib(102)


#str = "927372692193079200000"
#str2 = "927372692193078999176"

