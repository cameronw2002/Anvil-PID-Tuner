"""
Made by cheesefacejoe

initially ported to python by Dr.B

I know it looks like a mess right now, much of this code has been thrown together in my free time. I will be making it much better in the next few days/weeks because this has become my main project
"""
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import numpy as np
import random

window = Tk()

window.title("Anvil Tuner 0.1")
window.geometry("500x300")
    
def runSim():
    #time variables
    dt = T.get() / 200.0 #sim refresh rate
    count = 0 #how far along the sim is

    #state variables
    i = I.get() / 100.0 #inertia
    l = L.get() / 100.0 #lever
    t = 0 #torque
    aa = 0 #angular accel
    av = AV.get()
    ap = AP.get()
    avPrev = av #previous angular vel
    apPrev = ap #previous angular pos

    #PID variables
    intg = 0 #integral
    PIDout = 0 #PID output

    #other variables
    dR = 3.1416 / 180 # degrees to radians
    off = o.get() #motor mount offset
    M = 5 #max servo range
    m = -M #min servo range

    #matplotlib stuff
    ts = np.arange(0, T.get(), dt)
    ap_plot = []
    #av_plot = []
    pid_plot = []
    zero_plot = []

    plt.close()
    
    while(count < T.get()):
        PIDout = ((Kp.get() / 100.0) * -apPrev + (Kd.get() / 100.0) * -avPrev) + off

        if(PIDout > M + off):
            PIDout = M + off
        if(PIDout < m + off):
             PIDout = m + off

        apPrev = ap
        avPrev = av
         
        t = l * f.get() * np.sin(PIDout * dR)
            
        aa = t / i

        av += aa * dt

        if(w.get() > 0):
             av += (random.randrange(-w.get(), w.get()) / 100.0)

        ap += av * dt

        ap_plot.append(ap)
        pid_plot.append(PIDout)
        zero_plot.append(0)

        count += dt

    def c_extend(array):
        array.extend(np.full(len(ts) - len(array), array[0]))
        
    c_extend(ap_plot)
    c_extend(pid_plot)
    c_extend(zero_plot)

    fig, ax = plt.subplots()

    plt.ylim(-15, 15)
    plt.plot(ts, ap_plot, label = 'Angular Position')
    plt.plot(ts, pid_plot, label = 'PID Output')
    plt.plot(ts, zero_plot, color = 'BLACK')

    plt.ylabel("Angle (D)")
    plt.xlabel("Time (S)")
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    plt.title('Anvil Tuner 0.1')
    plt.legend()
    plt.show()

KpLabel = Label(window, text = "Kp:  ")
Kp = Scale(window, from_ = 0, to = 300, orient = HORIZONTAL)
KpLabel.grid(row = 0, column = 0)
Kp.grid(row = 0, column = 1)

KdLabel = Label(window, text = "Kd:  ")
Kd = Scale(window, from_ = 0, to = 300, orient = HORIZONTAL)
KdLabel.grid(row = 0, column = 2)
Kd.grid(row = 0, column = 3)

apLabel = Label(window, text = "Initial AngPos (deg):  ")
AP = Scale(window, from_ = -10, to = 10, orient = HORIZONTAL)
apLabel.grid(row = 1, column = 0)
AP.grid(row = 1, column = 1)

avLabel = Label(window, text = "Initial AngVel (deg):  ")
AV = Scale(window, from_ = -10, to = 10, orient = HORIZONTAL)
avLabel.grid(row = 1, column = 2)
AV.grid(row = 1, column = 3)

oLabel = Label(window, text = "TVC Misalignment (deg): ")
o = Scale(window, from_ = -3, to = 3, orient = HORIZONTAL)
oLabel.grid(row = 2, column = 0)
o.grid(row = 2, column = 1)

wLabel = Label(window, text = "Wind(Noise):  ")
w = Scale(window, from_ = 0, to = 100, orient = HORIZONTAL)
wLabel.grid(row = 2, column = 2)
w.grid(row = 2, column = 3)

fLabel = Label(window, text = "Force:  ")
f = Scale(window, from_ = 0, to = 20, orient = HORIZONTAL)
fLabel.grid(row = 3, column = 0)
f.grid(row = 3, column = 1)

iLabel = Label(window, text = "Inertia:  ")
I = Scale(window, from_ = 1, to = 100, orient = HORIZONTAL)
iLabel.grid(row = 3, column = 2)
I.grid(row = 3, column = 3)

lLabel = Label(window, text = "Lever (cm):  ")
L = Scale(window, from_ = 1, to = 100, orient = HORIZONTAL)
lLabel.grid(row = 4, column = 0)
L.grid(row = 4, column = 1)

tLabel = Label(window, text = "Sim Length (s):  ")
T = Scale(window, from_ = 2, to = 25, orient = HORIZONTAL)
tLabel.grid(row = 4, column = 2)
T.grid(row = 4, column = 3)

blankRow = Label(window, text = " ")
blankRow.grid(row = 5, column = 0)

runButton = Button(window, text = "Start Sim", command = runSim, bg = "green")
runButton.grid(row = 6, column = 1)

window.mainloop()
