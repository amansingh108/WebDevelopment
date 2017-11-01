from functools import lru_cache

@lru_cache (maxsize = 1000)
def fibonaci(n):
	if n == 1 or n ==2:
		return 1
	return fibonaci(n-1) + fibonaci(n-2)


for n in range(1,1001):
	print("Current Number :" , n , "Value :",fibonaci(n)) 



def factorial(n):
	if n<=1:
		return 1
	else:
		return n* factorial(n-1)

if __name__ == '__main__':
	factorial()
