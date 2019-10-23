class SlotToCarStorage(object):
    def __init__(self):
        self.slotStorage = dict()

    def addCarToTheSlot(self, slotNumber, carDetails):
        self.slotStorage[slotNumber] = carDetails

    def removeCarFromSlot(self, slotNumber):
        if slotNumber not in self.slotStorage:
            return None
        carDetails = self.slotStorage[slotNumber]
        return carDetails

    def showCarDetailForGivenSlot(self, slotNumber):
        formatStr = ""
        if slotNumber not in self.slotStorage:
            return formatStr
        carDetail = self.slotStorage[slotNumber]
        formatStr += "%d\t" % slotNumber
        formatStr += carDetail.showCarDetail()
        return formatStr

    def showCarDetails(self):
        initStr = "Slot No.\tRegistration No\tColour\n"
        print initStr
        for slotNumber in sorted(self.slotStorage.keys()):
            carStr = self.showCarDetailForGivenSlot(slotNumber)
            print carStr
