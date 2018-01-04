#!/usr/bin/env python
#coding:utf-8
with open("AE-BME280_data.csv","r") as read_file,open("AE-BME280_graph.csv","w") as write_file:
    write_file.write("time, temperature, humidity, pressure,\n")
    for read_line in read_file:
        divided_line = read_line[19:-1].split(":")
        #current_time = read_line[0:19]
        current_time = read_line[5:16]
        temperature = str(int(divided_line[10].lstrip("tm="))/100)
        humidity = str(int(divided_line[11].lstrip("hu="))/100)
        atmospheric_pressure = divided_line[12].lstrip("at=")
        write_file.write(current_time + "," + temperature + "," + humidity + "," +atmospheric_pressure + "\n")
