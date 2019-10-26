class SlotToCarStorage(object):
    """
    It stores car object for the given slot number.
    """
    def __init__(self):
        self.slotStorage = dict()
        self.printFormat = r"%-12s%-19s"

    def addCarToTheSlot(self, slotNumber, carDetails):
        """

        :param slotNumber: int
        :param carDetails:  Car
        :return: None

        Add the car to the given slot.
        """
        self.slotStorage[slotNumber] = carDetails

    def removeCarFromSlot(self, slotNumber):
        """

        :param slotNumber: int
        :return: None
        Remove the car from the given slot number.
        """
        del self.slotStorage[slotNumber]

    def getCarDetail(self, slotNumber):
        """

        :param slotNumber: int
        :return: Car object if present else None
        """
        if slotNumber not in self.slotStorage:
            return None
        return self.slotStorage[slotNumber]

    def showCarDetailForGivenSlot(self, slotNumber):
        """

        :param slotNumber: int
        :return: str
        It parses the car information for the car in the  given slot number in a string and
        returns this information back to the caller.
        """
        formatStr = ""
        if slotNumber not in self.slotStorage:
            return formatStr
        carDetail = self.slotStorage[slotNumber].showCarDetail()
        rowFormat = self.printFormat + "%-" + str(len(carDetail[1])) + "s"
        formatStr = rowFormat % (str(slotNumber), carDetail[0], carDetail[1].title())
        return formatStr

    def showCarDetails(self):
        """

        :return: str
        It returns a detail for all the parking slots in use. If all the
        parking slots are empty, it will return No cars present.
        """
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
