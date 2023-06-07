from client import Client

import os
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class StatusClient(Client):
    __fig = None
    __ax = None
    __data = []
    __counter = 0
    __ping = 0.0
    __type_of_attack = None
    __next_id = None
    def __init__(self, ip='0.0.0.0', port=80, type_of_attack=1):
        super().__init__(ip, port)
        self.__counter = 0
        self.__fig, self.__ax = plt.subplots()
        self.__type_of_attack = type_of_attack
    

    def save_to_file(self):
        ''' Saving data to file.'''
        if self.__type_of_attack == 1:
            file = open(f'data/dos/dos_{self.__next_id}.csv', 'w')
            for pi in self.__data:
                file.write(str(pi) + '\n')

            file.close()

        else:
            file = open(f'data/ddos/ddos_{self.__next_id}.csv', 'w')
            for pi in self.__data:
                file.write(str(pi) + '\n')

            file.close()

    def mapping_folders(self, attack_id):
        ''' Mapping folders.'''
        attack_types = {
            1: "dos",
            2: "ddos"
        }

        if attack_id not in attack_types:
            print(f"Invalid attack ID: {attack_id}")
            return

        attack_type = attack_types[attack_id]
        data_folder = "data"
        folder_path = os.path.join(data_folder, attack_type)
        file_mapping = []

        if os.path.exists(data_folder):
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            for file_name in os.listdir(folder_path):
                file_mapping.append(file_name)

            if not file_mapping:
                new_file_name = f"{attack_type}_1.csv"
                new_file_path = os.path.join(folder_path, new_file_name)
                open(new_file_path, 'a').close()

            max_id = 0
            for file_name in file_mapping:
                parts = file_name.split("_")

                try:
                    if len(parts) >= 2:
                        file_id = int(parts[1].split(".")[0])
                        max_id = max(max_id, file_id)
                except:
                    pass

            next_id = max_id + 1
            self.__next_id = next_id
        else:
            print(f"Folder not found: {data_folder}")


    def save_data(self):
        ''' Saving data to file every 10 seconds.'''
        self.__counter += 1
        if self.__counter == 10:
            self.__counter = 0
            try:
                self.save_to_file()
            except:
                pass
    
    def stats(self, i):
        self.save_data()

        ''' Collecting ping'''
        self.collecting_ping()
        if self.__ping == -2.0:
            exit()

        self.__data.append(self.__ping)

        self.__ax.clear()
        
        ''' dodane '''
        self.__ax.set_xlabel('Time [s]')
        self.__ax.set_ylabel('Ping [ms]')

        self.__ax.plot(self.__data[-30:])


    def show_data(self):
        ''' Showing data on plot.'''
        ani = FuncAnimation(self.__fig, self.stats, interval=1000, save_count=60)
        plt.xlabel('Last 30 seconds [s]')
        plt.ylabel('Ping [ms]')
        plt.show()

        # while True:
        #     self.save_data()
        #     time.sleep(1)
        
    def run(self):
        ''' Running client.'''
        super().connect_to_host()
        self.mapping_folders(self.__type_of_attack)
        self.show_data()
    
    def collecting_ping(self) -> None:
        ''' Collecting ping.'''
        try:
            self.__ping = float(super().accept_payload())
        except Exception as e:
            print(e)
            self.__ping = -2.0



 