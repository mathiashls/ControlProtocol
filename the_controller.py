from binascii import unhexlify
from time import sleep
from control_models import cr2fp
from twisted.internet.protocol import DatagramProtocol


class ControlProtocol(DatagramProtocol):

    def __init__(self, model):
        if model == 'cr2fp':
            self.control = cr2fp.CR2FP()
        else:
            raise
        self.host = "192.168.1.238"
        self.port = 7001

    def startProtocol(self):
        self.transport.connect(self.host, self.port)
        print("Connect with %s:%d" % (self.host, self.port))
        self.protocol_loop()

    def datagramReceived(self, data, addr):
        print("Received %r from %s." % (data, addr))

    def connectionRefused(self):
        print("Connection refused: no one listening.")

    # 'input_validation' method parse the input from the user and
    # check if it is a valid character:
    def input_validation(self, keyboard_input):
        list_of_buttons = []
        for letter in keyboard_input:
            if letter in self.control.buttons:
                list_of_buttons.append(letter)
            else:
                return None
        return list_of_buttons

    def protocol_loop(self):
        while True:
            keyboard_input = None
            keyboard_input = raw_input()
            list_of_cmd = self.input_validation(keyboard_input)
            if list_of_cmd is None:
                print("Wrong input parameters: try again.")
            else:
                while list_of_cmd:
                    sleep(self.control.message_delay)
                    self._send(self.control.buttons[list_of_cmd.pop(0)])

    # '_send' method receive the command string, convert it to binary and
    # send it to the IR device via UDP connection
    def _send(self, command):
        try:
            self.transport.write(unhexlify(command))
        except Exception as error:
            print(error)
