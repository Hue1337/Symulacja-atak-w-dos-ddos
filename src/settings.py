from dos import DoS
from ddos import DDoS
from status import StatusClient
from after_statistics import AfterStats

class Settings:
    __id = None

    def __init__(self):
        self.__id = 1

    def get_attack_id(self, attack_id) -> int:
        return self.__id

    def set_id(self, attack_id) -> None:
        self.__id = attack_id

    def run_stats_configuration(self):
        ip = "127.0.0.1"
        port = 80
        return StatusClient(ip, port, self.__id)

    def run_default_attack_configuration(self):
        ''' Running default attack configuration.'''
        ip='127.0.0.1'
        port = 80
        payload="This is just a plain text for DoS."
        amount_of_requests = 0
        amount_of_requests = 2700

        return DoS(ip, port, amount_of_requests, payload), self.__id

    def run_stats_generator_based_on_saved_data(self):
        ''' Running statistics generator based on saved data.'''
        print("Choose option:\n\t[1] Generate DoS statistics.\n\t[2] Generate DDoS statistics.\n\t[3] Generate DoS & DDoS statistics.\n>", end='')
        tmp_id = int(input())
        print("[*] Generating statistics based on saved data ...")
        after_stats = AfterStats()
        after_stats.run(tmp_id)

    def run_attack_configuration(self):
        ''' Running attack configuration.'''
        ip='127.0.0.1'
        port = 80

        print('Please privide the attack you want to run:\n[1] DoS\n[2] DDoS\n[3] Exit\n>', end='')
        self.__id = int(input())

        match self.__id:
            case 1:
                ''' DoS '''
                payload="This is just a plain text for DoS."
                amount_of_requests = 0
                print("Please provide amount of reauests you want to be sent at once (recommended value: 2500):\n>", end='')
                amount_of_requests = int(input())

                return DoS(ip, port, amount_of_requests, payload), self.__id

            case 2:
                ''' DDoS '''
                amount_of_requests = 250
                amount_of_threads = 50
                payload = "This is just a plain text for DDoS."
                
                print(f'Please provide amount of threads you want to be used (recommended value: 50):\n>', end='')
                amount_of_threads = int(input())
                
                
                print(f"Please provide amount of requests you want to be sent at once (recommended value:{amount_of_requests}):\n>", end='')
                amount_of_requests = int(input())



                return DDoS(ip, port, amount_of_threads, amount_of_requests, payload), self.__id

            case _:
                print("Bye!")