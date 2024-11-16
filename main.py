#sortin
# x=input('enter an arry of values').split()
# x=[int(x[i])for i in range(len(x))]
# for i in range(len(x)):
#     for j in range (i+1,len(x)):
#         if x[i]<x[j]:
#             t=x[i]
#             x[i]=x[j]
#             x[j]=t
# print(x)
#multiplecation table
# n=int(input('enter a number'))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print('%-5d'% (i*j), end=' ')
#     print()

# sum=0
# count=0
# tocountinue= True
# while tocountinue:
#     sum+=int(input('enter the number'))
#     count+=1
#     question=input('would you like to continue Y/N')
#     if question == 'N' :
#         tocountinue = False
# avg=sum/count
# print(avg)

# num=int(input('eneter the number'))
# factorial= 1
# i=2
# limit= False
# while i<= num:
#     if factorial<= 1000000 :
#         factorial*=i
#         i+=1
#     else:
#         limit=True
#         break
#

# sum=1
# i=2
# while sum<10000 :
#     sum+=i**2
#     i+=1
# print(i-1)

# listOne = input("Enter list one: ").split()
# listTwo = input("Enter list two: ").split()
# result = []
# if len(listOne) == len(listTwo):
#     i = 0
#     while i < len(listOne):
#         result.append(int(listOne[i]) - int(listTwo[i]))
#         i += 1
#     print("The result:", end=" ")
#     for i in result:
#         print(i, end=" ")
# else:
#     print("The two lists must be equal")
#
# listOne = input("Enter list one: ").split()
# listTwo = input("Enter list two: ").split()
# occurrence = []
# for i in listOne:
#     counter = 0
#     for j in listTwo:
#         if j == i:
#             counter += 1
#     occurrence.append(counter)
# for i in range(len(listOne)):
#     print(f"Number {listOne[i]} occurs {occurrence[i]} time(s)")

# n=int(input('enter the number'))
# for i in range(n):
#         print(f'%{i}s*' % '')
# for i in range(n-1,-1,-1):
#     print(f'%{i}s*' % '')


