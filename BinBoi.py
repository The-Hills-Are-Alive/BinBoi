from gpiozero import *
import board
import neopixel
pixel_pin = board.D18
num_pixels = 30
ORDER = neopixel.GRB
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)
sensorM = DigitalInputDevice(25)
sensorL = DigitalInputDevice(15)
sensorR = DigitalInputDevice(24)
Densor = Distance sensor (14,18)
#leg1 = Moter(#pin1,pin2)
#leg2 = Moter(#pin1,pin2)
class Big_work:
  def __init__(self):
    #print(sensorR.value, "R", sensorL.value, "L", sensorM.value, "M")
    if self.check("L")==0:
      #self.moveLeft(0.3)
      print("breb")
    elif self.check("R")==0:
      #self.moveRight(0.3)
      print("movingRight")
    elif self.check("M")==0:
      #moveFoward(0.3)
      print("moving")
    else:
      #self.stop
      print("stop")
    print(Densor.distance)
  
  def check(self, typ):
    #if Densor.distance > 10:
    if typ == "R":
      return sensorR.value
    elif typ == "L":
      return sensorL.value
    elif typ =="M":
      return sensorM.value
    return 0
  #def moveFoward (self, hardness):
    #leg1.foward(hardness)
    #leg2.foward(hardness)
    #pixels.fill((22, 247, 210))
  #def moveLeft(self, hardness):
    #leg1.foward(hardness):
    #leg2.stop()
    #pixels.fill((229, 5, 237))
  #def moveRight(self, hardness):
    #leg2.foward(hardness):
    #leg1.stop()
    #pixels.fill((0, 255, 0))
  #def stop(self):
    #leg1.stop()
    #pixels.fill((0, 255, 0))
    #leg2.stop()
#main
bruh=Big_work()
