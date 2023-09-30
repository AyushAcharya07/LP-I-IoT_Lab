import Rpi.GPIO as g
import time

g.setmode(g.BOARD)

g.setup(12,g.IN)
g.setup(22,g.OUT)

while True:
  var=g.input(12)
  print(var)
  if var==1:
    g.output(22,True)
    time.sleep(5)
  else:
    g.output(22,False)

g.cleanup()
