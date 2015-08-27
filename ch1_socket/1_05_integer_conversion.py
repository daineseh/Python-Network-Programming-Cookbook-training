#!/usr/bin/env python2
# Python Network Programming Cookbook -- Chapter 1
# This program is optimized for Python 2.7.
# It may run on any other version with/without modifications.

import socket

def convert_integer():
    data = 1234
    # 32-bit
    print "Original: %s => Long host by order: %s, Network byte order: %s"\
            % (data, socket.ntohl(data), socket.htonl(data))
    # 16-bit
    print "OriginalL %s => Short host by order: %s, Network byte order: %s"\
            % (data, socket.ntohs(data), socket.htons(data))

if __name__ == '__main__':
    convert_integer()
