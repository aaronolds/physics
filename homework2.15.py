from vpython import *

fancart = sphere(pos=vector(16.4, 15, 0), radius=0.5, color=color.green)
vfancart = vector(5.61, 0, 0)
t = 0
dt = 0.1

while t < 0.7:
    fancart.pos = fancart.pos + vfancart * dt
    print("The product of vfanctart and dt is", vfancart * dt)
    print("The position of the fancart at time", t, "is", fancart.pos)
    t = t + dt

print("The final time is", t)
print("The final position of the fancart is", fancart.pos)
print("The final velocity of the fancart is", vfancart)
