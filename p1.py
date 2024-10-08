# steps:
# take two numbers from users
# add those value
# display the result

# sudo code
# integer a,b
# add value to a,b
# display thosse numbers

# python code
# a=int(input('a: '))
# b=int(input('b: '))
# c=a+b
# print(c)

# '''program to swap to values'''
# a=int(input('a: '))
# b=int(input('b: '))
# print(f"before swapping\na:{a}\tb:{b}")
# c=a
# a=b
# b=c
# print(f"after swapping\na:{a}\tb:{b}")

# '''swapping the values without temporary value using +,-'''
# a=int(input('a: '))
# b=int(input('b: '))
# print(f"before swapping\na:{a}\tb:{b}")
# a=a+b
# b=a-b
# a=a-b
# print(f"after swapping\na:{a}\tb:{b}")

# a=int(input('a: '))
# b=int(input('b: '))
# print(f"before swapping\na:{a}\tb:{b}")
# a=a*b
# b=a//b
# a=a//b
# print(f"after swapping\na;{a}\tb:{b}")

# a=int(input('a: '))
# b=int(input('b: '))
# print(f"before swapping\na:{a}\tb:{b}")
# a=a|b
# b=a|b
# a=a|b
# print(f"after swapping\na:{a}\tb:{b}")

# a=int(input('a: '))
# b=int(input('b: '))
# print(f"before swapping\na:{a}\tb:{b}")
# a,b=b,a
# print(f"after swapping\na:{a}\tb:{b}")

# n=int(input('n: '))
# if n%2!=0:
#     print(f"{n}is odd")
# else:
#     print(f"{n}is even")

# n=int(input('n: '))
# if((n//2)*2)!=n:
#     print(f"{n}is odd")
# else:
#     print(f"{n} is even")

# n=int(input('n: '))
# if n&1==1:
#     print(f"{n}is odd")
# else:
#     print(f"{n}is even")

# n=int(input('n: '))
# if n|1!=n:
#     print(f"{n} is even")
# else:
#     print(f"{n} is odd")

# n=int(input('n: '))
# if (n>>1)<<1==n-1:
#     print(f"{n} is odd")
# else:
#     print(f"{n} is even")

# n=int(input('n: '))
# if (n>>1)<<1!=n:
#     print(f"{n} is odd")
# else:
#     print(f"{n}is even")

# print('*')
# print('*')

# for i in range(4):
#     print('*')

# row=int(input('row: '))
# col=int(input('col: '))
# val=1
# for i in range(row):
#     for j in range(col):
#         print(val,end=" ")
#     print()
#     val+=1
#     if val>9:
#         val=1

# row=int(input('row: '))
# col=int(input('col: '))
# for i in range(row):
#     val=1
#     for j in range(col):
#         print(val,end=" ")
#         val+=1
#         if val>9:
#             val=1
#     print()

# row=int(input('row: '))
# col=int(input('col: '))
# val=row
# if val>9:
#     val=9
#     for i in range(row):
#         for j in range(col):
#             print(val,end=" ")
#         print()
#         val-=1
#         if val<1:
#             val=9
# row=int(input('row: '))
# col=int(input('col: '))
# for i in range(row):
#     val=col
#     for j in range(col):
#         print(val,end=" ")
#         val-=1
#         if val>4:
#          val=4
#     print()
        
        
# n=int(input('n: '))
# val=ord('A')+n-1
# for i in range(n):
#     for j in range(n):
#         if i==j:
#           print(chr(val),end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#     val-=1

# row=int(input('row: '))
# col=int(input('col: '))
# val=row
# for i in range(row):
#   for j in range(col):
#     print(val,end=" ")
#   print()
#   val-=1

# row=int(input('row: '))
# col=int(input('col: '))

# for i in range(row):
#   val=ord('C')


#   for j in range(col):
#       print(chr(val),end=" ")
#       val-=1
   
#   print()

# row=int(input('row: '))
# col=int(input('col: '))
# val=ord('A')
# for i in range(row):
#   for j in range(col):
#     print(chr(val),end=" ")
#     val+=1
#     if val>ord('A'):
#       val=ord('A')
#   print()
#   # if val>ord('A'):
#   #   val=ord('A')


# n=int(input('n: '))
# val=1
# for i in range(n):
 
#   for j in range(n):
#     if i==j:
#       print(val,end=" ")
#       val+=1
      
