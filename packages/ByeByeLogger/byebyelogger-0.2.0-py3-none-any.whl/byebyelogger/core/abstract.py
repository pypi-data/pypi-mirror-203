from abc import ABC, abstractmethod

class AbstractLoggingRepository(ABC):
    
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def log(self):
        pass

class NotPrivatAttr(object):
    def __init__(self):
        for name in dir(self):
            if not name.startswith('_'):
                value = getattr(self, name)
                setattr(self, name, value)
