d=0
for i in range(n):
        d=d*10+9
        if s==0:
        return 0
    for i in range(d,-1,-1):
        temp=i
        sum=0
        while temp>0:
            sum+=temp%10
            temp//=10
        if sum==s:
            return i
    return -1