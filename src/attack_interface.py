from abc import ABC, abstractmethod

class AttackInterface(ABC):
    __ip = None
    __port = None

    @abstractmethod
    def run(self):
        pass