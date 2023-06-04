from attack_interface import AttackInterface
class Attack(AttackInterface):
    __ip = None
    __port = None
    
    def __init__(self, ip='127.0.0.1', port=80):
        self.__ip = ip
        self.__port = port

    def run(self):
        pass
