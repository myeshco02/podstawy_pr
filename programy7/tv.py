class TV:
    def __init__(self):
        self.isOn = False
        self.channelNo = 1
        self.channels = []
        self.volume = 0

    def turnOn(self):
        self.isOn = True

    def turnOff(self):
        self.isOn = False

    def setChannel(self, newChannelNo):
        self.channelNo = newChannelNo

    def showStatus(self):
        if self.isOn:
            if 1 <= self.channelNo <= len(self.channels):
                print(
                    f"TV is on, channel {self.channelNo} ({self.channels[self.channelNo - 1]}), volume {self.volume}")
            else:
                print(f"TV is on, channel {self.channelNo}, volume {self.volume}")
        else:
            print("TV is off")

    def setChannels(self, channelsList):
        self.channels = channelsList

    def showChannels(self):
        print("Channel list:")
        for i, channel in enumerate(self.channels, 1):
            print(f"{i}. {channel}")

    def volumeUp(self):
        if self.isOn and self.volume < 10:
            self.volume += 1

    def volumeDown(self):
        if self.isOn and self.volume > 0:
            self.volume -= 1
