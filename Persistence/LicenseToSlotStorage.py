class LicenseStorage(object):
    def __init__(self):
        self.licenseSlotMap = dict()

    def addLicenseToStorage(self, licenseNumber, slotNumber):
        self.licenseSlotMap[licenseNumber] = slotNumber

    def getSlotNumberForLicenseFromStorage(self, licenseNumber):
        value = self.licenseSlotMap.get(licenseNumber)
        return value if value else 0

    def removeLicenseFromStorage(self, licenseNumber):
        if licenseNumber not in self.licenseSlotMap:
            return 0
        del self.licenseSlotMap[licenseNumber]

