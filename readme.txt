Aim:
Aim of this project is to read data from a csv file, eg. uploaded 'data_input_file.csv' in repository as sample, in this case we are reading sensor 1 and sensor 2 values. We then compare each sensor value data with the previous data and check wether it exceeds the threshold value, if it exceeds then we increase the number of count and store that value in csv format in a list and then send to a server. The threshold value is input/asked by user for both the sensors.

Following
--> data_reporting.py file

1)   Data Reading
(i)  The path of csv file is copied to "path" variable. Change '\' with '/' for complete path.
(ii) CSV library is used to open csv file using built in open() function and read by using reader object.

2)   Data Checking
(i)  Threshold value is taken by user for sensor 1.
(ii) for loop is used to check weather each element in list of sensor 1 is within the given threshold,
     if not the it is reported and count is increased.
(iii)step (i) and (ii) are repeated for sensor 2.
(iv) Reported data values for both the sensors are seperated with ';' delimiter using join() method. 

3)   Data Publishing
(i)  UTC timestamp is calculated and rounded off into milliseconds.
(ii) Data to be transferred i.e. reported sensor_1 values, reported sensor_2 values, UTC_timestrap,count1 and count2
     are concatenated into one data_point list.
(iii)All this data are arranged as a text string with ';' delimiter using join method.
(iv) Pickling is done to serialize the data, ready to be transferred.
(v)  Socket is created with same host_name and port as server in order to transfer the data to server.

-->  data_report_server.py file

(i)  A TCP server is created which is used to recieve file from the client.
(ii) Recieved data is unpickled and the printed at server page.



