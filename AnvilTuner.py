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

window.title("Anvil Tuner 0.53")
window.geometry("800x275")

plotAngVel = False
night = True
slider = True
back = "#383838"
fore = "white"

Kp2 = DoubleVar()
Ki2 = DoubleVar()
Kd2 = DoubleVar()
AP2 = IntVar()
AV2 = IntVar()
o2 = IntVar()
n2 = IntVar()
f2 = IntVar()
I2 = DoubleVar()
L2 = IntVar()
T2 = IntVar()
MAX2 = IntVar()
y2 = IntVar()
slew2 = IntVar()
gear2 = IntVar()

window.configure(bg = back)

KpLabel = Label(window, text = "Kp:  ", bg = back, fg = fore)
KiLabel = Label(window, text = "Ki:  ", bg = back, fg = fore)
KdLabel = Label(window, text = "Kd:  ", bg = back, fg = fore)
apLabel = Label(window, text = "Initial AngPos (deg):  ", bg = back, fg = fore)
avLabel = Label(window, text = "Initial AngVel (deg/s):  ", bg = back, fg = fore)
oLabel = Label(window, text = "TVC Misalignment (deg): ", bg = back, fg = fore)
nLabel = Label(window, text = "Noise:  ", bg = back, fg = fore)
fLabel = Label(window, text = "Force (N):  ", bg = back, fg = fore)
iLabel = Label(window, text = "Inertia:  ", bg = back, fg = fore)
lLabel = Label(window, text = "Lever (cm):  ", bg = back, fg = fore)
tLabel = Label(window, text = "Sim Length (s):  ", bg = back, fg = fore)
maxLabel = Label(window, text = "TVC Max Deflection:  ", bg = back, fg = fore)
yLabel = Label(window, text = "Plot Y axis Range:  ", bg = back, fg = fore)
slewLabel = Label(window, text = "Servo Slew Rate (deg/s):  ", bg = back, fg = fore)
gearLabel = Label(window, text = "Gear Ratio:  ", bg = back, fg = fore)
blankRow = Label(window, text = " ", bg = back)
blankRow2 = Label(window, text = " ", bg = back)
blankRow3 = Label(window, text = " ", bg = back)
cLabel = Label(window, text = "You found me!", bg = back, fg = fore)

Kp = Scale(window, from_ = 0, to = 300, orient = HORIZONTAL, bg = back, fg = fore)
Ki = Scale(window, from_ = 0, to = 300, orient = HORIZONTAL, bg = back, fg = fore)
Kd = Scale(window, from_ = 0, to = 300, orient = HORIZONTAL, bg = back, fg = fore)
AP = Scale(window, from_ = -10, to = 10, orient = HORIZONTAL, bg = back, fg = fore)
AV = Scale(window, from_ = -10, to = 10, orient = HORIZONTAL, bg = back, fg = fore)
o = Scale(window, from_ = -3, to = 3, orient = HORIZONTAL, bg = back, fg = fore)
n = Scale(window, from_ = 0, to = 100, orient = HORIZONTAL, bg = back, fg = fore)
f = Scale(window, from_ = 1, to = 20, orient = HORIZONTAL, bg = back, fg = fore)
I = Scale(window, from_ = 1, to = 100, orient = HORIZONTAL, bg = back, fg = fore)
L = Scale(window, from_ = 1, to = 100, orient = HORIZONTAL, bg = back, fg = fore)
T = Scale(window, from_ = 2, to = 25, orient = HORIZONTAL, bg = back, fg = fore)
MAX = Scale(window, from_ = 1, to = 10, orient = HORIZONTAL, bg = back, fg = fore)
y = Scale(window, from_ = 5, to = 25, orient = HORIZONTAL, bg = back, fg = fore)
slew = Scale(window, from_ = 1, to = 600, orient = HORIZONTAL, bg = back, fg = fore)
gear = Scale(window, from_ = 1, to = 10, orient = HORIZONTAL, bg = back, fg = fore)

KpLabel.grid(row = 0, column = 0)
KiLabel.grid(row = 0, column = 2)
KdLabel.grid(row = 0, column = 4)
apLabel.grid(row = 1, column = 0)
avLabel.grid(row = 1, column = 2)
oLabel.grid(row = 1, column = 4)
nLabel.grid(row = 2, column = 0)
fLabel.grid(row = 2, column = 2)
iLabel.grid(row = 2, column = 4)
lLabel.grid(row = 3, column = 0)
tLabel.grid(row = 3, column = 2)
maxLabel.grid(row = 3, column = 4)
yLabel.grid(row = 4, column = 0)
slewLabel.grid(row = 4, column = 2)
gearLabel.grid(row = 4, column = 4)
blankRow.grid(row = 5, column = 0)
blankRow2.grid(row = 8, column = 0)
blankRow3.grid(row = 9, column = 0)
cLabel.grid(row = 10, column = 0)

