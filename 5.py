def f(n):
    a=1
    while n!=0:
        a=a*n
        n=n-1
    return a
n=int(input())
s=0
while n!=0:
    s+=f(n)
    n=n-1
print(s)


