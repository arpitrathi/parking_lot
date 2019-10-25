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


    @classmethod
    def run(cls):
        if len(sys.argv) > 1:
            fileName = sys.argv[1]
            cls.processFile(fileName)
        else:
            cls.processCommandLineArguments()


def main():
    Driver.run()


if __name__ == '__main__':
    main()
