"""
It involves dealing with storage of license plate to car number along with it's
removal and getting all the cars for a particular color.
"""
from collections import defaultdict
from collections import OrderedDict


class ColorStorage(object):
    """
    Storage module to store mapping of car color with all the corresponding license plates.
    """
    def __init__(self):
        self.colorToLicenseStorage = defaultdict(OrderedDict)

    def addLicenseToColor(self, color, licenseNumber):
        """

        :param color: str
        :param licenseNumber: str
        :return: None

         Add license plate to the corresponding color. If the color
        don't exist in the map, create a set of the license
        plate mapped to the color, otherwise if color
        already exists in the map, update the license plate to the map
        """

        colorToSmall = color.lower()
        if colorToSmall not in self.colorToLicenseStorage:
            self.colorToLicenseStorage[colorToSmall] = [licenseNumber]
        else:
            self.colorToLicenseStorage[colorToSmall].append(licenseNumber)

    def removeLicenseFromColor(self, color, licenseNumber):
        """

        :param color: str
        :param licenseNumber: str
        :return: Boolean

        Initially check for the color combination to be present in the storage.
        If it is not present, return False, otherwise check for the license
        number in the corresponding set. If it is not present, return False.
        Otherwise, remove the license plate from the set of the colors.
        """

        colorToSmall = color.lower()
        if colorToSmall not in self.colorToLicenseStorage and \
                licenseNumber not in \
                self.colorToLicenseStorage[colorToSmall]:
            return False
        self.colorToLicenseStorage[colorToSmall].remove(licenseNumber)
        if not self.colorToLicenseStorage[colorToSmall]:
            del self.colorToLicenseStorage[colorToSmall]
        return True

    def getListOfAllCars(self, color):
        """

        :param color: str
        :return: List

        Check whether the given color is present in the storage. If not present,
        simply return an empty list. Otherwise return a list of all the car
        license plates having that color.

        """
        colorToSmall = color.lower()
        ans = []
        if colorToSmall in self.colorToLicenseStorage:
            ans = self.colorToLicenseStorage[colorToSmall]
        return ans

    def getAllCars(self, color):
        ansList = self.getListOfAllCars(color)
        formatStr = ', '.join(ansList)
        return formatStr
