#!/usr/bin/env python2

# Python Network programming Cookbook - Chapter - 1
# This program is optimized for Python2.7. It may run on any
# other Python version with/without modification.

import socket

def test_socket_timeout():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "Default socket timeout: %s" % s.gettimeout()
    s.settimeout(100)
    print "Current socket timeout: %s" % s.gettimeout()

if __name__ == '__main__':
    test_socket_timeout()
