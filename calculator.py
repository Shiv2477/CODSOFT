def calculate(n1,n2,op):
	if op=='+':
		result=n1+n2
	elif op=='-':
		result=n1-n2
	elif op=='*':
		result=n1*n2
	elif op=='/':
		result=n1/n2
	elif op=='^':
		result=n1^n2
	return result
number1=float(input('Enter the first number:'))
op=input('Enter the operator(+,-,*,/,^)')
number1=float(input('Enter the second number:'))
print(number1,op,number2)
result=calculate(number1,number2,op)
print('=',result)



