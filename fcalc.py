print("ENTER THE FIRST NUMER")
num1=int(input())
print("ENTER THE OPERATER"  '+','-','*','/')
opert=(input())
print("ENTER THE SECOND NUMER")
num2=int(input())
if num1 ==45 and opert =='*' and num2 ==3:
    print(555)
elif num1 == 56 and opert == '+' and num2 == 9:
        print(77)
elif num1==56 and opert =='/' and num2==6:
    print(4)
#nw handle actual calc
elif opert =='+':
    plus=num1+num2
    print("the sum of two numbber" , plus)
elif opert =='*':
    mul=num1*num2
    print("the mul of two numbber" ,mul)
elif opert =='-':
    sub=num1-num2
    print("the sub of two numbber" ,sub)
elif opert =='/':
    div=num1/num2
    print("the div of two numbber" , div)
else:
    print("unexpected input")