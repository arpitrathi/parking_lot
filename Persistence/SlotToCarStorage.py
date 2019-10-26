class SlotToCarStorage(object):
    def __init__(self):
        self.slotStorage = dict()
        self.printFormat = r"%-12s%-19s"

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
        rowFormat = self.printFormat + "%-" + str(len(carDetail[1])) + "s"
        formatStr = rowFormat % (str(slotNumber), carDetail[0], carDetail[1].title())
        return formatStr

    def showCarDetails(self):
        colorLen = len("Colour")
        headerFormat = self.printFormat + "%-"+str(colorLen)+"s"
        initStr = headerFormat % ("Slot No.", "Registration No", "Colour")
        carStr = ""
        carsFound = False
        for slotNumber in sorted(self.slotStorage.keys()):
            carsFound = True
            carStr += "\n" + self.showCarDetailForGivenSlot(slotNumber)
        formatStr = "No cars present in the parking lot"
        if carsFound:
            formatStr = initStr + carStr

        return formatStr
