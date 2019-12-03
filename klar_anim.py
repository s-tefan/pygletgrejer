
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('seaborn-pastel')


fig = plt.figure()
ax = plt.axes(xlim=(0, 0.5), ylim=(-2, 2))
line, = ax.plot([], [], lw=3)

def init():
    line.set_data([], [])
    return line,
def animate(i):
    x = np.linspace(0.01, 0.5, 200)
    y = np.cos( np.pi * x) * np.sin(0.01 * np.pi* i)
    k=3
    y2 = 0.5*np.cos( np.pi * k * x) * np.sin(0.01* np.pi* k* i)
    line.set_data(x, y)
#    line.set_data(x, y+y2)
    return line,

anim = FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=10, blit=True)

anim.save('klar_wave.gif', writer='imagemagick')
plt.show()