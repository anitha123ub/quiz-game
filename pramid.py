# n=int(input('n: '))
# spc=n-1
# str=1
# for i in range(n):
#     for j in range(spc):
#         print(" ",end=" ")
#     for k in range(str):
#         print("*",end=" ")
#     print()
#     spc-=1
#     str+=2

# n=int(input('n: '))
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         print("*",end=" ")
#     print()

# n=int(input('n: '))

# for i in range(n):
#     val=ord('A')
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         print(chr(val),end=" ")
#         val+=1
#     print()
#     if val>ord('Z'):
#         val=ord('A')

# n=int(input('n: '))
# val=ord('Z')
# for i in range(n):
    
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         print(chr(val),end=" ")
        
#     print()
#     val-=1

# n=int(input('n: '))
# val=9
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         print(val,end=" ")
#     print()
#     val-=1

# n=int(input('n: '))

# for i in range(n):
#     val=3
    
#     for j in range(n-1-i):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         print(val,end=" ")
#         val-=1
#         if val<1:
#           val=3
        
#     print()


# n=int(input('n: '))
# spc=n+1
# str=7
# for i in range(n):
#     for j in range(spc):
#         print(" ",end=" ")
#     for k in range(str):
#         print("*",end=" ")
#     print()
#     spc+=1
#     str-=2

# n=int(input('n: '))
# val=3
# for i in range(n):
   
#     for j in range(n+i-3):
#         print(" ",end=" ")
#     for k in range(5-2*i):
#         print(val,end=" ")
       
       
#     print()
#     val-=1

# n=int(input('n: '))
# p = True
# val1=ord('A')
# val2=1

# for i in range(n):
#     for j in range(n):
#         if p:
#             print(chr(val1),end=" ")
#             val1+=1
#             p = False
#         else:
#             print(val2,end=" ")
#             val2+=1
#             p=True
#             if val2>9:
#               val2=1
            
#     print()

# n=int(input('n: '))
# # val=1
# for i in range(n):
#     val1=1
#     val2=1
#     for j in range(n):
#         if i==j:
#           print("*",end=" ")
         
#         elif i>=j:
#             print(val1,end=" ")
#             val1+=1
#         else:
#             print(val2,end=" ")
            
#             val2+=1
#             if val2>3:
#                 val2=1
            
#     print()
#     # val+=1
    
   
# n=int(input('n: '))
# val1=ord('Z')
# for i in range(n):
#     print(" "*(n-i-1),end=" ")
#     for j in range(n):
#         if (i+j)>=n-1:
#             print(chr(val1),end=" ")
            
#         else:
#             print(" ",end=" ")
#     print()
#     val1-=1
#     if val1>ord('Z'):
#         val1=ord('x')


# n=int(input('n: '))
# for i in range(n):
#     for j in range(2*n-1):
#            if i==0 or i==j or i+j==n*2-2:
#               print("*",end=" ")
#            else:
#               print(" ",end=" ")
#     print()

# n=int(input('n: '))
# for i in range(n):
#     for j in range(n):
#         if j==0 or i%2==0:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n=int(input('n: '))
# val=ord('Z')
# for i in range(n):
#    for j in range(n):
#       if
#       print(chr(val),end=" ")
#       val+=1
#       if val>ord('Z'):
#          val=ord('Z')
#    print()
#    val-=1

# n=int(input('n: '))
# for i in range(n):
#    for j in range(n):
#       if i==0 or i==n-1 or i+j==n-1:
#          print("*",end=" ")
#       else:
#          print(" ",end=" ")
#    print()

# n=int(input('n: '))
# for i in range(i*2+n-1):
#     print(i,end=" ")

# n=int(input('n: '))
# a=1
# for i in range(1,n+1):
#     print(a,end=" ")
#     a+=i

# n=int(input('n: '))
# for i in range(n):
#     for j in range(n-i-1):
#        print(" ",end=" ")
#     val=1
#     for k in range(i+1):
#        print(val,end="   ")
#        val=val*(i-k)//(k+1)
#     print()

n=int(input())
for i in range(n):
   for j in range(n):
      if i==0 or i==n-1 or j==0 or j==n-1:
         print("*",end=" ")
      else:
         print(" ",end=" ")
   print()

   
    
    
    
   
   
   
   

    
        
    
   
    
            
    
   
        
    
    
   
    
   
    
    
   
    
   
    
    
   
    
    
    