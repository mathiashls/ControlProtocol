from __future__ import print_function
import sys
sys.path.append("../")
from the_controller import ControlProtocol  # noqa
from twisted.internet import reactor  # noqa


class RemoteControlApp(ControlProtocol):

    def __init__(self, model, host, port):
        ControlProtocol.__init__(self, model, host, port)
        self.app_dict = {
            'j': 'channel_down',
            'k': 'channel_up',
            'h': 'volume_down',
            'l': 'volume_up',
        }

    def input_parser(self, keyboard_input):
        list_of_cmds = []
        for letter in keyboard_input:
            list_of_cmds.append(letter)
        return list_of_cmds

    def protocol_loop(self):
        while True:
            keyboard_input = None
            print("Insert your command:")
            keyboard_input = raw_input()
            cmd_list = self.input_parser(keyboard_input)
            print("Your commands:")
            print(cmd_list)
            while cmd_list:
                cmd_to_send = cmd_list.pop(0)
                if cmd_to_send in self.app_dict:
                    print("Sending %s to the dispatcher..." % cmd_to_send)
                    self.protocol_dispatcher(self.app_dict[cmd_to_send])
                else:
                    print("Sending %s to the dispatcher..." % cmd_to_send)
                    self.protocol_dispatcher(cmd_to_send)


def main():
    host = "172.16.16.161"
    port = 7001
    model = "cr2fp"
    reactor.listenUDP(0, RemoteControlApp(model, host, port))
    # reactor.listenUDP(0, ControlProtocol('skyhdtv'))
    reactor.run()


if __name__ == "__main__":
    main()
