#temp = eval(input('enter a temperature in celsius: '))
#print('In Fahrenheit, that is',9/5*temp+32)

num1 = eval(input('enter first number: '))
op = input('enter an operator: ')
num2 = eval(input('second number: '))
sum = num1 + num2
diff= num1 - num2
mult= num1*num2
div = num1/num2
mod = num1%num2
if op=='+':
    print('sum is: ',sum)

elif op=='-':
    print('differnt is: ',diff)

elif op=='*':
    print('multiplication is: ',mult)

elif op=='/':
    print('the divison is: ',div)
elif op=='%':
    print('the modulus is: ',mod)     
else:
     print('wrong operator')
           
            
        


