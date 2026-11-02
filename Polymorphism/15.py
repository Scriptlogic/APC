class SmartDevice:
    def turn_on(self):
        print("Device is ON")

    def turn_off(self):
        print("Device is OFF")


class Light(SmartDevice):
    def turn_on(self):
        print("Light is ON")

    def turn_off(self):
        print("Light is OFF")


class Fan(SmartDevice):
    def turn_on(self):
        print("Fan is ON")

    def turn_off(self):
        print("Fan is OFF")


class AC(SmartDevice):
    def turn_on(self):
        print("AC is ON")

    def turn_off(self):
        print("AC is OFF")


class TV(SmartDevice):
    def turn_on(self):
        print("TV is ON")

    def turn_off(self):
        print("TV is OFF")


devices = [Light(), Fan(), AC(), TV()]

for device in devices:
    device.turn_on()
    device.turn_off()