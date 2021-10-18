# INITATE CODE BY RUNNING python read-serial.py IN TERMINAL

import serial

# SET UP SERIAL CONNECTION + CREATE .CSV FILE

#arduino_port = "/dev/cu.usbmodem14201" # CHANGE according serial port of Arduino
#baud = 9600 #arduino uno runs at 9600 baud

arduino = serial.Serial(port='COM4', baudrate=9600, timeout=.1)
fileName = "AVF_data.csv" #name of the CSV file generated

ser = serial.Serial(arduino_port, baud)
print("Connected to Arduino port:" + arduino_port)
file = open(fileName, "a")
print("Created file")

# DATA COLLECTION FROM ARDUINO

samples = 10 #how many samples to collect
print_labels = False
line = 0 #start at 0 because our header is 0 (not real data)
while line <= samples:
    # incoming = ser.read(9999)
    # if len(incoming) > 0:
    if print_labels:
        if line == 0: # first line
            print("Printing Column Headers")
        else: # subsequent lines
            print("Line " + str(line) + ": writing...")
    getData=str(ser.readline())
    data=getData[0:][:-2] # might have to CHANGE this depending on the data
    print(data)

    file = open(fileName, "a")
    file.write(data + "\\n") #write data with a newline
    line += 1

print("Data collection complete!")
file.close()