#     else:
#       print("0",end=" ")
#   print()
  
  
# n=int(input('n: '))
# val=1
# for i in range(n):
 
#   for j in range(n):
#     if i*j:
#       print(val,end=" ")

#   print()
#   val+=1

# n = 5  # Number of rows
# n=int(input('n: '))
# for i in range(1, (n // 2) ):  # Loop to handle number and asterisk lines
#     print("1 " * n)  # Print line of numbers (replacing "1" with the appropriate number)
#     print("* " * n)  # Print line of asterisks

# for i in range(1, (n // 2) + 1):
#     print(f"{i + 1} " * n)  # Print the next sequence of numbers
#     if i < (n // 2):
#         print("* " * n)  
        
# n=int(input('n: '))
# val=1
# for i in range(n):
#   if(1,(n//2)):
#     print(val,*"n")
#     print('*',*"n")
# for j in range(n):
#   if(1,(n//2)+2):
#     print(f"{i+1}"*"n")
#     if i < (n//2):
#       print("*",*"n")    
  
  
# n=int(input('n: '))
# val1=ord('A')
# val2=1
# for i in range(n):
#     for j in range(n):
#         if i==j:
#             if(i%2==0):
#                print(chr(val1),end=" ")
#                val1+=1
#             else:
#                 print(val2,end=" ")
#                 val2+=1
           
            
#         elif i>j:
#              print("*",end=" ")
      
#         else:
#             print("-",end=" ")
#     print()
    


# p=True
# n=int(input('n: '))
# val1=1
# val2=ord('A')

# for i in range(n):
#     for j in range(n):
#         if p:
#             print(val1,end=" ")
#             val1+=1
#             p = False
            
#         else:
#             print(chr(val2),end=" ")
#             val2+=1
#             p=True
            
#     print()
#     if val1>9:
#       val=1

# n=int(input())   
# c=0
# for i in range(1,n+1):
#     if n%i==0:
#         c+=1
# if c==2:
#     print(f"{n} is prime number")
# else:
#     print(f"{n} is not prime number")

# n=int(input())
# p=len(str(n))
# s=0
# temp=n
# while n>0:
#     rem=n%10
#     s+=rem**p
#     n=n//10
# print(temp==s)

# n=int(input())
# for i in range(2,n+1):
#     factor=0
#     for j in range(2,i//2+1):
#         if i%j==0:
#             factor+=1
#             break
#         if factor==0:
#             print(i,end=" ")

# n=int(input())
# for i in range(1,n+1):
#     p=len(str(i))
#     temp=i
#     s=0
#     while temp>0:
#         rem=temp%10
#         s+=rem
#         temp=temp//10
#         if s==i:
#             print(i,end=" ")

# import math
# print(math.degrees(3.5))
# print(math.radians(200.535228295))
# print(math.gcd(10,15))
# print(math.lcm(5,8))
# print(math.ceil(10))
# print(math.log(8,2))
# print(math.log2(16))
# print(math.log(100,10))
# print(math.sqrt(16))
# print(math.sin(math.radians(90)))

# n=int(input())
# while len(str(n))>1:
#     s=0
#     temp=n
#     while temp>0:
#         s+=temp%10
#         temp//=10
#     n=s
# print(n)

# n=int(input("n:"))
# s=0
# if n>0:
#     res1=n*2
#     res2=n*3
#     res3=str(n)+str(res1)+str(res2)
#     print(res3)
# if len(n)==9:
#          print('fascinating number')
# else:
#     print("not")

# n=int(input("n:"))
# s=0
# num=str(n)
# l=len(num)
# if n>0:
#     for i in range(l):
#         res=int(num[i])**(i+1)
#         s+=res
# print(s)

# n=int(input())
# res=str(n)+str(n*2)+str(n*3)
# if len(res)==9:
#     for i in res:
#         if res.count(i)!=1:
#          print("not a facinating number")
#          break
#     else:
#         print("facinating number")
         
# else:
#     print("not a facinating number")

# n=int(input())
# res=str(n)+str(n*2)+str(n*3)
# if len(res)==9:
#     if set(str(x) for x in range(1,10))==set(res):
#         print("facinating number")
#     else:
#         print("not a facinating number")
# else:
#     print("not a facinating number")
    
