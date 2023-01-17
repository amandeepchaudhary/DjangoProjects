print('Hello User!! Welcome to the Calculator Made by Aman.')
b = int(input('''What do you want to do:
    1 = Addition, Subtraction, Divide, Multiply, Power, Percent
    2 = Converting Values like CM to M
    Enter Your Choice:'''))


if b==1:
    d = int(input('''Select What you want to do with the Number 
        1 = +,-,*,/ 
        2 = ^
        3 = %
        Enter Your Choice:'''))
    if d==1:
        a = float(input('Enter First Number:'))

        c = float(input('Enter Second Number:'))

        d1 = input('Select What you want to do with the Number (+,-,*,/):')
        if d1=='+':
            print('Your Answer is:', a+c)
        elif d1=='-':
            print('Your Answer is:', a-c)
        elif d1=='*':
            print('Your Answer is:', a*c)
        elif d1=='/':
            print('Your Answer is:', a/c)
        else:
            print('Enter a Valid Choice!!')

    if d == 2:
        d21 = int(input('Enter Number:'))
        d22 = int(input('Enter Power (Square=2,Cube=3,etc):'))
        def power(self,power1):
            self.pw = power1
            def powerwork():
                if self.pw == 2:
                    print(d21*d21)
            return powerwork()
        # if d22 == int:
            # power({power1: d22})


    if d == 3:
        d3 = int(input('%/ of Number is = 1 OR Number to % = 2 Simple % = 3'))
        if d3 ==1:
            d31 = int(input('Enter the %:'))
            d32 = int(input('Enter the Number:'))
            d33 = (d31/100) * d32
            print(f'%d% of %d is %d',d31,d32,d33)
        if d3 ==3:
            d39 = int(input('For how many number you wanna get the %:'))
            li = []
            i = 0
            while i<d39:
                li.append(int(input('Enter the Number:')))
                i+=1

            for j in range(len(li)):
                print(li[j])
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
