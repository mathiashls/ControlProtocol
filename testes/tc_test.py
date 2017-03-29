from __future__ import print_function
import logging
import sys
sys.path.append("../")
from the_controller import ControlProtocol  # noqa
from twisted.internet import reactor  # noqa

"""
    The RemoteControlApp class simulate a remote control using keyboard input.
    Change the host address for the one used by your HDbitT device.
"""


class RemoteControlApp(object):

    def __init__(self, remote):
        self.control = remote
        self.app_dict = {
            'j': 'channel_down',
            'k': 'channel_up',
            'h': 'volume_down',
            'l': 'volume_up',
        }

    def protocol_loop(self):
        while True:
            keyboard_input = None
            print("Insert your command:")
            keyboard_input = raw_input()
            if keyboard_input == 'j':
                self.control.channel_down()
            elif keyboard_input == 'k':
                self.control.channel_up()
            elif keyboard_input == 'h':
                self.control.volume_down()
            elif keyboard_input == 'l':
                self.control.volume_up()
            else:
                self.control.set_channel(keyboard_input)


def main():
    logging.basicConfig(filename='the_controller.log', level=logging.INFO)
    host = "172.16.16.161"
    port = 7001
    model = "cr2fp"
    remote = ControlProtocol(model, host, port)
    reactor.listenUDP(0, remote)
    app = RemoteControlApp(remote)
    reactor.callFromThread(app.protocol_loop)
    reactor.run()


if __name__ == "__main__":
    main()