# n=int(input())   
# s=0
# p=1
# for i in str(n):
#     s+=int(i)**p
#     p+=1
# if s==n:
#     print("disarium number")
# else:
#     print("not a disarium number")

# n=int(input())
# s=0
# p=len(str(n))
# temp=n
# while temp>0:
#     rem=temp%10
#     s+=rem**p
#     p-=1
#     temp//=10
# if s==n:
#     print("disarium number")
# else:
#     print("not a disarium number")

# n=int(input())
# res=str(n)+str(n*2)+str(n*3)
# if len(res)==9:
#     if set(str(x) for x in range(1,10))==set(res):
#         print("facinating number")
#     else:
#         print("not a facinating number")
# else:
#     print("not a facinating number")

# n=int(input())
# s=0
# p=1
# for i in str(n):
#     s+=int(i)**p
#     p+=1
# if s==n:
#     print("disarium number")
# else:
#     print("not a desarium number")


# n=int(input())
# dec=0
# p=1
# while n>0:
#     rem=n%10
#     dec=dec+rem*p
#     p=p*2
#     n=n//10
# print(dec)


# n=int(input())
# res=''
# while n>0:
#     res=str(n%2)+res
#     n//=2
# print(res)

# n=int(input())
# p=len(str(n))-1
# dec=0
# for i in str(n):
#     dec=dec+int(i)*(2**p)
#     p-=1
# print(dec)'


# n=int(input())
# bin=0
# p=1
# while n>0:
#     rem=n%2
#     bin=bin+rem*p
#     p*=10
#     n//=2
# print(bin)

# n=int(input())
# dec=0
# p=1
# while n>0:
#     rem=n%2
#     dec=dec+rem*p
#     p*=2
#     n//=10
# print(dec)

# n=int(input())
# o=""
# e=""
# for i in str(n):
#     if int(i)%2==0:
#         e+=i
        
#     else:
#         o+=i

# print(o)
# print(e)
# res=o+e
# print(res)

# n=int(input())
# o=""
# e=""
# for i in str(n):
#     if int(i)%2==0:
#         e+=i
#     else:
#         o+=i
# print(o,e)

# print("marriage age")
# n=int(input('n: '))
# if n%2==0:
#     print("Human")
# print("end")
# if n%2==1:
#     print("animal")

# n=int(input('n: '))
# if n>=10:
#     print(f"{n} is greater than 10")

# score=int(input("score: "))
# if 80<=score<=100:
#     print("Outstanding")
# elif 70<=score<=80:
#     print("excellent")
# elif 50<=score<=70:
#     print("well done")
# elif 30<=score<=50:
#     print("do well")
# else:
#     print("improve your skill")

# temperature=int(input('temperature: '))     
# if temperature>=50:
#     print("today is very hot")
# elif temperature>=30:
#     print("today is hot")
# else:
#     print("today is not hot")

# weather=int(input('weather: '))
# if 30<=weather<=50:
#     print("summer")
# elif 25<=weather<=30:
#     print("Autumn")
# elif 20<=weather<=25:
#     print("winter")
# elif 15<=weather<=20:
#     print("Rainy")
# else:
#     print("spring")

# fev=int(input('n: '))
# if 100<=fev<=150:
#   print("you have a high fever")
# elif 95<=fev<=100:
#     print("you have a fever")
# else:
#     print("you normal")
    
# n=int(input('n: '))  
# if n==10:
#     print(f"{n} is equal to 10")
# elif n>=10:
#     print(f"{n} is greater than 10")
# else:
#     print(f"{n} is less than 10")

# n=int(input("n: "))
# if n%5==0:
#     if n%10==0:
#         print(f"{n} is divasable by both 5 and 10")
#     else:
#         print(f"{n} is divisable by 5 not 10")
# else:
#     print(f"{n} is not divisable by 5 hence not checked 10")


# gender=input("select your gender\nmale female:")
# if gender in['male','female']:
#     age=int(input("age: "))
#     if gender in['male']:
#         if age<=25:
#             print("eligible for marriage")
#         else:
#             print("not eligible for marriage")
#     else:
#         if age<=22:
#             print("eligible for marriage")
#         else:
#             print("not eligible for marriage")
# else:
#     print("Invalid gender")


# heart=int(input("heartbeat: "))
# if 80<=heart<=150:
#     if 70<=heart<=80:
#         print("normal")
#     else:
#         print("abnormal")
# else:
#     print("died")


