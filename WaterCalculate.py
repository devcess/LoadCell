'''
Moisture Content Calculator 

This program calculates the water % of object placed on load cell

Input is a file with USB port, Tar value, wet value and dry value.
Wet value is not used but is stored in the file for reference. 

File format should be: 
    FileID,USB-port,Tar,wet,dry

All in grams. 

Program will log values to local file complete with date and time
'''



import serial
import time

# Startup loads values from id file 

def Startup():
    # TODO: ADD IN FILE LOAD FIRST
    Values = []
    print("No file Loaded")
    n = input("Enter ID to load: ")
    try:
        Values = LoadValues(n)
        print(Values)
        return(Values)
    except:
        print("File not found")

# strip files from txt file

def LoadValues(filename):
    f = open(filename, 'r')
    f = f.read()
    f = f.split(",")
    # f[0] = SampleID, f[1] = usbID, f[2] = Tar Value, f[3] = Wet Value, f[4] = dry value
    f[2] = float(f[2])
    f[3] = float(f[3])
    f[4] = float(f[4])
    return f


def Logging(Values):
   
    currentWeight = ReadValues(Values[1]) - Values[2]
    currentWeight = round(currentWeight, 1)
    WaterPercent = currentWeight - Values[4] #Dry value
    WaterPercent = WaterPercent / Values[4]
    WaterPercent = WaterPercent * 100
    WaterPercent = round(WaterPercent, 1)
    logFile = Values[0] + "WaterLog"
    with open(logFile, "a") as f:
         DateTime = str(time.strftime("%m/%d,%H:%M:%S"))
         line = DateTime + "," + str(currentWeight) + "," + str(WaterPercent) + "\n"
         f.write(line)
    print("Current Reading: " + str(currentWeight) + " g")
    print("Current Reading: " + str(WaterPercent) + " %")
    time.sleep(60)



def ReadValues(usbID):
    s = serial.Serial(usbID, 9800, timeout=1)
    if s.readable():
        time.sleep(.01)
        text = s.readline().decode()
        text = CleanData(text)
        text = text * 453.592 # convert to grams
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

def main():
    Values = Startup()
    try:
        while True:
            Logging(Values)
    except KeyboardInterrupt:
        print("Program closed")

main()

