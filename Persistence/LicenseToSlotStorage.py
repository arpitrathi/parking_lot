"""
It involves dealing with addition and removal of license plate to slot
number mapping.
"""
import traceback

class LicenseStorage(object):
    """
    This module maps a licence plate to a parking slot and reverses it.
    """
    def __init__(self):
        self.licenseSlotMap = dict()

    def addLicenseToStorage(self, licenseNumber, slotNumber):
        """

        :param licenseNumber:  str
        :param slotNumber: int
        :return: Boolean

        This method tries to add a slot number to a corresponding license number.
        Returns true on success otherwise returns False
        """
        try:
            self.licenseSlotMap[licenseNumber] = slotNumber
        except Exception:
            traceback.print_exc()
            return False
        return True

    def getSlotNumberForLicenseFromStorage(self, licenseNumber):
        """

        :param licenseNumber:  str
        :return: int

        This method tries to find the given license number in the map and
        returns the slot number if available, otherwise returns 0
        """
        value = self.licenseSlotMap.get(licenseNumber)
        return value if value else 0

    def removeLicenseFromStorage(self, licenseNumber):
        """

        :param licenseNumber: str
        :return: Bool

        This method tries to delete a license number mapping from the
        storage. Returns True on success, otherwise returns False.
        """
        if licenseNumber not in self.licenseSlotMap:
            return False
        del self.licenseSlotMap[licenseNumber]
        return True
