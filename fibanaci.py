def feb(a,b,n):
    
  c=a+b
  if(n>0):
        print(c)
        feb(b,c,n-1)
   
a=0
b=1

n=int(input("how many digits"))
print(a)
feb(a,b,n-1)
