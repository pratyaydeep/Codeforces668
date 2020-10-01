# Author : Pratyaydeep↯Ghanta
import io,os
inp=io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
inar=lambda: list(map(int,inp().split()))
inin=lambda: int(inp())
inst=lambda: inp().decode().strip()
# Am I debugging, check if I'm using same variable name in two places
from collections import deque as que
_T_=inin()
for _t_ in range(_T_):
    n=inin()
    a=inar()
    dq=que()
    for i in range(n):
        if a[i]<0:
            dq.append(i)
    for i in range(n):
        while(dq and a[i]>0):
            j=dq.popleft()
            if j<i:
                pass
            else:
                minu=min(a[i],abs(a[j]))
                a[i]-=minu 
                a[j]+=minu
                if a[j]<0:
                    dq.appendleft(j)
            #print(dq)
    ans=0
    for i in a:
        if i>0:
            ans+=i
    print(ans)

