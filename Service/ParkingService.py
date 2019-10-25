from Model.Car import Car
from Persistence.ColorToLicenseStorage import ColorStorage
from Persistence.LicenseToSlotStorage import LicenseStorage
from Persistence.SlotToCarStorage import SlotToCarStorage
import heapq


class ParkingService(object):
    def __init__(self):
        self.slotStorage = SlotToCarStorage()
        self.noOfParkingSlots = 0
        self.licenseToSlotStorage = LicenseStorage()
        self.colorToLicenseStorage = ColorStorage()
        self.minHeap = []

    def createParkingLot(self, n):
        self.noOfParkingSlots = n
        self.minHeap = range(1, n+1)
        heapq.heapify(self.minHeap)
        return True

    def parkVehicle(self, licenseNumber, carColor):
        if len(self.minHeap) == 0:
            return 0
        parkingSlot = heapq.heappop(self.minHeap)
        carDetails = Car(licenseNumber, carColor)
        self.colorToLicenseStorage.addLicenseToColor(carColor, licenseNumber)
        self.licenseToSlotStorage.addLicenseToStorage(licenseNumber, parkingSlot)
        self.slotStorage.addCarToTheSlot(parkingSlot, carDetails)
        return parkingSlot

    def leaveParkingSlot(self, slotNumber):
        if slotNumber<1 or slotNumber > self.noOfParkingSlots:
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
        return self.slotStorage.showCarDetails()

    def getLicenseNumbersOfCarForGivenColor(self, carColor):
        return self.colorToLicenseStorage.getAllCars(carColor)

    def getSlotNumberForGivenLicense(self, licenseNumber):
        return self.licenseToSlotStorage.getSlotNumberForLicenseFromStorage(licenseNumber)

    def getSlotNumbersOfCarForGivenColor(self, carColor):
        listOfCars = self.colorToLicenseStorage.getListOfAllCars(carColor)
        slotNumbers = []
        for carLicense in listOfCars:
            slotNumbers.append(str(self.getSlotNumberForGivenLicense(carLicense)))
        formatStr = ', '.join(slotNumbers)
        return formatStr