Kp.grid(row = 0, column = 1)
Ki.grid(row = 0, column = 3)
Kd.grid(row = 0, column = 5)
AP.grid(row = 1, column = 1)
AV.grid(row = 1, column = 3)
o.grid(row = 1, column = 5)
n.grid(row = 2, column = 1)
f.grid(row = 2, column = 3)
I.grid(row = 2, column = 5)
L.grid(row = 3, column = 1)
T.grid(row = 3, column = 3)
MAX.grid(row = 3, column = 5)
y.grid(row = 4, column = 1)
slew.grid(row = 4, column = 3)
gear.grid(row = 4, column = 5)

def textBox():
    global slider

    global Kpt
    global Kit
    global Kdt
    global APt
    global AVt
    global ot
    global nt
    global ft
    global It
    global Lt
    global Tt
    global MAXt
    global yt
    global slewt
    global geart

    global Kp
    global Ki
    global Kd
    global AP
    global AV
    global o
    global n
    global f
    global I
    global L
    global T
    global MAX
    global y
    global slew
    global gear

    global Kp2
    global Ki2
    global Kd2
    global AP2
    global AV2
    global o2
    global n2
    global f2
    global I2
    global L2
    global T2
    global MAX2
    global y2
    global slew2
    global gear2

    global blankR0
    global blankR
    global blankR2
    global blankR3
    global blankR4

    global blankRow2
    global blankRow3
    global cLabel
    
    if(slider):
        Kp.destroy()
        Ki.destroy()
        Kd.destroy()
        AP.destroy()
        AV.destroy()
        o.destroy()
        n.destroy()
        f.destroy()
        I.destroy()
        L.destroy()
        T.destroy()
        MAX.destroy()
        y.destroy()
        slew.destroy()
        gear.destroy()
        
        Kpt = Entry(window, textvariable = Kp2, bg = back, fg = fore)
        Kit = Entry(window, textvariable = Ki2, bg = back, fg = fore)
        Kdt = Entry(window, textvariable = Kd2, bg = back, fg = fore)
        APt = Entry(window, textvariable = AP2, bg = back, fg = fore)
        AVt = Entry(window, textvariable = AV2, bg = back, fg = fore)
        ot = Entry(window, textvariable = o2, bg = back, fg = fore)
        nt = Entry(window, textvariable = n2, bg = back, fg = fore)
        ft = Entry(window, textvariable = f2, bg = back, fg = fore)
        It = Entry(window, textvariable = I2, bg = back, fg = fore)
        Lt = Entry(window, textvariable = L2, bg = back, fg = fore)
        Tt = Entry(window, textvariable = T2, bg = back, fg = fore)
        MAXt = Entry(window, textvariable = MAX2, bg = back, fg = fore)
        yt = Entry(window, textvariable = y2, bg = back, fg = fore)
        slewt = Entry(window, textvariable = slew2, bg = back, fg = fore)
        geart = Entry(window, textvariable = gear2, bg = back, fg = fore)

        blankR0 = Label(window, text = " ", bg = back)
        blankR = Label(window, text = " ", bg = back)
        blankR2 = Label(window, text = " ", bg = back)
        blankR3 = Label(window, text = " ", bg = back)
        blankR4 = Label(window, text = " ", bg = back)

        blankRow2.grid(row = 14, column = 0)
        blankRow3.grid(row = 15, column = 0)

        blankR0.grid(row = 0, column = 0)

        KpLabel.grid(row = 1, column = 0)
        KiLabel.grid(row = 1, column = 2)
        KdLabel.grid(row = 1, column = 4)

        blankR.grid(row = 2, column = 0)
        
        apLabel.grid(row = 3, column = 0)
        avLabel.grid(row = 3, column = 2)
        oLabel.grid(row = 3, column = 4)

        blankR2.grid(row = 4, column = 0)
        
        nLabel.grid(row = 5, column = 0)
        fLabel.grid(row = 5, column = 2)
        iLabel.grid(row = 5, column = 4)

        blankR3.grid(row = 6, column = 0)

        lLabel.grid(row = 7, column = 0)
        tLabel.grid(row = 7, column = 2)
        maxLabel.grid(row = 7, column = 4)

        blankR4.grid(row = 8, column = 0)
        
        yLabel.grid(row = 9, column = 0)
        slewLabel.grid(row = 9, column = 2)
        gearLabel.grid(row = 9, column = 4)
        
        blankRow.grid(row = 10, column = 0)

        Kpt.grid(row = 1, column = 1)
        Kit.grid(row = 1, column = 3)
        Kdt.grid(row = 1, column = 5)
        APt.grid(row = 3, column = 1)
        AVt.grid(row = 3, column = 3)
        ot.grid(row = 3, column = 5)
        nt.grid(row = 5, column = 1)
        ft.grid(row = 5, column = 3)
        It.grid(row = 5, column = 5)
        Lt.grid(row = 7, column = 1)
        Tt.grid(row = 7, column = 3)
        MAXt.grid(row = 7, column = 5)
        yt.grid(row = 9, column = 1)
        slewt.grid(row = 9, column = 3)
        geart.grid(row = 9, column = 5)

        nmButton.grid(row = 13, column = 0)
        textButton.grid(row = 13, column = 1)
        avButton.grid(row = 13, column = 2)
        runButton.grid(row = 13, column = 3)

        cLabel.grid(row = 16, column = 0)
        
        slider = False
        textButton.configure(text = "Sliders")
        
    else:
        Kpt.destroy()
        Kit.destroy()
        Kdt.destroy()
        APt.destroy()
        AVt.destroy()
        ot.destroy()
        nt.destroy()
        ft.destroy()
        It.destroy()
        Lt.destroy()
        Tt.destroy()
        MAXt.destroy()
        yt.destroy()
        slewt.destroy()
        geart.destroy()
        blankR0.destroy()
        blankR.destroy()
        blankR2.destroy()
        blankR3.destroy()
        blankR4.destroy()

        Kp = Scale(window, from_ = 0, to = 300, orient = HORIZONTAL, bg = back, fg = fore)
        Ki = Scale(window, from_ = 0, to = 300, orient = HORIZONTAL, bg = back, fg = fore)
        Kd = Scale(window, from_ = 0, to = 300, orient = HORIZONTAL, bg = back, fg = fore)
        AP = Scale(window, from_ = -10, to = 10, orient = HORIZONTAL, bg = back, fg = fore)
        AV = Scale(window, from_ = -10, to = 10, orient = HORIZONTAL, bg = back, fg = fore)
        o = Scale(window, from_ = -3, to = 3, orient = HORIZONTAL, bg = back, fg = fore)
        n = Scale(window, from_ = 0, to = 100, orient = HORIZONTAL, bg = back, fg = fore)
        f = Scale(window, from_ = 1, to = 20, orient = HORIZONTAL, bg = back, fg = fore)
        I = Scale(window, from_ = 1, to = 100, orient = HORIZONTAL, bg = back, fg = fore)
        L = Scale(window, from_ = 1, to = 100, orient = HORIZONTAL, bg = back, fg = fore)
        T = Scale(window, from_ = 2, to = 25, orient = HORIZONTAL, bg = back, fg = fore)
        MAX = Scale(window, from_ = 1, to = 10, orient = HORIZONTAL, bg = back, fg = fore)
        y = Scale(window, from_ = 5, to = 25, orient = HORIZONTAL, bg = back, fg = fore)
        slew = Scale(window, from_ = 1, to = 600, orient = HORIZONTAL, bg = back, fg = fore)
        gear = Scale(window, from_ = 1, to = 10, orient = HORIZONTAL, bg = back, fg = fore)

        KpLabel.grid(row = 0, column = 0)
        KiLabel.grid(row = 0, column = 2)
        KdLabel.grid(row = 0, column = 4)
        apLabel.grid(row = 1, column = 0)
        avLabel.grid(row = 1, column = 2)
        oLabel.grid(row = 1, column = 4)
        nLabel.grid(row = 2, column = 0)
        fLabel.grid(row = 2, column = 2)
        iLabel.grid(row = 2, column = 4)
        lLabel.grid(row = 3, column = 0)
        tLabel.grid(row = 3, column = 2)
        maxLabel.grid(row = 3, column = 4)
        yLabel.grid(row = 4, column = 0)
        slewLabel.grid(row = 4, column = 2)
        gearLabel.grid(row = 4, column = 4)
        
        Kp.grid(row = 0, column = 1)
        Ki.grid(row = 0, column = 3)
        Kd.grid(row = 0, column = 5)
        AP.grid(row = 1, column = 1)
        AV.grid(row = 1, column = 3)
        o.grid(row = 1, column = 5)
        n.grid(row = 2, column = 1)
        f.grid(row = 2, column = 3)
        I.grid(row = 2, column = 5)
        L.grid(row = 3, column = 1)
        T.grid(row = 3, column = 3)
        MAX.grid(row = 3, column = 5)
        y.grid(row = 4, column = 1)
        slew.grid(row = 4, column = 3)
        gear.grid(row = 4, column = 5)
        
        slider = True
        textButton.configure(text = "Text Boxes")

