#load iRobot API
import create

#enable sleep
from time import sleep

#create robot object. uncomment line for your operation system
#windows
#robot = create.Create(4)
#macos
#robot = create.Create("/dev/tty.KeySerial1")
#linux
robot = create.Create("/dev/ttyUSB0")

def dot():
    return("dot() not implemented")
def dash():
    return("dash() not implemented")

inputString = input("Enter text to be translated: ")

#to do: remove spaces & punctuation
