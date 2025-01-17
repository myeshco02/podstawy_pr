from tv import TV


def main():
    myTV = TV()
    myTV.showStatus()

    myTV.turnOn()
    myTV.showStatus()
    myTV.showChannels()

    myTV.setChannels(['TVP1', 'TVP2', 'Polsat', 'TVN', 'Filmbox', 'Discovery', 'MTV'])
    myTV.showChannels()
    myTV.showStatus()

    myTV.setChannel(2)
    myTV.showStatus()

    myTV.setChannel(4)
    myTV.showStatus()

    myTV.setChannel(8)
    myTV.showStatus()

    [myTV.volumeUp() for _ in range(20)]
    myTV.showStatus()

    [myTV.volumeUp() for _ in range(20)]
    myTV.showStatus()

    myTV.turnOff()
    myTV.showStatus()


if __name__ == "__main__":
    main()