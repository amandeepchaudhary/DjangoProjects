import re

# dicti = {'aman': 'male', 'ishu': 'female', 'sunita': 'female'}
# listi = []
# for k in dicti:
#     print(dicti[k])
#     listi.append(k)
#     print(k)
#     print(listi)
#     print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

# # di = {'aman':'male','hitesh':'male'}
# # li=[]
# # aman =di.get
# # print(aman)
# # for name,gen in di.items():
# #     li.append((name,gen))
# # print(li)
# # print("@$$$$$$$$$$$$$$$$$$$$")
# # for gen in di.get():
# #     li.append(gen)
# # print(li)

# # ?Diksha's Lab Tasks
# # Question 4: Write a Program which takes two lists as inputs and validate if they have atleast one common member
# def fun():
#     l1=[]
#     l2=[]
#     num=int(input("Enter the Number of items you want to add in the L1:"))
#     for i in range(num):
#         l1.append(input(f"Enter the value to add in L1 at index {i}:"))

#     num2=int(input("Enter the Number of items you want to add in the L2:"))
#     for i1 in range(num2):
#         l2.append(input(f"Enter the value to add in L2 at index {i1}:"))
        
#     print(l1)
#     print(l2)

#     execute =0
    
#     for ele in l1:
#         if ele in l2:
#             execute = execute + 1
#     if not execute:
#         print("List is Invalid")
#     else:
#         print("List is Valid",l1+l2)
    

# # fun()

# # Question 3: Write a program to check if the input number is a palindrome number or not
# def Palindrome():
#     number = int(input("Enter a Number to Check whether it is a Palindrome or Not:"))
#     reverse = 0
#     orinum = number
#     # for i in range(number):
#     while number>0:
#         reverse = (reverse*10)+(number%10)
#         number = number//10
    
#     if orinum==reverse:
#         print("This number is a Palindrome")
#     else:
#         print("This number is not a Palindrome")


# Palindrome()

# cost_price = int(input("Enter the Cost Price:"))
# selling_price = int(input("Enter the Selling Price:"))

# # calculate profit or loss amount and print it
# if cost_price>selling_price:
#     lp = cost_price - selling_price
#     # lp = lp*(-1)
#     print(lp)
# else:
#     lp = cost_price - selling_price
#     print(lp)



#/ Regular Expression (Redux)
its_me = '''+91 8178750436
+91 4672636278 +91 7867676768 +91 1234567890'''
pattern = re.compile(r'\d{10}')

matching = pattern.finditer(its_me)
for match in matching:
    print(match)