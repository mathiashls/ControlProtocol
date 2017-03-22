from __future__ import print_function
import sys
sys.path.append("../")
from the_controller import ControlProtocol
from twisted.internet import reactor


def main():
    reactor.listenUDP(0, ControlProtocol('cr2fp'))
    # reactor.listenUDP(0, ControlProtocol('skyhdtv'))
    reactor.run()


if __name__ == "__main__":
    main()
