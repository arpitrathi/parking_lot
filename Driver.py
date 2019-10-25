import sys
import traceback
from CommandExecutor import CommandExecutor


class Driver(object):
    def __init__(self):
        self.commandExecutor = CommandExecutor()

    def processFile(self, fileName):
        #print(self)
        print(fileName)
        pass

    def processCommandLineArguments(self):
        while True:
            try:
                commandStr = raw_input()
                self.commandExecutor.executeCommand(commandStr)
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
