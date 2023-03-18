#!/bin/python3

import struct
from models import Key

f = open("/dev/input/event2", 'rb')
o = open("remote.log", 'a')

def code2key(code):
  #TODO implement converter
  code=str(code)
  return code

while 1:
  data = f.read(24)
  kbdEvent = struct.unpack('4IHHI', data)
  kbdCode = int(kbdEvent[4+2-1])
  kbdValue = kbdEvent[4+3-1]
  if kbdValue in (1, 2):
  # 'value' is the value the event carries. Either a relative change for
  # EV_REL, absolute new value for EV_ABS (joysticks ...), or 0 for EV_KEY for
  # release, 1 for keypress and 2 for autorepeat.
      try:
        o.write(Key(kbdCode).__str__())
      except Exception as e:
        pass
