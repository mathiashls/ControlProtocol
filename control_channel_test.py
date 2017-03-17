from __future__ import print_function
import time
from ControlProtocol import ControlProtocol

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class Helloer(DatagramProtocol):
    def startProtocol(self):
        host = "192.168.1.238"
        port = 7001
        model_type = 'cr2fp'
        try:
            controller = ControlProtocol(model_type)
        except Exception as error:
            controller = None
            print("Could not create the class:")
            print("\t", error)

        if(controller):
            self.transport.connect(host, port)
            self.transport.write(controller.channel_up())
            time.sleep(4)
            self.transport.write(controller.channel_up())
            time.sleep(4)
            self.transport.write(controller.channel_down())
            time.sleep(4)
            self.transport.write(controller.channel_down())
        else:
            print("Can't do any task: control unknown.")

    def datagramReceived(self, data, addr):
        print("received %r from %s" % (data, addr))

    # Possibly invoked if there is no server listening on the
    # address to which we are sending.
    def connectionRefused(self):
        print("No one listening")


# 0 means any port, we don't care in this case
reactor.listenUDP(0, Helloer())
reactor.run()
