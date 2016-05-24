import serial
import time

class RN4870:
    def __init__(self,name):
        self.baud = 115200
        self.name = name
        self.ser = serial.Serial()
        self.ser.baudrate = self.baud
        self.ser.timeout = 6
        self.error_flag = 0
        self.mode = 0

    def set_port(self, comm):
        self.ser.port = str(comm)
        print self.ser.port

    def close_connection(self):
        self.ser.close()

    def open_connection(self):
        try:
            self.ser.open()
        except:
            self.error_flag = 100  #Error opening the comm port
            print self.error_flag

    def command_mode(self):
        if self.ser.isOpen() is not True:
            self.open_connection()
        if self.ser.isOpen():
            self.ser.write('$$$')
            time.sleep(1)
            response = self.ser.read(4)
            print response
            self.mode = 1
            if response != 'CMD>':
                self.error_flag = 101      # Cannot get in to command mode
                print self.error_flag

    def reboot(self):
        if self.mode is not 1:
            self.command_mode()
        else:
            command = 'R,1'
            command += '\r\n'
            print command
            self.ser.write(command)
            response = self.ser.readline()
            print response
            response = self.ser.read(8)
            print response

    def send_command(self, command):
        command += "\r\n"
        print command
        self.ser.write(command)
        response1 = self.ser.readline()
        print response1

    def factory_reset(self):
        if self.mode is not 1:
            self.command_mode()
        else:
            command = 'SF,1'
            command += '\r\n'
            print command
            self.ser.write(command)
            response = self.ser.readline()
            print response
            response = self.ser.read(8)
            print response

    def set_name(self, name):
        command = 'SN,' + name
        self.send_command(command)

    def program_script(self, command):
        command += "\r\n"
        print command
        self.ser.write(command)
        time.sleep(0.2)

