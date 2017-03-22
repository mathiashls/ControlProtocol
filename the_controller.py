from binascii import unhexlify
from time import sleep
from control_models import cr2fp
from control_models import skyhdtv
from twisted.internet.protocol import DatagramProtocol


class ControlProtocol(DatagramProtocol):

    # remote control models available
    # it needs a better approach if the number of models grows
    def __init__(self, model):
        if model == 'cr2fp':
            self.control = cr2fp.CR2FP()
        elif model == 'skyhdtv':
            self.control = skyhdtv.SKYHDTV()
        else:
            raise
        # the HDbitT device works with a default IP (192.168.1.238)
        # the default port for the IR stream is 7001
        self.host = "192.168.1.238"
        self.port = 7001

    # default reactor method startProtocol, used here to create the 
    # socket connection and call the main protocol loop
    def startProtocol(self):
        self.transport.connect(self.host, self.port)
        print("Connect with %s:%d" % (self.host, self.port))
        self.protocol_loop()

    # default reactor method (useless for the protocol itself)
    def datagramReceived(self, data, addr):
        print("Received %r from %s." % (data, addr))

    # default reactor method (useless for the protocol itself)
    def connectionRefused(self):
        print("Connection refused: no one listening.")

    # 'input_validation' method returns a list of validated parsed characters
    # or None if the chars are not valid. This way the user can insert a string
    # of buttons and the program will work just fine
    def input_validation(self, keyboard_input):
        list_of_buttons = []
        for letter in keyboard_input:
            if letter in self.control.buttons:
                list_of_buttons.append(letter)
            else:
                return None
        return list_of_buttons

    # main program loop, used to read the input from the user and make the
    # general decisions
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
    # send it to the socket
    def _send(self, command):
        try:
            self.transport.write(unhexlify(command))
        except Exception as error:
            print(error)
