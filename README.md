# TWELITE_AE-BME280_python
Acquire information of AE-BME280 via TWELITE

# Overview
It consists of two codes.
One is a code to receive data from AE-BME 280 via TWELITE.
The other is a code for processing graphs of received data.

# Features
CPU usage rate does not become 100%

# requirement
I used this version of python 3.

```console
Python 3.5.3
```

I used this version of package or module.

```console
pyserial==3.2.1
```

# Usage
1. Data sent from AE-BME280 via TWELITE is output to a file. When this command is executed, the result is output to the prompt and AE-BME 280_data.csv.

```console
$ python3 get_twelite_data.py
```

If you do it in the background
```console
$ nohup python3 get_twelite_data.py &
```

Example of AE-BME 280_data.csv
```console
2018/01/03 12:15:09 ::rc=80000000:lq=111:ct=206E:ed=810E4653:id=1:ba=2660:a1=0808:a2=0407:tm=2280:hu=5264:at=1008
2018/01/03 12:16:09 ::rc=80000000:lq=75:ct=206F:ed=810E4653:id=1:ba=2665:a1=0808:a2=0407:tm=2282:hu=5264:at=1008
2018/01/03 12:17:08 ::rc=80000000:lq=75:ct=2070:ed=810E4653:id=1:ba=2660:a1=0805:a2=0405:tm=2282:hu=5235:at=1008
2018/01/03 12:18:08 ::rc=80000000:lq=84:ct=2071:ed=810E4653:id=1:ba=2665:a1=0808:a2=0405:tm=2282:hu=5250:at=1008
2018/01/03 12:19:07 ::rc=80000000:lq=87:ct=2072:ed=810E4653:id=1:ba=2665:a1=0808:a2=0407:tm=2284:hu=5234:at=1008
2018/01/03 12:20:06 ::rc=80000000:lq=78:ct=2073:ed=810E4653:id=1:ba=2665:a1=0805:a2=0405:tm=2284:hu=5239:at=1008
2018/01/03 12:21:06 ::rc=80000000:lq=102:ct=2074:ed=810E4653:id=1:ba=2665:a1=0808:a2=0405:tm=2285:hu=5228:at=1008
2018/01/03 12:22:05 ::rc=80000000:lq=102:ct=2075:ed=810E4653:id=1:ba=2660:a1=0808:a2=0407:tm=2286:hu=5225:at=1008
```


2. When this command is executed, AE-BME280_graph.csv file is output based on AE-BME280_data.csv.

```console
$ python3 make_graph_data.py
```

Example of AE-BME280_graph.csv
```console
time, temperature, humidity, pressure,
12/31 16:37,20.4,48.0,1012
12/31 16:38,20.41,48.44,1012
12/31 16:38,20.41,49.78,1012
12/31 16:39,20.42,49.87,1012
12/31 16:40,20.4,50.01,1012
12/31 16:41,20.42,50.23,1012
```


3. There is no graphing code here. Please try graphing with pandas or matplotlib. Sorry

For details, please refer to this page

https://hakengineer.xyz/2018/01/05/post-859/

# Installation
```console
$ git clone https://github.com/hakengineer/TWELITE_AE-BME280_python.git
```

# Author
hakengineer

# Licence
MIT

