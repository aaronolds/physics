from vpython import *

scene.background = vector(1, 1, 0.8)

# Objects

leftcliff = box(pos=vector(-100, 0, 0),
                size=vector(2000, 400, 0), color=color.white)

skateboard = box(pos=vector(-100, 250, 0),
                 size=vector(50, 50, 0), color=color.green)

rightcliff = box(pos=vector(1500, 0, 0), size=vector(
    500, 400, 0), color=color.white)

# Parameters and Initial Conditions

g = vector(0, -9.81, 0)

skateboardm = 1500

skateboardv = vector(10, 0, 0)

skateboardp = vector(skateboardm * skateboardv.x,
                     skateboardm * skateboardv.y, skateboardm * skateboardv.z)


# Time and time step
t = 0

dt = .01

# Calculation Loop
while skateboard.pos.x <= 875:
    rate(500)

    Fgrav = vector(skateboardm * g.x, skateboardm * g.y, skateboardm * g.z)

    Fground = Fgrav

    Fnet = vector(Fgrav.x - Fground.x, Fgrav.y -
                  Fground.y, Fgrav.z - Fground.z)

    skateboardp = skateboardp + vector(Fnet.x * dt, Fnet.y * dt, Fnet.z * dt)

    skateboard.pos = skateboard.pos + (skateboardp/skateboardm)*dt

    t = t + dt
