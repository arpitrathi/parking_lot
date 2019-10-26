from Model.Car import Car
from Persistence.ColorToLicenseStorage import ColorStorage
from Persistence.LicenseToSlotStorage import LicenseStorage
from Persistence.SlotToCarStorage import SlotToCarStorage
import heapq


class ParkingService(object):
    """
    Involved in performing the business logic of the application.
    """
    def __init__(self):
        self.slotStorage = SlotToCarStorage()
        self.noOfParkingSlots = 0
        self.licenseToSlotStorage = LicenseStorage()
        self.colorToLicenseStorage = ColorStorage()
        self.minHeap = []

    def createParkingLot(self, n):
        """

        :param n: int
        :return: bool
        Creates a parking lot of the given size. Returns true on success.
        Returns false on failure to create the parking lot.
        """
        try:
            self.noOfParkingSlots = n
            self.minHeap = range(1, n+1)
            heapq.heapify(self.minHeap)
        except Exception:
            return False
        return True

    def parkVehicle(self, licenseNumber, carColor):
        """

        :param licenseNumber: str
        :param carColor: str
        :return: int
        It involves allotment of the lowest slot number to the vehicle and returns
        that slot number. If all the slots are full, return 0.
        """
        if len(self.minHeap) == 0:
            return 0
        parkingSlot = heapq.heappop(self.minHeap)
        carDetails = Car(licenseNumber, carColor)
        self.colorToLicenseStorage.addLicenseToColor(carColor, licenseNumber)
        self.licenseToSlotStorage.addLicenseToStorage(licenseNumber, parkingSlot)
        self.slotStorage.addCarToTheSlot(parkingSlot, carDetails)
        return parkingSlot

    def leaveParkingSlot(self, slotNumber):
        """

        :param slotNumber: int
        :return: bool
        It tries to remove the car from the given slot number.
        returns True on success, otherwise returns False.
        """
        if slotNumber < 1 or slotNumber > self.noOfParkingSlots:
            return False
        carDetails = self.slotStorage.getCarDetail(slotNumber)
        if carDetails is None:
            return False
        self.slotStorage.removeCarFromSlot(slotNumber)
        self.licenseToSlotStorage.removeLicenseFromStorage( \
                carDetails.licenseNumber)
        self.colorToLicenseStorage.removeLicenseFromColor(\
                carDetails.carColor, carDetails.licenseNumber)
        heapq.heappush(self.minHeap, slotNumber)
        return True

    def statusOfParkingSlot(self):
        """

        :return: str
        It fetches the details of all the parking slots and returns them
        back to the user.
        """
        return self.slotStorage.showCarDetails()

    def getLicenseNumbersOfCarForGivenColor(self, carColor):
        """

        :param carColor: str
        :return: str
        It tries to fetch the list of registration numbers of the cars which have this color
        and returns their details. Otherwise returns vacant.
        """
        return self.colorToLicenseStorage.getAllCars(carColor)

    def getSlotNumberForGivenLicense(self, licenseNumber):
        """

        :param licenseNumber: str
        :return: int
        It tries to fetch the slot number for the given license number and
        returns the slot number, otherwise returns 0
        """
        return self.licenseToSlotStorage.getSlotNumberForLicenseFromStorage(licenseNumber)

    def getSlotNumbersOfCarForGivenColor(self, carColor):
        """

        :param carColor: str
        :return: str
         returns the formatstr of slots occupied by the car having this color.
        """
        listOfCars = self.colorToLicenseStorage.getListOfAllCars(carColor)
        slotNumbers = []
        for carLicense in listOfCars:
            slotNumbers.append(str(self.getSlotNumberForGivenLicense(carLicense)))
        formatStr = ', '.join(slotNumbers)
        return formatStr




