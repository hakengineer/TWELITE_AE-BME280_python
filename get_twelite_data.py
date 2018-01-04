#!/usr/bin/env python
#coding: utf-8
import time
import datetime
import serial
ser = serial.Serial("/dev/ttyUSB0", 115200)
output_data = ""
with open("AE-BME280_data.csv","a") as write_file:
    try:
        while (True):
            receive_data = ser.read(1).decode("utf-8")
            if receive_data == "\n":
                current_time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
                print("{0} {1}".format(current_time, output_data))
                write_file.write("{0} {1}".format(current_time, output_data))
                write_file.write("\n")
                write_file.flush()
                output_data = ""
            else:
                output_data = output_data + receive_data
    except KeyboardInterrupt:
        print("Ctrl + C")
        ser.close()
