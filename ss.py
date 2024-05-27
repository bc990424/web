import numpy as np

a=np.zeros((16,16))
def w(n,m):
    a[n] = m

w(((3,3)),1)



print(a)

print(a[np.where(a == 1 )])