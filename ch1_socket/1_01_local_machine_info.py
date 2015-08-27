#!/usr/bin/env python2
# Python Network Programming Cookbook -- Chapter -1
# This program is optimized for Python2.7. It may run on any
# other Python version with/without modifications.

import socket

def print_machine_info():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print "Host name: %s" % host_name
    print "IP address: %s" % ip_address

if __name__ == '__main__':
    print_machine_info()
