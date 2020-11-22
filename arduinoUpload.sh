cd led
arduino-cli compile --fqbn arduino:avr:uno led
arduino-cli upload -p /dev/cu.usbmodem146101 --fqbn arduino:avr:uno led