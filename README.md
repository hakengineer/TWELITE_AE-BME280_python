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

`Python 3.5.3`

I used this version of package or module.

`pyserial==3.2.1`

# Usage
1. Data sent from AE-BME280 via TWELITE is output to a file.
When this command is executed, the result is output to the prompt and AE-BME 280_data.csv.

`python3 get_twelite_data.py`

If you do it in the background

`nohup python3 get_twelite_data.py &`

2. When this command is executed, AE-BME280_graph.csv file is output based on AE-BME280_data.csv.

`python3 make_graph_data.py`

3. There is no graphing code here.
Please try graphing with pandas or matplotlib.
Sorry

For details, please refer to this page


# Installation
``$ git clone https://github.com/hakengineer/TWELITE_AE-BME280_python.git``

# Author
hakengineer

# Licence
MIT

