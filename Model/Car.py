"""
Model for a car which will store initially license number and car color.
This model can be extended later if we need to add more attributes specific
to car.
"""
from Model.Library import IdGenerator


class Car(object):
    """
    Creates a car object
    """

    def __init__(self, licenseNumber, carModel):
        """
        :param licenseNumber: str
        :param carModel: str
        """
        self.id = IdGenerator.generateUniqueId()
        self.licenseNumber = licenseNumber
        self.carModel = carModel.lower()

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
        return self.carModel

    def showCarDetail(self):
        formatStr = "%s\t%s\n" % (self.licenseNumber, self.carModel)
        return formatStr
