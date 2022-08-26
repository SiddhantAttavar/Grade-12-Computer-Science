l,r=map(int,input().split())
print(*(i for i in range(l,r+1) if sum(i%j==0 for j in range(2,i))))