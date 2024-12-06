from irover import *
from time import sleep
w=IROVER()
w.OK()
L = 2800
R = 2900
L1 = w.analog(33)
R1 = w.analog(34)
def check() :
    while True:
        w.fill(0)
        w.text("L=%d"%w.analog(33),0,0)
        w.text("R=%d"%w.analog(34),0,12)
        w.show()
        sleep(0.2)

def wall() :
    while True:
        if w.analog(35) > 100 :
            if w.analog(33) < 2800 and w.analog(34) < 2800 :
                w.fd2(30,31)
                sleep(0.01)
            if w.analog(33) > 2800 and w.analog(34) < 2800 :
                w.tr(50)
                sleep(0.02)
            if w.analog(33) < 2800 and w.analog(34) > 2800 :
                w.tl(50)
                sleep(0.02)
            if w.analog(33) > 2800 and w.analog(34) > 2800 :
                w.fd2(53,53)
                sleep(0.01)
        else :
            w.stop()
            rr()
            w.stop()
            break
        
def track() :
    while True:
        if w.analog(33) < 2800 and w.analog(34) < 2800 :
            w.fd2(20,21)
            sleep(1.4)
            w.stop()
            break
        if w.analog(33) > 2800 and w.analog(34) < 2800 :
            w.tr(50)
            sleep(0.02)
        if w.analog(33) < 2800 and w.analog(34) > 2800 :
            w.tl(50)
            sleep(0.02)
        if w.analog(33) > 2800 and w.analog(34) > 2800 :
            w.fd2(40,41)
            sleep(0.01)
def trackaaa() :
    while True:
        if w.analog(33) < 2800 and w.analog(34) < 2800 :
            w.fd2(20,21)
            sleep(0.5)
            w.stop()
            break
        if w.analog(33) > 2800 and w.analog(34) < 2800 :
            w.tr(50)
            sleep(0.02)
        if w.analog(33) < 2800 and w.analog(34) > 2800 :
            w.tl(50)
            sleep(0.02)
        if w.analog(33) > 2800 and w.analog(34) > 2800 :
            w.fd2(40,41)
            sleep(0.01)
def tracks() :
    while True:
        if w.analog(33) < 2800 and w.analog(34) < 2800 :
            w.fd2(20,21)
            sleep(0.8)
            w.sl(25)
            sleep(0.2)
            w.stop()
            break
        if w.analog(33) > 2800 and w.analog(34) < 2800 :
            w.tr(64)
            sleep(0.135)
        if w.analog(33) < 2800 and w.analog(34) > 2800 :
            w.tl(64)
            sleep(0.135)
        if w.analog(33) > 2800 and w.analog(34) > 2800 :
            w.fd2(35,35)
            sleep(0.01)
def trackf() :
    while True:
        if w.analog(33) < 2800 and w.analog(34) < 2800 :
            w.fd2(20,21)
            sleep(0.5)
            w.stop()
            break
        if w.analog(33) > 2800 and w.analog(34) < 2800 :
            w.tr(58)
            sleep(0.03)
        if w.analog(33) < 2800 and w.analog(34) > 2800 :
            w.tl(58)
            sleep(0.03)
        if w.analog(33) > 2800 and w.analog(34) > 2800 :
            w.fd2(53,53)
            sleep(0.01)
def trackfaa() :
    while True:
        if w.analog(33) < 2800 and w.analog(34) < 2800 :
            w.fd2(20,21)
            sleep(0.5)
            w.stop()
            break
        if w.analog(33) > 2800 and w.analog(34) < 2800 :
            w.tr(58)
            sleep(0.03)
        if w.analog(33) < 2800 and w.analog(34) > 2800 :
            w.tl(58)
            sleep(0.03)
        if w.analog(33) > 2800 and w.analog(34) > 2800 :
            w.fd2(45,45)
            sleep(0.01)
def trackfs() :
    while True:
        if w.analog(33) < 2800 and w.analog(34) < 2800 :
            w.fd2(20,21)
            sleep(0.5)
            w.sl(25)
            sleep(0.2)
            w.stop()
            break
        if w.analog(33) > 2800 and w.analog(34) < 2800 :
            w.tr(65)
            sleep(0.06)
        if w.analog(33) < 2800 and w.analog(34) > 2800 :
            w.tl(65)
            sleep(0.06)
        if w.analog(33) > 2800 and w.analog(34) > 2800 :
            w.fd2(70,70)
            sleep(0.01)
def trackb() :
    while True:
        if w.analog(33) < 2800 and w.analog(34) < 2800 :
            w.stop()
            break
        if w.analog(33) > 2800 and w.analog(34) < 2800 :
            w.tr(55)
            sleep(0.05)
        if w.analog(33) < 2800 and w.analog(34) > 2800 :
            w.tl(55)
            sleep(0.05)
        if w.analog(33) > 2800 and w.analog(34) > 2800 :
            w.fd2(52,52)
            sleep(0.01)

def rr() :
    while True:
        w.sr(50)
        sleep(0.42)
        w.stop()
        break
def rt() :
    while True:
        if w.analog(34) > 2800 :
            w.sr(50)
            sleep(0.01)
        else :
            w.sr(50)
            sleep(0.1)
            w.stop()
            break
def lt() :
    while True:
        if w.analog(33) > 2800 :
            w.sl(50)
            sleep(0.01)
        else :
            w.sl(50)
            sleep(0.1)
            w.stop()
            break    
def ll() :
    while True:
        w.sl(50)
        sleep(0.38)
        w.stop()
        break
def back() :
    while True:
        w.bk(30)
        sleep(1)
        rt()
        break
def backtwo() :
    while True:
        w.bk(35)
        sleep(0.5)
        rt()
        rt()
        rt()
        break
def twoback() :
    while True:
        w.bk(30)
        sleep(1)
        w.sr(50)
        sleep(2.3)
        w.stop()
        break
def fd() :
    while 1 :
        w.fd(50)
        sleep(0.3)
        break
def bk() :
    while True :
        w.bk(30)
        sleep(0.8)
        break
while 1 :
    trackf()
    lt()
    trackf()
    lt()
    trackb()
    back()
    track()
    lt()
    tracks()####\
    bk()
    track()
    lt()
    trackaaa()
    backtwo()
    trackf()
    lt()
    wall()
    trackfaa()
    lt()
    trackf()
    fd()
    #track()
    #lt()
    #track()
    #lt()
    #track()
    #check()
    w.stop()
    break
    