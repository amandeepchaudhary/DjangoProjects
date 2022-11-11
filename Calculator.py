print('Hello User!! Welcome to the Calculator Made by Aman.')
b = int(input('''What do you want to do:
    1 = Addition, Subtraction, Divide, Multiply  
    2 = Converting Values like CM to M
    Enter Your Choice:'''))


if b==1:
    a = float(input('Enter First Number:'))

    c = float(input('Enter Second Number:'))

    d = input('Select What you want to do with the Number +,-,*,/ :')
    if d=='+':
        print('Your Answer is:', a+c)
    elif d=='-':
        print('Your Answer is:', a-c)
    elif d=='*':
        print('Your Answer is:', a*c)
    elif d=='/':
        print('Your Answer is:', a/c)
else:
    e = float(input('Enter Number for Conversion:'))
    f = int(input('''What Conversion do you want to do:
    1 = KG to Gram
    2 = Gram to KG
    3 = M to CM
    4 = CM to M
    Enter Your Choice:'''))
    if f==1:
        print(e,'KG =',e*1000,'Grams')
    elif f==2:
        print(e,'Grams =',e/1000,'KG')
    elif f==3:
        print(e,'M =',e*100,'CM')
    elif f==4:
        print(e,'CM =',e/100,'M')
