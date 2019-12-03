
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('seaborn-pastel')


fig1 = plt.figure()
ax = plt.axes(xlim=(-1, 1), ylim=(0, 16))


z=[0]*16
p=list(range(1,17))

print(z,p)
plt.plot(z,p,'o')

fig2 = plt.figure()
ax = plt.axes(xlim=(-1, 1), ylim=(0, 12))
print(np.log2(16))
xapa=[[-1]*13,[1]*13]
yapa=[list(range(13)),list(range(13))]
plt.plot(xapa,yapa,'b-')
treklang=list(map(lambda x:12*np.log2(x),[1,5/4,3/2,2]))
treklangplus=list(map(lambda x:12*np.log2(x),[1,5/4,3/2,7/4,2]))
#plt.hold()
plt.plot([0]*5,treklangplus,'ro')
dimmoj=list(map(lambda x:12*np.log2(x),[1,6/5,7/5,8/5,9/5,2]))
plt.plot([0.1]*6,dimmoj,'mo')
molltreklang=list(map(lambda x:12*np.log2(x),[1,6/5,3/2,2]))
plt.plot([0.2]*4,molltreklang,'bo')
mujklang=list(map(lambda x:12*np.log2(x),[1,7/6,8/6,9/6,10/6,11/6,12/6]))
plt.plot([0.3]*7,mujklang,'go')


plt.show()

