from settings import Settings
from server import Server
from status import StatusClient

import threading
import time

def menu():
    print("Welcome to DoS and DDoS attacks simulation.")
    print("My github: https://github.com/hue1337")
    new_settings = Settings()
    attack = None
    attack_id = 1

    ''' Default settings '''
    attack, attack_id = new_settings.run_default_attack_configuration()
    while True:
        print('''
Menu:
\t[1] Choose the type of an attack you want to simulate (default: DoS).
\t[2] Run the attack.
\t[3] Generate statistics based on saved data.
\t[4] Exit.

Choose an option:
>''', end="")
        try:
            menu_id = int(input())
        except Exception as e:
            print(e)
        
        match menu_id:
            case 1:
                attack, attack_id = new_settings.run_attack_configuration()

            case 2:
                print("[*] Starting attack simulation...")
                return attack, attack_id

            case 3:
                print("[*] Generating statistics based on saved data ...")
                new_settings.run_stats_generator_based_on_saved_data()
            
            case _:
                print("Bye!")
                exit()
        

        

def main():
    attack,  attack_id = menu()

    victim_server = Server('127.0.0.1', 80, attack_id)
    th1 = threading.Thread(target=victim_server.start_new_instance)
    th1.daemon = True
    th1.start()

    time.sleep(1)

    th_dos = threading.Thread(target=attack.run)
    th_dos.daemon = True
    th_dos.start()

    time.sleep(1)

    status_client = StatusClient('127.0.0.1', 80, attack_id)
    status_client.run()

    th_dos.join()
    th1.join()





if __name__ == '__main__':
    main()