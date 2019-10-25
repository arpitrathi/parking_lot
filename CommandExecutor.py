from Service.ParkingService import ParkingService
import traceback
import sys


class CommandExecutor(object):
    def __init__(self):
        self.parkingService = ParkingService()

    def executeCommand(self, commandStr):
        commands = commandStr.split()
        if commands[0] == "create_parking_lot":
            if self.parkingService.createParkingLot(int(commands[1])):
                print("Created a parking lot with %s slots" % commands[1])
        elif commands[0] == "park":
            slotNumber = self.parkingService.parkVehicle(commands[1], commands[2])
            if slotNumber == 0:
                print("Sorry, parking lot is full")
            else:
                print("Allocated slot number: %d" % slotNumber)
        elif commands[0] == "leave":
            try:
                if self.parkingService.leaveParkingSlot(int(commands[1])):
                    print("Slot number %s is free" % commands[1])
                else:
                    print("Slot number %s is already free" % commands[1])
            except AssertionError:
                traceback.print_exc()
        elif commands[0] == "status":
            formatStr = self.parkingService.statusOfParkingSlot()
            print(formatStr)
        elif commands[0] == "registration_numbers_for_cars_with_colour":
            ansStr = self.parkingService.getLicenseNumbersOfCarForGivenColor(commands[1])
            if len(ansStr) == 0:
                print("Not found")
            else:
                print(ansStr)
        elif commands[0] == "slot_numbers_for_cars_with_colour":
            ansStr = self.parkingService.getSlotNumbersOfCarForGivenColor(commands[1])
            if len(ansStr) == 0:
                print("Not found")
            else:
                print(ansStr)
        elif commands[0] == "slot_number_for_registration_number":
            ans = self.parkingService.getSlotNumberForGivenLicense(commands[1])
            if ans == 0:
                print("Not found")
            else:
                print(ans)
        elif commands[0] == "exit":
            sys.exit(0)

