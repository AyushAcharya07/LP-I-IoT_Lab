import RPi.GPIO as g
import time

g.setmode(g.BOARD)
g.setup(3,g.OUT)
g.setup(5,g.OUT)

g.output(3,True) # Instead of True-> g.HIGH or 1
time.sleep(3)
g.output(3,False) # Instead of False-> g.LOW or 0

g.output(3,True)
time.sleep(3)
g.output(3,False)

g.cleanup()
