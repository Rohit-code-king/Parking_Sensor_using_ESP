# Parking_Sensor_using_ESP

This project (esp.py) allows remote control of an ESP (or any compatible device) by sending UDP packets in response to keyboard input.

Features
Sends simple UDP packets when keys are pressed:

Up arrow sends 1

Down arrow sends 0

All other keys send 2

Uses pynput to listen for key events

Sends data to a configured IP address and port
