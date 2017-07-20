# coding=utf-8
import time, datetime
import serial.tools.list_ports

'''
mass = [1,2,3,4,5,6]
for element in mass:
    print(element)
    if element == 3:
        mass.remove(element)
mass
print(mass)
'''

ports = serial.tools.list_ports.comports()
for port in ports:
    print(port)

ser = serial.Serial()
ser.port = 'COM4'
ser.baudrate=57600
ser.bytesize=8
ser.parity='N'
ser.stopbits=1
# ser.timeout=1
ser.xonxoff=0
ser.rtscts=0
res = ser.open()

int_number_of_line = 0
while 1:
    int_number_of_line += 1
    now = datetime.datetime.now()
    current_time = now.strftime("%Y-%m-%d\t%Hh%Mm%Ss")
    #current_time = str(now.date()) + '\t' + str(now.hour) + 'h' + str(now.minute) + 'm' + str(now.second)+'s'
    # line = str(int_number_of_line) +'\t'+ current_time +'\t\t'+ str(ser.readline().decode('utf-8').strip())
    port_data = ser.readline()
    #print("Bytes - `{0}`, string - `{1}`".format(repr(port_data), port_data.decode('utf-8')))
    #port_data = port_data.decode('utf-8')
    line = str(int_number_of_line) +'\t'+ current_time +'\t\t'+ str(port_data)#.decode('utf-8').strip()
    print(line) # .encode('utf8')
    #time.sleep(0.1)

print(ser.is_open)
ser.close()
print(ser.is_open)
# False