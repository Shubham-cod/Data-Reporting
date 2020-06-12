# Project: Data reporter
# Author:  Shubham Agarwal
# Date:    01/06/2020

#importing modules
import csv
import socket
import pickle
import datetime
from datetime import timezone

#defining lists and variables
data_1 = []      #list for collecting first column values from csv file
data_2 = []      #list for collecting second column values from csv file
maxCount_1 = 0   #variable for counting data reported from list of data_1[]
maxCount_2 = 0   #variable for counting data reported from list of data_2[]

########################################################   Data Reading   ####################################################

#opening csv file and reading its columns to respective data_1 and data_2 lists
path = 'C:/Users/SHUBHAM/Desktop/New folder/Teraki_task/data_input_file.csv'        #Give path of csv file here
with open(path) as csvDataFile:
    csvReader = csv.reader(csvDataFile,delimiter=';')
    for row in csvReader:
        data_1.append(row[0])                               #appending sensor 1 values to data_1
        data_2.append(row[1])                               #appending sensor 2 values to data_2

#converting data_1 of Sensor 1 string list into integer
for i in range(1,len(data_1)):
    data_1[i] = int(data_1[i])

#converting data_2 of Sensor 2 string list into float
for i in range(1,len(data_2)):
    data_2[i] = float(data_2[i])

#######################################################   Data Checking   ####################################################
    
#calculating number of reported data points for sensor 1
threshold_value1 = float(input("Enter threshold value for sensor 1\n"))       #asking user for threshold value and converting to int
data1_point = []                                                              #list for storing all reported values

for i in range(1,len(data_1)-1):
    if abs(data_1[i] - data_1[i+1])>threshold_value1:
        data1_point.append(data_1[i])
        maxCount_1 += 1
    else:
        continue
    
#print(maxCount_1)

#arranging reported data values seperated with ';' delimiter
data1_str = 0
for j in range(0,len(data1_point)):
    data1_str = ';'.join(map(str,(data1_point)))
    

#calculating number of reported data points for sensor 2
threshold_value2 = float(input("Enter threshold value for sensor 2\n"))     #asking user for threshold value and converting to float
data2_point = []                                                            #list for storing all reported values

for i in range(1,len(data_2)-1):
    if abs(data_2[i] - data_2[i+1])>threshold_value2:
        data2_point.append(data_2[i])
        maxCount_2 += 1
    else:
        continue
    
#print(maxCount_2)

#arranging reported data values seperated with ';' delimiter
data2_str = 0
for j in range(0,len(data2_point)):
   data2_str = ';'.join(map(str,(data2_point)))
    
#print(data2_str)

###################################################   Data Publishing     #########################################################
    
#UTC timestamp
dt = datetime.datetime.now()                                #Getting current time  
utc_time = dt.replace(tzinfo = timezone.utc)                #converting our datetime to UTC
utc_timestamp = round(utc_time.timestamp() * 1000)          #UTC time in millisecond

#print(utc_timestamp) 


data_point = []                                 #list containing reported sensor_1, sensor_2 values, UTC_timestrap,count1 & count2
                                                #last 2 values are the count of reported sensor_1 & sensor_2  respectively
data_point.append(utc_timestamp)        
data_point.append(data1_str)
data_point.append(data2_str)
data_point.append(maxCount_1) 
data_point.append(maxCount_2)            


data_point = ';'.join(map(str,data_point))      #arranging the data to be published in text string with ';' as delimiter

print(data_point)

#creating client for transfering the data
publish_data = pickle.dumps(data_point)         #using pickle technique to serialize data to be published 

HOST = '127.0.0.1'                              # The server's hostname or IP address
PORT = 65432                                    # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(publish_data)
    data = s.recv(1024)
s.close()


####################################################     END      ###############################################################
