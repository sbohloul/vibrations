import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation


r_0 = [
    [1, 1], 
    [2, 2]
]

u_q = [
    [0.1, 0.1], 
    [0.1, -0.1]
]

dt = 20 
w = 0.01
scale_a = 1.0
T = 2 * np.pi / w
frame_num = T // dt

fig, ax = plt.subplots()
ax.set_xlim(0, 3)
ax.set_ylim(0, 3)
line, = ax.plot([], [], markersize=10)

def update_position(t):
    r = []
    for r_s, u_s in zip(r_0, u_q):
        r.append([x + scale_a * y * np.sin(w * t) for x, y in zip(r_s, u_s)])
    
    return r
    
def init():
    line.set_data([], [])
    return line,

def animate(i):
    r = update_position(i)


    for r_s in r:
        xdata, ydata = r_s
        line.set_data(xdata, ydata, 'o')
    
    return line,

# anim = animation.FuncAnimation(fig, animate, interval=dt, frames=frame_num, blit=True)

# plt.show()        
r = update_position(T)
for r_s in r:
    xdata, ydata = r_s
    print(xdata, ydata)