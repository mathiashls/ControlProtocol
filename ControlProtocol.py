from control_models import cr2fp
from binascii import unhexlify

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class ControlProtocol(DatagramProtocol):

    def __init__(self, model):
        if model == 'cr2fp':
            self.control = cr2fp
        else:
            raise
        self.host = "192.168.1.238"
        self.port = 7001
        self.transport.connect(self.host, self.port)

    def protocol_callback(self):
        # callback used only for tests with a computer keyboard
        while True:
            button_pressed = raw_input()
            if button_pressed == '0':
                self.number0
            elif button_pressed == '1':
                self.number1
            elif button_pressed == '2':
                self.number2
            elif button_pressed == '3':
                self.number3
            elif button_pressed == '4':
                self.number4
            elif button_pressed == '5':
                self.number5
            elif button_pressed == '6':
                self.number6
            elif button_pressed == '7':
                self.number7
            elif button_pressed == '8':
                self.number8
            elif button_pressed == '9':
                self.number9
            elif button_pressed == 'h':
                self.volume_down
            elif button_pressed == 'l':
                self.volume_up
            elif button_pressed == 'j':
                self.channel_down
            elif button_pressed == 'k':
                self.channel_up
            else:
                print("Wrong input")

    def _send(self, command):
        try:
            self.transport.write(unhexlify(command))
        except Exception as error:
            print(error)

    def volume_down(self):   # return the binary code for VOLUME DOWN
        cmd = self.control.VOLUME_DOWN
        self._send(cmd)

    def volume_up(self):     # return the binary code for VOLUME UP
        cmd = self.control.VOLUME_UP
        self._send(cmd)

    def channel_down(self):  # return the binary code for CHANNEL DOWN
        cmd = self.control.CHANNEL_DOWN
        self._send(cmd)

    def channel_up(self):    # return the binary code for CHANNEL_UP
        cmd = self.control.CHANNEL_UP
        self._send(cmd)

    def number0(self):       # return the binary code for NUMBER 0
        cmd = self.control.NUMBER_0
        self._send(cmd)

    def number1(self):       # return the binary code for NUMBER 1
        cmd = self.control.NUMBER_1
        self._send(cmd)

    def number2(self):       # return the binary code for NUMBER 2
        cmd = self.control.NUMBER_2
        self._send(cmd)

    def number3(self):       # return the binary code for NUMBER 3
        cmd = self.control.NUMBER_3
        self._send(cmd)

    def number4(self):       # return the binary code for NUMBER 4
        cmd = self.control.NUMBER_4
        self._send(cmd)

    def number5(self):       # return the binary code for NUMBER 5
        cmd = self.control.NUMBER_5
        self._send(cmd)

    def number6(self):       # return the binary code for NUMBER 6
        cmd = self.control.NUMBER_6
        self._send(cmd)

    def number7(self):       # return the binary code for NUMBER 7
        cmd = self.control.NUMBER_7
        self._send(cmd)

    def number8(self):       # return the binary code for NUMBER 8
        cmd = self.control.NUMBER_8
        self._send(cmd)

    def number9(self):       # return the binary code for NUMBER 9
        cmd = self.control.NUMBER_9
        self._send(cmd)
