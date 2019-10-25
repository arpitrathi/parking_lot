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
        self.minHeap = [range(1, n+1)]
        heapq.heapify(self.minHeap)
        return True

    def parkVehicle(self, licenseNumber, color):
        if len(self.minHeap) == 0:
            return 0
        parkingSlot = heapq.heappop(self.minHeap)
        carDetails = Car(licenseNumber, color)
        self.colorToLicenseStorage.addLicenseToColor(color, licenseNumber)
        self.licenseToSlotStorage.addLicenseToStorage(licenseNumber, parkingSlot)
        self.slotStorage.addCarToTheSlot(parkingSlot, carDetails)
        return parkingSlot

    def leaveParkingSlot(self, slotNumber):
        if slotNumber<1 or slotNumber > self.noOfParkingSlots:
            return False
        carDetails = self.slotStorage.getCarDetail(slotNumber)
        self.slotStorage.removeCarFromSlot(slotNumber)
        assert self.licenseToSlotStorage.removeLicenseFromStorage( \
                carDetails.licenseNumber), "License number not found in map"
        assert self.colorToLicenseStorage.removeLicenseFromColor(\
                carDetails.color, carDetails.licenseNumber), "License number not found in color set"
        return True

    def statusOfParkingSlot(self):
        return self.slotStorage.showCarDetails()

    def getLicenseNumbersOfCarForGivenColor(self, color):
        return self.colorToLicenseStorage.getAllCars(color)

    def getSlotNumberForGivenLicense(self, licenseNumber):
        return self.licenseToSlotStorage.getSlotNumberForLicenseFromStorage(licenseNumber)

    def getSlotNumbersOfCarForGivenColor(self, color):
        listOfCars = self.colorToLicenseStorage.getListOfAllCars(color)
        slotNumbers = []
        for carLicense in listOfCars:
            slotNumbers.append(str(self.getSlotNumberForGivenLicense(carLicense)))
        formatStr = ', '.join(slotNumbers)
        return formatStr