# username=input("username: ")
# password="admin123"
# if username == "admin" :
#     if password == "admin123":
#         print("Login successful!")
#     else:
#         print("username not found")
# else:
#     print("incorrect paasword")

# marks=int(input('marks: '))
# if marks>=60:
#     if marks>=90:
#         print("grade A")
#     elif marks>=75:
#         print("grade B")
#     else:
#         print("grade C")
# else:
#     print("grade D")

# animal=input("animal: ")
# match animal:
#     case 'dog':
#         print("thank creature")
#     case 'cow':
#         print("milk")
#     case 'horse':
#         print("Running")
#     case 'duck':
#         print("swim")
#     case 'cat':
#         print("miyav...miyaw...")
#     case _:
#         print("no match")

# grade=input("n: ")
# match grade:
#     case 'A':
#         print(" more than 90")
#     case 'B':
#         print(" more than grade 75")
#     case 'C':
#         print(" less than grade 50")
#     case 'D':
#         print("less than grade 30")
#     case _:
#         print("fail")

# day=int(input("n: "))
# match day:
#     case 1:
#         print("sunday")
#     case 2:
#         print("Monday")
#     case 3:
#         print("tuesday")
#     case 4:
#         print("wednesday")
#     case 5:
#         print("thursday")
#     case 6:
#         print("friday")
#     case 7:
#         print("saturday")
#     case _:
#         print("invalid day")
    
# age=int(input('age: '))  
# match age:
#     case age if age < 18:
#         print("Child")
#     case age if 18 <= age < 60:
#         print("Adult")
#     case age if age >= 60:
#         print("Senior")
#     case _:
#         print("Invalid age")

# n=int(input('n: '))
# for i in range(1,n+1):
#     print(i,end=" ")

# for i in range(5):
#     if i == 3:
#         continue
#     print(i)

# n=int(input('n:'))
# i = 0
# while i < 5:
#     i += 1
#     if i == 3:
#         continue  # Skip the rest of the loop when i is 3
#     print(i)

# l1=[1,2,3,4,5]
# l1.append(1000)
# print(l1)

# n=int(input('n: '))
# p=sum(n)
# print(p)


# n=(1,2,3,4,5)
# print(sum(n))

# n=(2,4,6,4,7,8)
# print(len(n))

# def even_odd():
#     n=int(input('n: '))

# def size_of_str():
#     str_input=input("enter string: ")
#     if len(str_input)<=8:
#         print("equal or more than 8")
#     else:
#         print(" less than 8")
# res=size_of_str(n=input())
# print(res)

# names=['anitha','jon','praveen']
# scores=[72,45,78]
# z=zip(names,scores)
# print(list(z))

# fruits=['apple','banana','grapes','kiwi']
# for index,fruits in enumerate(fruits):
#     print(index,fruits)

# l=[1,2,3,4,2,3]
# unique_l=set(l)
# print(unique_l)

# n=[3,5,4,2,3,1,3,6]
# n_sorted=sorted(n)
# print(n_sorted)

# n="3+5*2"
# res=eval(n)
# print(res)

# n=int(input('n: '))
# l1=eval(input("values: "))[:n]
# res=0
# for i in l1:
#     if i%2==0:
#         res+=i
# print(res)


# n=int(input('n: '))
# l1=eval(input("values: "))[:n]
# res=0
# for i in l1:
#     if i%2==1:
#         res+=i
# print(res)

# n=int(input('n: '))
# l1=eval(input("values: "))[:n]
# res=([x for x in l1 if x%2==1])
# print(sum(res))

# n=int(input('n: '))
# l1=eval(input("values: "))[:n]
# res=0
# for i in range(len(l1)):
#     if i%2==0:
#         res+=l1[i]
# print(res)
        
# n=int(input('n: '))
# l1=eval(input("values: "))[:n]
# res=sum(l1[::2])-sum(l1[1::2])
# print(res)

# def filters_five(n):
#     return n%5==0

# l1=[10,20,35,46,43,15]
# res=[]
# for i in l1:
#     if filters_five(i):
#         res.append(i)
# print(res)

# def filters_five(n):
#     return n%5==0
# l1=[10,20,30,45,64,15]
# res=[x for x in l1 if filters_five(x)]
# print(res)

# def anitha():
#     pass

# print(type(anitha))

