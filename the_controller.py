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
        """
            The HDbitT device works with a default IP (192.168.1.238)
            The default port for the IR stream is 7001
        """
        self.host = host
        self.port = port

    def startProtocol(self):
        """
            Default reactor method startProtocol, used here to create the
            socket connection and call the main protocol loop
        """
        self.transport.connect(self.host, self.port)
        logging.info("Connect with %s:%d" % (self.host, self.port))

    def datagramReceived(self, data, addr):
        """Default reactor method (useless for the protocol itself)"""
        logging.info("Received %r from %s." % (data, addr))

    def connectionRefused(self):
        """Default reactor method (useless for the protocol itself)"""
        logging.error("Connection refused: no one listening.")

    def _channel_is_valid(self, user_input):
        """
            Return True if all the characters inside user_input are valid, and
            False if not.
        """
        try:
            int(user_input)
            return True
        except Exception as error:
            logging.error(error)
        return False

    def _send(self, command):
        """
            _send method receive the command string, convert it to binary and
            send it to the socket.
        """
        try:
            self.transport.write(unhexlify(command))
            logging.info("Signal successfully sent.")
        except Exception as error:
            logging.error(error)

    def volume_up(self):
        self._send(self.control.buttons['volume_up'])

    def volume_down(self):
        self._send(self.control.buttons['volume_down'])

    def channel_up(self):
        self._send(self.control.buttons['channel_up'])

    def channel_down(self):
        self._send(self.control.buttons['channel_down'])

    def set_channel(self, channel):
        if self._channel_is_valid(channel):
            for letter in str(channel):
                self._send(self.control.buttons[letter])
                sleep(self.control.INTERVAL)
                logging.info("Sending %s signal..." % letter)
        else:
            logging.info("Wrong input parameters: try again.")
