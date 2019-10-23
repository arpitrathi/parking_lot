"""Helper module"""

import string
import random


class IdGenerator(object):
    """
    Generates unique global ids in the system
    """
    generatedIds = set()

    @staticmethod
    def getStringId():
        """
        :return: str
        Returns a string id after processing all the letters and digits.
        """
        randomString = ''.join([random.choice(string.ascii_letters
                                              + string.digits) for _ in range(10)])
        return randomString

    @classmethod
    def generateUniqueId(cls):
        """

        :return: Unique id across the system.
        This method first fetch a id from getStringId and if it gets a unique id
        which has not been generated previously, it will return this id, otherwise
        keep regenerating a new id until we get a unique one.

        Considering our system will work with low scale of cars using the
        parking facility, this will be work fine.
        """
        randomString = cls.getStringId()
        while randomString in cls.generatedIds:
            randomString = cls.getStringId()
        cls.generatedIds.add(randomString)
        return randomString
