f=lambda n:1 if n <= 1 else n*f(n-1)
n,l,r=map(int,input().split())
print(sum([-(-1)**i*i*1.0/f(2*i+1) for i in range(1,n+1)]))
print(*[i for i in range(l,r+1)if i==sum(map(f,map(int,str(i))))])
