from abc import ABCMeta, abstractmethod

# use ABCMeta compatible with Python 2 and Python 3
ABC = ABCMeta('ABC', (object,), {'__slots__': ()})


class Search(ABC):
    """ Abstract product """

    @abstractmethod
    def __init__(self, source):
        self.source = source

    @abstractmethod
    def matching(self):
        # example of abstract
        pass


