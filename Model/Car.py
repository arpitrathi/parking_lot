"""
Model for a car which will store initially license number and car color.
This model can be extended later if we need to add more attributes specific
to car.
"""
from Common.Library import IdGenerator


class Car(object):
    """
    Creates a car object
    """

    def __init__(self, licenseNumber, carColor):
        """
        :param licenseNumber: str
        :param carColor: str
        """
        self.id = IdGenerator.generateUniqueId()
        self.licenseNumber = licenseNumber
        self.carColor = carColor.lower()

    def getCarLicenseNumber(self):
        """

        :return: str
        Returns the car license number
        """
        return self.licenseNumber

    def getCarModel(self):
        """

        :return: str
        Returns the car model
        """
        return self.carColor

    def showCarDetail(self):
        carTuple = (self.licenseNumber, self.carColor)
        return carTuple
