#program for adding numbers
series = [int(x) for x in input("Enter the numbers to add: ").split()]
def addition(numbers):
	sum=0
	for x in numbers:
		sum+=x
        return sum

sum_of_numbers = addition(series)
print(f"Addition of the given numbers is {sum_of_numbers}")
