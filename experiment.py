# coding=utf-8

# mass = [1,2,3,4,5,6]

'''
for element in mass:
    print(element)
    if element == 3:
        mass.remove(element)
mass
print(mass)
'''

import serial.tools.list_ports
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
ser.open()

while 1:
    line = ser.readline().decode('utf-8').strip()
    print(line)




print(ser.is_open)
ser.close()
print(ser.is_open)
# False