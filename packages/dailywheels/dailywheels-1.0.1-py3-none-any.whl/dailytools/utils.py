# -*- coding: utf-8 -*
import socket
from .__exceptions import *


def get_host_ip():
    try:
        # Create a new socket using the given address family,
        # socket type and protocol number.
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Connect to a remote socket at address.
        # (The format of address depends on the address family.)
        address = ("8.8.8.8", 80)
        s.connect(address)

        # Return the socket’s own address.
        # This is useful to find out the port number of an IPv4/v6 socket, for instance.
        # (The format of the address returned depends on the address family.)
        sockname = s.getsockname()
        # print(sockname)

        ip = sockname[0]
    except Exception as e:
        ip = None
        raise NetConfigError(e.__str__())

    finally:
        s.close()

    return ip