# fun=lambda a,b:a+b
# print(type(fun))
# print(fun(10,20))

# cube=lambda n:n**3
# print(cube(4))

# min=lambda a,b:a+b
# print(min(10,40))


# square=lambda n:n**2
# print(square(4))


# l1=[10,20,30,13,15,20]
# res=list(filter (lambda n:n%5==0,l1))
# print(res)

# n=int(input("n: "))
# l1=eval(input("l1: "))[:n]
# c=input("c: ")[0].lower()
# res=list(filter(lambda n:n .startswith(c),l1))
# print(res)

# l1=[1,2,3,4,5]
# res=l1.pop(0)
# l1.append(res)
# print(l1)

# l1=[1,2,3,4,5]
# n=int(input('n: '))
# n=n%len(l1)
# for i in range(n):
#     temp=l1[0]
#     for i in range(len(l1)-1):
#         l1[i] = l1[i+1]
#     l1[-1]=temp
# print(l1)

# l1=[10,20,30,10,40,70]
# for i in l1:
#     while l1.count(i)-1:
#         l1.remove(i)
# print(l1)

# l2=[]
# for i in l1:
#     if i not in l2:
#        l2.append(i)
# print(l2)

# for i in range(len(l1)-1):
#     for j in range(i+len(l1)):
#         if l1[i] == l1[i]:
#           l1[j] = None
# while None in l1:
#   l1.remove(None)
# print(l1)


# l1=[10,20,30,40,10,70]
# for i in l1:
#     if l1.count(i)==1:
#       print(i)
#       break

# l1=[10,20,30,40,10,70]
# l2=[100,200,20,70]
# l3=[]
# for i in l1:
#     for j in l2:
#         if i==j:
#             l3.append(i)
#print(l3)
# l3=[]
# for i in l1:
#     if (i in l2)and (i not in l3):
#         l3.append(i)
# print(l3)
    
    
l1=[10,20,34,56,3,28]
# # print(max(l1))
# # print(min(l1))
# m=l1[0]
# u=l1[0]
# for i in l1:
#     if i>m:
#         m=i
#     if i<u:
#         u=i
# print(m,u)


# l1.sort()
# print("max",l1[-1],"min",l1[0])


# l1=[[1,3,5],[2,5,8],[9,6,5]]
# m=[]
# u=[]
# for i in l1:
#     m.append(max(i))
#     u.append(min(i))
# res=[m,u]
# print(res)


# l1=[['a',10],['b',34],['c',6],['d',24]]
# m=l1[0]
# u=l1[0]
# for i in l1:
    
#         if i[1]>m[1]:
#           m=i
#         #   m.append(max(i))
#         if i[1]<u[1]:
#            u=i
#         #    u.append(min(i))
# res=[m,u]      
# print(res)

# val=[i[1] for i in l1]
# g=max(val)
# s=min(val)
# print(g,s)
        
        
# s1="sasi"
# c=0
# for i in s1:
#   if s1>='a' and s1<='z' or s1>='A' and s1<='Z':
#    c+=1
# print(c)

# val=input("string: ")
# c=0
# for i in val:
#   if ord(i)>=97 and ord(i)<=122 or ord(i)>=65 and ord(i)<=90:
#     c+=1
# else:
#   print("total string is ->",c)


# s1=input("enter your string: ")
# j=len(s1)-1
# for i in range (len(s1)):
#   if s1[i] != s1[j]:
#     print("not a palindrome string")
#     break
#   j-=1
# else:
#   print(" palindrome string")

# s1="I am not in danger I am the danger Now say my Name"
# d1={}
# for i in s1:
#   if i not in d1.keys():
#     d1[i] = 1
#   else:
#     d1[i] +=1
# for k,v in d1.items():
#   print(k,'->',v)

# s1="pack my box with five dozens of liquor jugs"
# chr=set()
# for i in s1:
#     if i==" ":
#       continue
#     else:
#       chr.add(i)
  
# if len(chr) == 26:
#   print("palindrome string")
# else:
#   print("not palindrome string")

s1=input("enter string: ")
s2=input("enter string: ")
for i in s1:
  if s1.count(i) != s2.count(i):
    print("not a anagram string")
    break
else:
  print("anagram string")
    


        
    


    
    

    
        
    
    
 


 
     
    
    
    
   
    
    
    
    

        

    
    