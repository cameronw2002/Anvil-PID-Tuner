"""
Made by cheesefacejoe

initially ported to python by Dr.B
"""
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import numpy as np
import random

window = Tk()


window.title("Anvil Tuner 0.21")
window.geometry("500x320")

plotAngVel = False
night = True
back = "#383838"
fore = "white"

window.configure(bg = back)

def nightMode():
    global night
    if(night):
        night = False
        back = "white"
        fore = "#383838"
        window.configure(bg = back)
        KpLabel.configure(bg = back, fg = fore)
        Kp.configure(bg = back, fg = fore)
        KdLabel.configure(bg = back, fg = fore)
        Kd.configure(bg = back, fg = fore)
        apLabel.configure(bg = back, fg = fore)
        AP.configure(bg = back, fg = fore)
        avLabel.configure(bg = back, fg = fore)
        AV.configure(bg = back, fg = fore)
        oLabel.configure(bg = back, fg = fore)
        o.configure(bg = back, fg = fore)
        nLabel.configure(bg = back, fg = fore)
        n.configure(bg = back, fg = fore)
        fLabel.configure(bg = back, fg = fore)
        f.configure(bg = back, fg = fore)
        iLabel.configure(bg = back, fg = fore)
        I.configure(bg = back, fg = fore)
        lLabel.configure(bg = back, fg = fore)
        L.configure(bg = back, fg = fore)
        tLabel.configure(bg = back, fg = fore)
        T.configure(bg = back, fg = fore)
        maxLabel.configure(bg = back, fg = fore)
        MAX.configure(bg = back, fg = fore)
        yLabel.configure(bg = back, fg = fore)
        y.configure(bg = back, fg = fore)
        blankRow.configure(bg = back, fg = fore)
        blankRow2.configure(bg = back, fg = fore)
        blankRow3.configure(bg = back, fg = fore)
        cLabel.configure(bg = back, fg = fore)
        nmButton.configure(text = "NightMode", bg = fore, fg = back)
    else:
        night = True
        back = "#383838"
        fore = "white"
        window.configure(bg = back)
        KpLabel.configure(bg = back, fg = fore)
        Kp.configure(bg = back, fg = fore)
        KdLabel.configure(bg = back, fg = fore)
        Kd.configure(bg = back, fg = fore)
        apLabel.configure(bg = back, fg = fore)
        AP.configure(bg = back, fg = fore)
        avLabel.configure(bg = back, fg = fore)
        AV.configure(bg = back, fg = fore)
        oLabel.configure(bg = back, fg = fore)
        o.configure(bg = back, fg = fore)
        nLabel.configure(bg = back, fg = fore)
        n.configure(bg = back, fg = fore)
        fLabel.configure(bg = back, fg = fore)
        f.configure(bg = back, fg = fore)
        iLabel.configure(bg = back, fg = fore)
        I.configure(bg = back, fg = fore)
        lLabel.configure(bg = back, fg = fore)
        L.configure(bg = back, fg = fore)
        tLabel.configure(bg = back, fg = fore)
        T.configure(bg = back, fg = fore)
        maxLabel.configure(bg = back, fg = fore)
        MAX.configure(bg = back, fg = fore)
        yLabel.configure(bg = back, fg = fore)
        y.configure(bg = back, fg = fore)
        blankRow.configure(bg = back, fg = fore)
        blankRow2.configure(bg = back, fg = fore)
        blankRow3.configure(bg = back, fg = fore)
        cLabel.configure(bg = back, fg = fore)
        nmButton.configure(text = "BrightMode", bg = fore, fg = back)
        
def plotAV():
    global plotAngVel
    if(plotAngVel):
        plotAngVel = False
        avButton.configure(bg = "red")
    else:
        plotAngVel = True
        avButton.configure(bg = "green")
    
    
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
    aaPrev = ap #previous angular acc
    avPrev = av #previous angular vel
    apPrev = ap #previous angular pos

    #other variables
    dR = 3.1416 / 180.0 # degrees to radians

    #matplotlib stuff
    ts = np.arange(0, T.get(), dt)
    ap_plot = []
    av_plot = []
    pid_plot = []
    zero_plot = []

    #close the previous graph
    plt.close()

    #plot dark mode
    if(night):
        plt.style.use('dark_background')
    else:
        plt.style.use('default')
    
    while(count < T.get()):
        PIDout = ((Kp.get() / 100.0) * -apPrev + (Kd.get() / 100.0) * -avPrev) + o.get()

        if(PIDout > MAX.get() + o.get()):
            PIDout = MAX.get() + o.get()
        if(PIDout < -MAX.get() + o.get()):
            PIDout = -MAX.get() + o.get()

        aaPrev = aa
        apPrev = ap
        avPrev = av
         
        t = l * f.get() * np.sin(PIDout * dR)
            
        aa = t / i

        av += ((aa + aaPrev) / 2) * dt

        if(n.get() > 0):
             av += (random.randrange(-n.get(), n.get()) / 100.0)

        ap += ((av + avPrev) / 2) * dt

        ap_plot.append(ap)
        if(plotAngVel):
            av_plot.append(av)
        pid_plot.append(PIDout - o.get())
        zero_plot.append(0)

        count += dt

    def c_extend(array):
        array.extend(np.full(len(ts) - len(array), array[0]))
        
    c_extend(ap_plot)
    if(plotAngVel):
            c_extend(av_plot)
    c_extend(pid_plot)
    c_extend(zero_plot)

    fig, ax = plt.subplots()

    plt.ylim(-y.get(), y.get())
    plt.plot(ts, ap_plot, label = 'Angular Position')
    plt.plot(ts, pid_plot, label = 'PID Output')
    if(plotAngVel):
        plt.plot(ts, av_plot, label = 'Angular Velocity')
    if(night):
        plt.plot(ts, zero_plot, color = 'WHITE')
    else:
        plt.plot(ts, zero_plot, color = 'BLACK')

    plt.ylabel("Angle (D)")
    plt.xlabel("Time (S)")
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    plt.title('Anvil Tuner 0.21')
    plt.legend()
    plt.show()

