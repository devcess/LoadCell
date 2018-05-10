

import serial
import time

LogID = ""


def main():
    global LogID
    n = input("Enter serial port: ")
    try:
        s = serial.Serial(n, 9800, timeout=1)
    except:
        print("Bad port name try again")
    testPort(n)
    LogID = input("Enter Log ID: ")
    try:
        while True:
            Logging(n)
    except KeyboardInterrupt:
        print("done for now")


def testPort(usbID):
    s = serial.Serial(usbID, 9800, timeout=1)
    if s.readable():
        time.sleep(.01)
        text = s.readline()
        if text == "":
            testPort(usbID)
        else:
            print(text)


def Logging(usbID):
    global LogID
    s = serial.Serial(usbID, 9800, timeout=1)
    while True:
        if s.readable():
            time.sleep(.01)
            text = s.readline()
            if text == "":
                pass
            else:
                with open(LogID, "a") as f:
                    DateTime = str(time.strftime("%m/%d,%H:%M:%S"))
                    line = DateTime + "," + str(text) + "\n"
                    f.write(line)
                line = DateTime + "," + str(text)
                print(line)


main()
