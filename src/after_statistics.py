import os
import matplotlib.pyplot as plt

class AfterStats:
    __dos = None
    __ddos = None
    __data_path = None   
    __home_path = None

    def __init__(self):
        self.__dos = []
        self.__ddos = []
        self.__home_path = os.getcwd()

        ''' Initialization of data path '''
        self.check_if_data_is_correct
        self.__data_path = os.getcwd() + '/data'
        
    def run(self, attacks_id):
        if self.check_if_data_is_correct():
            self.read_data()
        
        if attacks_id == 1:
            self.generate_line_charts_dos()
        elif attacks_id == 2:
            self.generate_line_charts_ddos()
        elif attacks_id == 3:
            self.generate_line_charts_dos_ddos()

    ''' Data '''
    def read_data(self):
        ''' Reading data from files '''
        os.chdir(self.__data_path + '/dos')

        """ DoS """
        tmp_dos = []
        os.chdir(self.__data_path + '/dos')
        
        for file in os.listdir(self.__data_path + '/dos'):
            if self.if_file_is_allowed(file):
                with open(file, 'r') as f:
                    for line in f:
                        tmp_dos.append(float(line))
                    f.close()
                self.__dos.append(list(tmp_dos))
                tmp_dos.clear()

        ''' DDoS '''
        tmp_ddos = []
        os.chdir(self.__data_path + '/ddos')

        for file in os.listdir(self.__data_path + '/ddos'):
            if self.if_file_is_allowed(file):
                with open(file, 'r') as f:
                    for line in f:
                        tmp_ddos.append(float(line))
                    f.close()   
                self.__ddos.append(list(tmp_ddos))
                tmp_ddos.clear()
        
        os.chdir(self.__home_path)

    def analyze_data(self):
        pass

    def check_if_data_is_correct(self):
        '''If data exists '''
        os.chdir(self.__home_path)
        try:
            if not os.path.exists('data'):
                os.mkdir('data')
            if not os.path.exists('data/dos'):
                os.mkdir('data/dos')
            if not os.path.exists('data/ddos'):
                os.mkdir('data/ddos')
            if not os.path.exists('data/line_charts'):
                os.mkdir('data/line_charts')
            if not os.path.exists('data/line_charts/dos'):
                os.mkdir('data/line_charts/dos')
            if not os.path.exists('data/line_charts/ddos'):
                os.mkdir('data/line_charts/ddos')
            return True
        except Exception as e:
            print(f'[-] Error occurred during data check: {e}')
            return False


    ''' Line charts '''
    def generate_line_charts_dos(self):
        ''' Generate line charts '''
        
        ''' DoS '''
        for i in range(1, len(self.__dos)+1):
            x = []
            for counter in range(1, len(self.__dos[i-1])+1):
                x.append(counter)
            plt.plot(x, self.__dos[i-1])
            plt.xlabel('Time [s]')
            plt.ylabel('Ping [ms]')
            plt.title(f'DoS simulation {i}')

            plt.savefig(f'data/line_charts/dos/dos_{i}.png')
            plt.clf()

    def generate_line_charts_ddos(self):
        ''' DDoS '''
        for i in range(1, len(self.__ddos)+1):
            x = []
            for counter in range(1, len(self.__ddos[i-1])+1):
                x.append(counter)
                counter
            plt.plot(x, self.__ddos[i-1])
            plt.xlabel('Time [s]')
            plt.ylabel('Ping [ms]')
            plt.title(f'DDoS simulation {i}')

            plt.savefig(f'data/line_charts/ddos/ddos_{i}.png')
            plt.clf()

    def generate_line_charts_dos_ddos(self):
        ''' Generate for both attacks '''
        self.generate_line_charts_dos()
        self.generate_line_charts_ddos()


    ''' Files '''
    def if_file_is_allowed(self, file_name):
        if 'dos' in file_name or 'ddos' in file_name:
            return True
        else:
            return False

