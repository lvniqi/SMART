#-*- coding: utf-8 -*-
from serial import Serial
from serial.tools import list_ports 
from binascii import b2a_hex as str2int
from binascii import a2b_hex as int2str

def List2Str(str_list):
    str_temp = ''
    for x in str_list:
        temp  =hex(x)[2:]
        if len(temp) == 1:
            temp = '0'+temp
        str_temp+=int2str(temp)
    return str_temp

class Uart(Serial):
    def __init__(self,baudrate = 57600,timeout = 1):
        Serial.__init__(self)
        self.setBaudrate(baudrate)
        self.setTimeout(timeout)
        self.GetFreePort()
    
    def GetFreePort(self):
        self.freeport = list(list_ports.comports())
        
    def SetPortAuto(self):
        self.GetFreePort()
        if self.freeport:
            self.port  = self.freeport[0][0]
            self.close()
            return True
        else:
            return False
     
    def ReSetPort(self,port,baudrate):
        self.port = port
        self.baudrate = baudrate

    def GetData(self):
        data1 = []
        while True:
            b = self.read()
            if b == '' :
                return None
            else :
                if str2int(str(b)) != 'ff' :
                    data_base = str2int(str(b))
                    data1.append(int(data_base,16))
                    
                else:
                        return data1
        
        
                
if __name__ == "__main__":
    a = Uart()
    a.SetPortAuto()
    a.open()
    List2Str([1,2,3])
    '''while(True):
        b = str2int(a.read())
        if b != '':
            print int(b,16)'''
