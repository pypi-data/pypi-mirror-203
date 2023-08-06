"""Firepup650's fkeycapture module"""
import termios, fcntl, sys
global fd,flags_save,attrs_save
fd = sys.stdin.fileno()
flags_save = fcntl.fcntl(fd, fcntl.F_GETFL)
attrs_save = termios.tcgetattr(fd)
def __getp1():
    """Internal Method - Modify terminal settings"""
    import termios, fcntl, sys, os
    fd = sys.stdin.fileno()
    # save old state
    flags_save = fcntl.fcntl(fd, fcntl.F_GETFL)
    attrs_save = termios.tcgetattr(fd)
    # make raw - the way to do this comes from the termios(3) man page.
    attrs = list(attrs_save) # copy the stored version to update
    # iflag
    attrs[0] &= ~(termios.IGNBRK | termios.BRKINT | termios.PARMRK
                  | termios.ISTRIP | termios.INLCR | termios. IGNCR
                  | termios.ICRNL | termios.IXON )
    # oflag
    attrs[1] &= ~termios.OPOST
    # cflag
    attrs[2] &= ~(termios.CSIZE | termios. PARENB)
    attrs[2] |= termios.CS8
    # lflag
    attrs[3] &= ~(termios.ECHONL | termios.ECHO | termios.ICANON
                  | termios.ISIG | termios.IEXTEN)
    termios.tcsetattr(fd, termios.TCSANOW, attrs)
    # turn off non-blocking
    fcntl.fcntl(fd, fcntl.F_SETFL, flags_save & ~os.O_NONBLOCK)
def __getp2():
    """Internal Method - Reset terminal settings"""
    termios.tcsetattr(fd, termios.TCSAFLUSH, attrs_save)
    fcntl.fcntl(fd, fcntl.F_SETFL, flags_save)
def get(keycount: int = 1, bytes: bool = False) -> str or bytes:
  """# Function: get

# Inputs:
  keycount: int - Number of keys, defualts to 1
  bytes: bool   - Wether or not to return the key(s) as bytes, defaults to False

# Returns:
  str or bytes

# Raises:
  None"""
  __getp1()
  key = sys.stdin.read(keycount)
  __getp2()
  if bytes:
    return key.encode()
  else:
    return key
def getnum(keycount: int = 1, ints: bool = False) -> str or int:
  """# Function: getnum

# Inputs:
  keycount: int - Number of keys, defualts to 1
  ints: bool    - Wether to return the keys as ints, defaults to False

# Returns:
  str or int

# Raises:
  None"""
  internalcounter=0
  keys = []
  while internalcounter != keycount:
    key = get()
    if key in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      keys.append(key)
      internalcounter += 1
  key = "".join(keys)
  if not ints:
    return key
  else:
    return int(key)
def getchars(keycount: int = 1, chars: list = ["1", "2"], bytes: bool = False) -> str:
  """# Function: getchars

# Inputs:
  keycount: int - Number of keys, defualts to 1
  chars: list   - List of allowed keys, defaults to ["1", "2"]
  bytes: bool   - Wether or not to return the key(s) as bytes, defaults to False

# Returns:
  str

# Raises:
  None"""
  internalcounter=0
  keys = []
  while internalcounter != keycount:
    key = get()
    for char in chars:
      if key == char:
        keys.append(key)
        internalcounter += 1
  key = "".join(keys)
  if not bytes:
    return key
  else:
    return key.encode()
# def help():
#   """# Function: help

# # Inputs:
#   None

# # Returns:
#   None

# # Raises:
#   None"""
#   print("FKEYCAPTURE HELP\nThis is a simple and easy to use package that allows you to capture individual keystrokes from the user.\nFORMS:\n1. (Default) Recive key as a string\n2. Recive key as bytes\nHOW TO USE:\n1. from fkeycapture import get, getnum, getchars\n2. Use get like this: get([number of keys to capture],[if you want bytes output, make this 'True'])\n3. Use getnum like this: getnum([number of numbers to capture])\n4. Use getchars like this: get([number of keys to capture],[list of chars to capture])")