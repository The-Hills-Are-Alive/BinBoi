from gpiozero import *
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
  #def moveLeft(self, hardness):
    #leg1.foward(hardness):
    #leg2.stop()
  #def moveRight(self, hardness):
    #leg2.foward(hardness):
    #leg1.stop()
  #def stop(self):
    #leg1.stop()
    #leg2.stop()
#main
bruh=Big_work()