def nightMode():
    global night
    global back
    global fore
    
    if(night):
        night = False
        back = "white"
        fore = "#383838"
        window.configure(bg = back)
        
        KpLabel.configure(bg = back, fg = fore)
        KiLabel.configure(bg = back, fg = fore)
        KdLabel.configure(bg = back, fg = fore)
        apLabel.configure(bg = back, fg = fore)
        avLabel.configure(bg = back, fg = fore)
        oLabel.configure(bg = back, fg = fore)
        nLabel.configure(bg = back, fg = fore)
        fLabel.configure(bg = back, fg = fore)
        iLabel.configure(bg = back, fg = fore)
        lLabel.configure(bg = back, fg = fore)
        tLabel.configure(bg = back, fg = fore)
        maxLabel.configure(bg = back, fg = fore)
        yLabel.configure(bg = back, fg = fore)
        slewLabel.configure(bg = back, fg = fore)
        gearLabel.configure(bg = back, fg = fore)
        blankRow.configure(bg = back, fg = fore)
        avButton.configure(fg = 'black')
        runButton.configure(fg = 'black')
        nmButton.configure(text = "NightMode", bg = fore, fg = back)
        textButton.configure(bg = fore, fg = back)
        blankRow2.configure(bg = back, fg = fore)
        blankRow3.configure(bg = back, fg = fore)
        cLabel.configure(bg = back, fg = fore)
        

        if(slider):
            Kp.configure(bg = back, fg = fore)
            Ki.configure(bg = back, fg = fore)
            Kd.configure(bg = back, fg = fore)
            AP.configure(bg = back, fg = fore)
            AV.configure(bg = back, fg = fore)
            o.configure(bg = back, fg = fore)
            n.configure(bg = back, fg = fore)
            f.configure(bg = back, fg = fore)
            I.configure(bg = back, fg = fore)
            L.configure(bg = back, fg = fore)
            T.configure(bg = back, fg = fore)
            MAX.configure(bg = back, fg = fore)
            y.configure(bg = back, fg = fore)
            slew.configure(bg = back, fg = fore)
            gear.configure(bg = back, fg = fore)
        else:
            Kpt.configure(bg = back, fg = fore)
            Kit.configure(bg = back, fg = fore)
            Kdt.configure(bg = back, fg = fore)
            APt.configure(bg = back, fg = fore)
            AVt.configure(bg = back, fg = fore)
            ot.configure(bg = back, fg = fore)
            nt.configure(bg = back, fg = fore)
            ft.configure(bg = back, fg = fore)
            It.configure(bg = back, fg = fore)
            Lt.configure(bg = back, fg = fore)
            Tt.configure(bg = back, fg = fore)
            MAXt.configure(bg = back, fg = fore)
            yt.configure(bg = back, fg = fore)
            slewt.configure(bg = back, fg = fore)
            geart.configure(bg = back, fg = fore)

            blankR0.configure(bg = back, fg = fore)
            blankR.configure(bg = back, fg = fore)
            blankR2.configure(bg = back, fg = fore)
            blankR3.configure(bg = back, fg = fore)
            blankR4.configure(bg = back, fg = fore)
    else:
        night = True
        back = "#383838"
        fore = "white"
        window.configure(bg = back)

        KpLabel.configure(bg = back, fg = fore)
        KiLabel.configure(bg = back, fg = fore)
        KdLabel.configure(bg = back, fg = fore)
        apLabel.configure(bg = back, fg = fore)
        avLabel.configure(bg = back, fg = fore)
        oLabel.configure(bg = back, fg = fore)
        nLabel.configure(bg = back, fg = fore)
        fLabel.configure(bg = back, fg = fore)
        iLabel.configure(bg = back, fg = fore)
        lLabel.configure(bg = back, fg = fore)
        tLabel.configure(bg = back, fg = fore)
        maxLabel.configure(bg = back, fg = fore)
        yLabel.configure(bg = back, fg = fore)
        slewLabel.configure(bg = back, fg = fore)
        gearLabel.configure(bg = back, fg = fore)
        blankRow.configure(bg = back, fg = fore)
        avButton.configure(fg = fore)
        runButton.configure(fg = fore)
        nmButton.configure(text = "BrightMode", bg = fore, fg = back)
        textButton.configure(bg = fore, fg = back)
        blankRow2.configure(bg = back, fg = fore)
        blankRow3.configure(bg = back, fg = fore)
        cLabel.configure(bg = back, fg = fore)

        if(slider):
            Kp.configure(bg = back, fg = fore)
            Ki.configure(bg = back, fg = fore)
            Kd.configure(bg = back, fg = fore)
            AP.configure(bg = back, fg = fore)
            AV.configure(bg = back, fg = fore)
            o.configure(bg = back, fg = fore)
            n.configure(bg = back, fg = fore)
            f.configure(bg = back, fg = fore)
            I.configure(bg = back, fg = fore)
            L.configure(bg = back, fg = fore)
            T.configure(bg = back, fg = fore)
            MAX.configure(bg = back, fg = fore)
            y.configure(bg = back, fg = fore)
            slew.configure(bg = back, fg = fore)
            gear.configure(bg = back, fg = fore)
        else:
            Kpt.configure(bg = back, fg = fore)
            Kit.configure(bg = back, fg = fore)
            Kdt.configure(bg = back, fg = fore)
            APt.configure(bg = back, fg = fore)
            AVt.configure(bg = back, fg = fore)
            ot.configure(bg = back, fg = fore)
            nt.configure(bg = back, fg = fore)
            ft.configure(bg = back, fg = fore)
            It.configure(bg = back, fg = fore)
            Lt.configure(bg = back, fg = fore)
            Tt.configure(bg = back, fg = fore)
            MAXt.configure(bg = back, fg = fore)
            yt.configure(bg = back, fg = fore)
            slewt.configure(bg = back, fg = fore)
            geart.configure(bg = back, fg = fore)
            
            blankR0.configure(bg = back, fg = fore)
            blankR.configure(bg = back, fg = fore)
            blankR2.configure(bg = back, fg = fore)
            blankR3.configure(bg = back, fg = fore)
            blankR4.configure(bg = back, fg = fore)
        
