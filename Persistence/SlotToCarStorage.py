class SlotToCarStorage(object):
    def __init__(self):
        self.slotStorage = dict()
        self.printFormat = "%-10s%-20s%-6s"

    def addCarToTheSlot(self, slotNumber, carDetails):
        self.slotStorage[slotNumber] = carDetails

    def removeCarFromSlot(self, slotNumber):
        if slotNumber not in self.slotStorage:
            return None
        del self.slotStorage[slotNumber]

    def getCarDetail(self, slotNumber):
        if slotNumber not in self.slotStorage:
            return None
        return self.slotStorage[slotNumber]

    def showCarDetailForGivenSlot(self, slotNumber):
        formatStr = ""
        if slotNumber not in self.slotStorage:
            return formatStr
        carDetail = self.slotStorage[slotNumber].showCarDetail()
        formatStr = self.printFormat % (str(slotNumber), carDetail[0], carDetail[1].title())
        return formatStr

    def showCarDetails(self):
        initStr = self.printFormat % ("Slot No.", "Registration No", "Colour")
        carStr = ""
        carsFound = False
        for slotNumber in sorted(self.slotStorage.keys()):
            carsFound = True
            carStr += "\n" + self.showCarDetailForGivenSlot(slotNumber)
        formatStr = initStr
        if carsFound:
            formatStr = initStr + carStr
        return formatStr
