import Adafruit_DHT
import RPi.GPIO as g

g.setmode(g.BCM)

while True:
  humidity,temperature=Adafruit_DHT.read_retry(Adafruit_DHT.DHT11,2)
  print(humidity,temperature)

g.cleanup()