def plotAV():
    global plotAngVel
    if(plotAngVel):
        plotAngVel = False
        avButton.configure(bg = "red")
    else:
        plotAngVel = True
        avButton.configure(bg = "green")
    
def runSim():
    #state variables
    if(slider):
        P = Kp.get() / 100.0
        In = Ki.get() / 100.0
        D = Kd.get() / 100.0
        ap = AP.get()
        av = AV.get()
        off = o.get()
        N = n.get()
        F = f.get()
        i = I.get() / 100.0
        l = L.get() / 100.0
        time = T.get()
        M = MAX.get()
        yLim = y.get()
        slewRate = slew.get()
        gearRatio = gear.get()
    else:
        P = Kp2.get()
        In = Ki2.get()
        D = Kd2.get()
        ap = AP2.get()
        av = AV2.get()
        off = o2.get()
        N = n2.get()
        F = f2.get()
        i = I2.get()
        l = L2.get() / 100.0
        time = T2.get()
        M = MAX2.get()
        yLim = y2.get()
        slewRate = slew2.get()
        gearRatio = gear2.get()

        if(P < 0):
            P = 0
        if(P > 3):
            P = 3
        if(In < 0):
            In = 0
        if(In > 3):
            In = 3
        if(D < 0):
            D = 0
        if(D > 3):
            D = 3
        if(ap < -10):
            ap = -10
        if(ap > 10):
            ap = 10
        if(av < -10):
            av = -10
        if(av > 10):
            av = 10
        if(off < -3):
            off = -3
        if(off > 3):
            off = 3
        if(N < 0):
            N = 0
        if(N > 100):
            N = 100
        if(F < 1):
            F = 1
        if(F > 25):
            F = 25
        if(i <= 0):
            i = 0.01
        if(i > 1):
            i = 1
        if(l < 0):
            l = 0
        if(l > 100):
            l = 100
        if(time < 2):
            time = 2
        if(time > 25):
            time = 25
        if(M < 2):
            M = 2
        if(M > 10):
            M = 10
        if(yLim < 5):
            yLim = 5
        if(yLim > 30):
            yLim = 30
        if(slewRate < 1):
            slewRate = 1
        if(slewRate > 600):
            slewRate = 600
        if(gearRatio < 1):
            gearRatio = 1
        if(gearRatio > 10):
            gearRatio = 10
        
    t = 0 #torque
    aa = 0 #angular accel
    aaPrev = ap #previous angular acc
    avPrev = av #previous angular vel
    apPrev = ap #previous angular pos
    
    #time variables
    dt = time / 200.0 #sim refresh rate
    if(time % 2 != 0):
        dt += 0.005
    if(time >= 18):
        dt += 0.01
    if(time >= 21):
        dt += 0.01
    count = 0 #how far along the sim is
    
    #other variables
    dR = 3.1416 / 180.0 # degrees to radians
    intg = 0
    PIDout = 0
    PIDprev = 0
    PIDactual = 0

    #matplotlib stuff
    ts = np.arange(0, time, dt)
    ap_plot = []
    av_plot = []
    pid_plot = []
    zero_plot = []
    pida_plot = []

    #close the previous graph
    plt.close()

    #plot dark mode
    if(night):
        plt.style.use('dark_background')
    else:
        plt.style.use('default')
    
    while(count < time):
        intg -= apPrev * dt

        PIDout = P * -apPrev + D * -avPrev + off

        if(PIDout > M + off):
            PIDout = M + off
        if(PIDout < -M + off):
            PIDout = -M + off

        if(In > 0):
            intg *= In
            if(intg > M - PIDout + off):
               intg = (M - PIDout + off)
            if(intg < -M - PIDout + off):
               intg = (-M - PIDout + off)
            intg /= In
            PIDout += intg * In
            
        servoCount = 0
        
        if(PIDout > PIDactual):
            
            while(servoCount < dt):
                PIDactual += slewRate / gearRatio * servoCount / 9.5
                
                if(PIDactual >= PIDout):
                    PIDactual = (PIDout + PIDprev) / 2
                    servoCount = dt + 1
                    
                servoCount += 0.001
        elif(PIDout < PIDactual and servoCount == 0):
            
            while(servoCount < dt):
                PIDactual -= slewRate / gearRatio * servoCount / 9.5
                
                if(PIDactual <= PIDout):
                    PIDactual = (PIDout + PIDprev) / 2
                    servoCount = dt + 1
                    
                servoCount += 0.001
        else:
            PIDactual = PIDout

        PIDprev = PIDactual
        
        aaPrev = aa
        apPrev = ap
        avPrev = av
         
        t = l * F * np.sin(PIDactual * dR)
            
        aa = t / i

        av += ((aa + aaPrev) / 2) * dt

        if(N > 0):
             av += (random.randrange(-N, N) / 100.0)

        ap += ((av + avPrev) / 2) * dt

        ap_plot.append(ap)
        if(plotAngVel):
            av_plot.append(av)
        pid_plot.append(PIDout - off)
        pida_plot.append(PIDactual - off)
        zero_plot.append(0)

        count += dt

    def c_extend(array):
        array.extend(np.full(len(ts) - len(array), array[0]))
        
    c_extend(ap_plot)
    if(plotAngVel):
            c_extend(av_plot)
    c_extend(pid_plot)
    c_extend(pida_plot)
    c_extend(zero_plot)

    fig, ax = plt.subplots()

    plt.ylim(-yLim, yLim)
    plt.plot(ts, ap_plot, label = 'Angular Position')
    plt.plot(ts, pid_plot, label = 'PID Output')
    plt.plot(ts, pida_plot, label = 'PID Actual')
    
    if(plotAngVel):
        plt.plot(ts, av_plot, label = 'Angular Velocity')
    if(night):
        plt.plot(ts, zero_plot, color = 'WHITE')
    else:
        plt.plot(ts, zero_plot, color = 'BLACK')

    plt.ylabel("Angle (D)")
    plt.xlabel("Time (S)")
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    plt.title('Anvil Tuner 0.53')
    plt.legend()
    plt.show()

nmButton = Button(window, text = "BrightMode", command = nightMode, bg = "white")
textButton = Button(window, text = "Text Boxes", command = textBox, bg = "white")
avButton = Button(window, text = "Plot AngVel", command = plotAV, bg = "red", fg = 'white')
runButton = Button(window, text = "Start Sim", command = runSim, bg = "green", fg = 'white')

nmButton.grid(row = 6, column = 0)
textButton.grid(row = 6, column = 1)
avButton.grid(row = 6, column = 2)
runButton.grid(row = 6, column = 3)

window.mainloop()
