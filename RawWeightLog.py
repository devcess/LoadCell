

import serial
import time



def Logging(usb, log_name, delay):
    read = ReadValues(usb)
    read = round(read, 1)
    with open(log_name, "a") as f:
        DateTime = str(time.strftime("%m/%d,%H:%M:%S"))
        line = DateTime + "," + str(read) + "\n"
        f.write(line)
    print("Current Reading: " + str(read) + " g")



def ReadValues(usb):
    s = serial.Serial(usb, 9800, timeout=1)
    if s.readable():
        time.sleep(.01)
        text = s.readline().decode()
        text = CleanData(text)
        text = text * 453.592
        text = round(text, 1)
        return text


def CleanData(data):
    try:
        data = data.replace("+", "")
        data = data.replace("lbs", "")
        data = float(data)
        return data
    except:
        print("READ ERROR")
        return 0.0

usb = input("Enter USB device name: ")
log_name = input("Enter log name: ")
delay = int(input("Seconds between samples: "))

try:
    while True:
        Logging(usb, log_name, delay)
        time.sleep(delay)
except KeyboardInterrupt:
    print("Program Closed")
