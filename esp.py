import struct
import socket
from pynput.keyboard import Key, Listener

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = ("192.168.138.182", 8888)
def on_press(key):
    if key == Key.up:
        data = struct.pack("B", 1)
    elif key == Key.down:
        data = struct.pack("B", 0)
    else:
        data = struct.pack("B", 2)
    
    client.sendto(data, addr)

def on_release(key):
    data = struct.pack("B", 2)
    client.sendto(data, addr)

with Listener(on_press=on_press, on_release=on_release) as l:
    l.join()