KpLabel = Label(window, text = "Kp:  ", bg = back, fg = fore)
Kp = Scale(window, from_ = 0, to = 300, orient = HORIZONTAL, bg = back, fg = fore)
KpLabel.grid(row = 0, column = 0)
Kp.grid(row = 0, column = 1)

KdLabel = Label(window, text = "Kd:  ", bg = back, fg = fore)
Kd = Scale(window, from_ = 0, to = 300, orient = HORIZONTAL, bg = back, fg = fore)
KdLabel.grid(row = 0, column = 2)
Kd.grid(row = 0, column = 3)

apLabel = Label(window, text = "Initial AngPos (deg):  ", bg = back, fg = fore)
AP = Scale(window, from_ = -10, to = 10, orient = HORIZONTAL, bg = back, fg = fore)
apLabel.grid(row = 1, column = 0)
AP.grid(row = 1, column = 1)

avLabel = Label(window, text = "Initial AngVel (deg/s):  ", bg = back, fg = fore)
AV = Scale(window, from_ = -10, to = 10, orient = HORIZONTAL, bg = back, fg = fore)
avLabel.grid(row = 1, column = 2)
AV.grid(row = 1, column = 3)

oLabel = Label(window, text = "TVC Misalignment (deg): ", bg = back, fg = fore)
o = Scale(window, from_ = -3, to = 3, orient = HORIZONTAL, bg = back, fg = fore)
oLabel.grid(row = 2, column = 0)
o.grid(row = 2, column = 1)

nLabel = Label(window, text = "Noise:  ", bg = back, fg = fore)
n = Scale(window, from_ = 0, to = 100, orient = HORIZONTAL, bg = back, fg = fore)
nLabel.grid(row = 2, column = 2)
n.grid(row = 2, column = 3)

fLabel = Label(window, text = "Force (N):  ", bg = back, fg = fore)
f = Scale(window, from_ = 1, to = 20, orient = HORIZONTAL, bg = back, fg = fore)
fLabel.grid(row = 3, column = 0)
f.grid(row = 3, column = 1)

iLabel = Label(window, text = "Inertia:  ", bg = back, fg = fore)
I = Scale(window, from_ = 1, to = 100, orient = HORIZONTAL, bg = back, fg = fore)
iLabel.grid(row = 3, column = 2)
I.grid(row = 3, column = 3)

lLabel = Label(window, text = "Lever (cm):  ", bg = back, fg = fore)
L = Scale(window, from_ = 1, to = 100, orient = HORIZONTAL, bg = back, fg = fore)
lLabel.grid(row = 4, column = 0)
L.grid(row = 4, column = 1)

tLabel = Label(window, text = "Sim Length (s):  ", bg = back, fg = fore)
T = Scale(window, from_ = 2, to = 25, orient = HORIZONTAL, bg = back, fg = fore)
tLabel.grid(row = 4, column = 2)
T.grid(row = 4, column = 3)

maxLabel = Label(window, text = "TVC Max Deflection:  ", bg = back, fg = fore)
MAX = Scale(window, from_ = 1, to = 10, orient = HORIZONTAL, bg = back, fg = fore)
maxLabel.grid(row = 5, column = 0)
MAX.grid(row = 5, column = 1)

yLabel = Label(window, text = "Plot Y axis Range:  ", bg = back, fg = fore)
y = Scale(window, from_ = 1, to = 25, orient = HORIZONTAL, bg = back, fg = fore)
yLabel.grid(row = 5, column = 2)
y.grid(row = 5, column = 3)

blankRow = Label(window, text = " ", bg = back)
blankRow.grid(row = 6, column = 0)

nmButton = Button(window, text = "BrightMode", command = nightMode, bg = "white")
nmButton.grid(row = 7, column = 1)

avButton = Button(window, text = "Plot AngVel", command = plotAV, bg = "red")
avButton.grid(row = 7, column = 2)
    
runButton = Button(window, text = "Start Sim", command = runSim, bg = "green")
runButton.grid(row = 7, column = 3)

blankRow2 = Label(window, text = " ", bg = back)
blankRow2.grid(row = 8, column = 0)
blankRow3 = Label(window, text = " ", bg = back)
blankRow3.grid(row = 9, column = 0)

cLabel = Label(window, text = "You found me!", bg = back, fg = fore)
cLabel.grid(row = 10, column = 0)

window.mainloop()
