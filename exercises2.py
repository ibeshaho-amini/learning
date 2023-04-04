#Question1
""" for i in range(100):
    print('Amini')
"""

#Question2
"""for i in range(5):
    print('Amini',end=' ')
    print('Amini')
"""
#Question3
""" for i in range(100):
    print(i+1,'Amini')
"""

#Question4
"""for i in range(1,21):
    print(i+1,'---',i ** 2)
"""
#Question5
"""for i in range(8,90,3):
    print(i)
"""
#Question6
"""for i in range(100,1,-2):
    print(i)
"""
#Question7
"""for i in range(5):
    print('A'*i,end=' ')
    for i in range(3,5):
        print('B'*i,end=' ')
        for i in range(1,4):
            print('C'*i,end=' ')
            print('D'*i,end=' ')
            print('E'*i,end=' ')
            for i in range(2,4):
                print('F'*i,end=' ')
            print('G',end=' ')
"""
#Question8
"""user=input('Enter your name: ')
num=eval(input('Enter the times you want it to be dspalyed: '))
for i in range(num):
    print(user)
"""
#Question9
"""result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (column > 1 and column < 5))):    
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);"""
#Q11
"""row=int(input('enter number of rows:'))
col=int(input('enter number of columns:'))

for i in range(row):
    for j in range(col):
        if(i==0 or i==row-1 or j==0 or j==col-1):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    """
#q12
"""for i in range(4):
    print('*'*(1+i))"""
#q13
"""for i in range(7,3):
    for j in range(7,2):
        print('*'*(i+1))
"""
