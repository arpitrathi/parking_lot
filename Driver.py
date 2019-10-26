import sys
import traceback
from CommandExecutor import CommandExecutor


class Driver(object):
    def __init__(self):
        self.commandExecutor = CommandExecutor()

    def processFile(self, fileName):
        fileContents = open(fileName, "r")
        for commandStr in fileContents.readlines():
            try:
                self.commandExecutor.executeCommand(commandStr)
            except AssertionError:
                print("Please input valid commands")
            except Exception:
                traceback.print_exc()

    def processCommandLineArguments(self):
        while True:
            try:
                commandStr = raw_input()
                self.commandExecutor.executeCommand(commandStr)
            except AssertionError:
                print("Please input valid commands")
            except Exception:
                traceback.print_exc()

    def run(self):
        if len(sys.argv) > 1:
            fileName = sys.argv[1]
            self.processFile(fileName)
        else:
            self.processCommandLineArguments()


def main():
    driver = Driver()
    driver.run()


if __name__ == '__main__':
    main()
