from control_models import cr2fp
from binascii import unhexlify


class ControlProtocol(object):

    def __init__(self, model):
        if model == 'cr2fp':
            self.control = cr2fp.CR2FP()
            print('omg omg omg: %r' % self.control)
        else:
            raise

    # BINARY SECTION:
    def volume_down(self):   # return the binary code for VOLUME DOWN
        try:
            cmd = unhexlify(self.control.VOLUME_DOWN)
        except Exception as error:
            cmd = None
        return cmd

    def volume_up(self):     # return the binary code for VOLUME UP
        try:
            cmd = unhexlify(self.control.VOLUME_UP)
        except Exception as error:
            cmd = None
        return cmd

    def channel_down(self):  # return the binary code for CHANNEL DOWN
        try:
            cmd = unhexlify(self.control.CHANNEL_DOWN)
        except Exception as error:
            cmd = None
        return cmd

    def channel_up(self):    # return the binary code for CHANNEL_UP
        try:
            cmd = unhexlify(self.control.CHANNEL_UP)
        except Exception as error:
            cmd = None
        return cmd

    def number0(self):       # return the binary code for NUMBER 0
        try:
            cmd = unhexlify(self.control.NUMBER_0)
        except Exception as error:
            cmd = None
        return cmd

    def number1(self):       # return the binary code for NUMBER 1
        try:
            cmd = unhexlify(self.control.NUMBER_1)
            print("entrou no try")
        except Exception as error:
            cmd = None
            print("entrou no except")
        return cmd

    def number2(self):       # return the binary code for NUMBER 2
        try:
            cmd = unhexlify(self.control.NUMBER_2)
        except Exception as error:
            cmd = None
        return cmd

    def number3(self):       # return the binary code for NUMBER 3
        try:
            cmd = unhexlify(self.control.NUMBER_3)
        except Exception as error:
            cmd = None
        return cmd

    def number4(self):       # return the binary code for NUMBER 4
        try:
            cmd = unhexlify(self.control.NUMBER_4)
        except Exception as error:
            cmd = None
        return cmd

    def number5(self):       # return the binary code for NUMBER 5
        try:
            cmd = unhexlify(self.control.NUMBER_5)
        except Exception as error:
            cmd = None
        return cmd

    def number6(self):       # return the binary code for NUMBER 6
        try:
            cmd = unhexlify(self.control.NUMBER_6)
        except Exception as error:
            cmd = None
        return cmd

    def number7(self):       # return the binary code for NUMBER 7
        try:
            cmd = unhexlify(self.control.NUMBER_7)
        except Exception as error:
            cmd = None
        return cmd

    def number8(self):       # return the binary code for NUMBER 8
        try:
            cmd = unhexlify(self.control.NUMBER_8)
        except Exception as error:
            cmd = None
        return cmd

    def number9(self):       # return the binary code for NUMBER 9
        try:
            cmd = unhexlify(self.control.NUMBER_9)
        except Exception as error:
            cmd = None
        return cmd
