def fibo():
	runningSum = 0
	prevPrevFib = 0
	prevFib = 1
	currentFib = 1
	while currentFib < 4000000:
		if currentFib % 2 == 0:
			runningSum += currentFib
		prevPrevFib = prevFib
		prevFib = currentFib
		currentFib = prevPrevFib + prevFib
		print currentFib, prevFib
	print runningSum
	return runningSum

if __name__ == "__main__":
	fibo()