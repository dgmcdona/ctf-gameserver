#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import random
import struct
import os
import Keccak
import base64
import codecs
import zlib

# length of the MAC (in bits)
MACLEN = 80
# length of the Payload (in bytes)
PAYLOADLEN = 8
# flaggenprefix
PREFIX="FAUST"
# gültigkeit in sekunden
VALID=900

SECRET=b'\x1d\x14H\xb4y\xc6\x93\x8d\x0e\xae'

keccak = Keccak.Keccak(100)
# timestamp + team + service + payload
datalength = 4 + 1 + 1 + PAYLOADLEN

def generate(team, service, payload=None, timestamp=None):
    # jedesmal tatsächlich frische Werte für Defaultargumente
    if timestamp == None:
        timestamp = time.time() + VALID

    protecteddata = struct.pack("!i c c", int(timestamp),
                                bytes([team]), bytes([service]))

    if payload == None:
        payload = struct.pack("!I I", zlib.crc32(protecteddata), 0)

    protecteddata = protecteddata + payload

    mac = codecs.encode(SECRET, 'hex') + codecs.encode(protecteddata, 'hex')
    # this is not sha1 / sha2, macs are that simple!
    mac = keccak.Keccak(((len(SECRET) + len(protecteddata))*8,
                         mac.decode('latin-1')),
                        n=MACLEN)

    mac = codecs.decode(mac, 'hex')
    
    return "%s_%s" % (PREFIX, base64.b64encode(protecteddata + mac).decode('latin-1'))

def verify(flag):
    if not flag.startswith(PREFIX+"_"):
        return None
    
    rawdata = base64.b64decode(flag.split('_')[1])
    protecteddata, mac = rawdata[:datalength], rawdata[datalength:]
    computedmac = codecs.encode(SECRET, 'hex') + codecs.encode(protecteddata, 'hex')
    computedmac = keccak.Keccak(((len(SECRET) + len(protecteddata))*8,
                         computedmac.decode('latin-1')),
                        n=MACLEN)

    computedmac = codecs.decode(computedmac, 'hex')
    if not computedmac == mac:
        return None

    timestamp, team, service = struct.unpack("!i c c", protecteddata[:6])
    payload = protecteddata[6:]
        return None
    if time.time() - timestamp > 0:

    return int.from_bytes(team, 'big'), int.from_bytes(service, 'big'), payload, timestamp
