num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum1 = 0
sum2 = 0
for i in range(1,num1):
	if(num1 % i == 0):
		sum1 = sum1 + i
for i in range(1,num2):
	if(num2 % i == 0):
		sum2 = sum2 + i
if(sum1 == num1 and sum2 == num2):
	print("Friendly Pair")
else:
	print("Not Friendly Pair")