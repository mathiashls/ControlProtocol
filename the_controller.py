from binascii import unhexlify
import logging
from time import sleep
from control_models import cr2fp
from control_models import skyhdtv
from twisted.internet.protocol import DatagramProtocol


class ControlProtocol(DatagramProtocol):

    def __init__(self, model, host, port):
        """
            Remote control models that are available.
            It needs a better approach if the number of models grows.
        """
        if model == 'cr2fp':
            self.control = cr2fp.CR2FP()
        elif model == 'skyhdtv':
            self.control = skyhdtv.SKYHDTV()
        else:
            raise
        self.host = host
        self.port = port

    def startProtocol(self):
        """
            Default reactor method startProtocol, used here to create the
            socket connection and call the main protocol loop
        """
        self.transport.connect(self.host, self.port)
        logging.info("Connect with %s:%d" % (self.host, self.port))
        self.protocol_loop()

    def datagramReceived(self, data, addr):
        """Default reactor method (useless for the protocol itself)"""
        logging.info("Received %r from %s." % (data, addr))

    def connectionRefused(self):
        """Default reactor method (useless for the protocol itself)"""
        logging.error("Connection refused: no one listening.")

    def input_validation(self, keyboard_input):
        """
            input_validation method returns a list of validated parsed
            characters if all the characters are valid, or None if the
            characters are not valid. This way the user can insert a string of
            buttons and the program will work just fine.
        """
        list_of_buttons = []
        if keyboard_input in self.control.buttons:
            list_of_buttons.append(keyboard_input)
        else:
            for letter in keyboard_input:
                if letter in self.control.buttons:
                    list_of_buttons.append(letter)
                else:
                    return None
        return list_of_buttons

    def protocol_loop(self):
        """
            protocol_loop must be overwritten by the application. It must
            capture the input from the user and send it to the
            protocol_dispatcher
        """
        raise

    def protocol_dispatcher(self, keyboard_input):
        """
            Main program loop, used to read the input from the user and make
            the general method calls.
        """
        list_of_cmd = self.input_validation(keyboard_input)
        if list_of_cmd is None:
            logging.warn("Wrong input parameters: try again.")
        else:
            while list_of_cmd:
                sleep(self.control.INTERVAL)
                self._send(self.control.buttons[list_of_cmd.pop(0)])

    def _send(self, command):
        """
            _send method receive the command string, convert it to binary and
            send it to the socket.
        """
        try:
            self.transport.write(unhexlify(command))
        except Exception as error:
            logging.error(error)
