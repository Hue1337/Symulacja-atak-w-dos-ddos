import socket
import random
import time

from threading import Thread


from server_interface import ServerInterface

class Server(ServerInterface):
    __host = '0.0.0.0'
    __port = 80
    __server_socket = None
    __message = ''
    __threads = []
    __clients_connected = []
    __ping = 1.0
    __type_of_attack = 1

    ''' Required for ping '''
    __client_socket = None
    __client_address = None

    ''' Dodane zmienne '''
    __amount_of_connections = 0
    __amuont_of_paylaods = 0

    ''' Required for (VIP) status client'''
    __client_socket_status = None
    __client_address_status = None

    ''' Server is done after the random number above 2000 requests ''' 
    __the_end = 0

    def __init__(self, ip, port, type_of_attack):
        self.__host = ip
        self.__port = port
        self.__server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__message = '[+] Connection accepted.'
        self.__the_end = random.randint(0, 500)
        self.__type_of_attack = type_of_attack

    def start_new_instance(self):
        self.__server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.__server_socket.bind((self.__host, self.__port))
        self.__server_socket.listen(5)
        print(f'Listening on {self.__host}:{self.__port}')

        ''' Server status controller '''
        match self.__type_of_attack:
            case 1:
                server_status_controller = Thread(target=self.ping_manipulation_dos)
                server_status_controller.start()
            
            case 2:
                server_status_controller = Thread(target=self.ping_manipulation_ddos)
                server_status_controller.start()
            
            case _:
                print('[-] Incorrect type of attack!')

        ''' Simulating ping response '''
        ping_response = Thread(target=self.send_ping)
        ping_response.start()

        ''' Sending simulated ping to a status client '''
        sending_simulated_ping = Thread(target=self.send_simulated_ping)
        sending_simulated_ping.start()

        while True:
            self.__client_socket, self.__client_address = self.__server_socket.accept()
            self.__client_socket_status, self.__client_address_status = self.__server_socket.accept()
            self.__clients_connected.append(self.__client_socket_status)
            self.__clients_connected.append(self.__client_socket)

            # print(f"[*] Accepted connection from: {client_address}:{client_socket}")

            '''  Obslugiwanie za duzej ilosci clientow '''
            # client_handler = Thread(target=self.handle_client, args=(client_socket, client_address,))
            # client_handler.start()
            self.handle_client()

            if self.__ping == -2.0:
                self.disconnect_all()
                return



            # client_socket.close()


            
    def handle_client(self):
        while True:
            try:
                response = self.__client_socket.recv(1024).decode('utf-8')
                
                if response:
                    if self.__ping != -2.0:
                        print(f'[+] Received message from: {self.__client_address}\n\t{response}')
                        if response == '!abort':
                            self.__ping = -2.0
                            exit()
                    try:
                        self.__client_socket.send(str(self.__ping).encode())
                    except:
                        break

                    ''' Data manipulation '''
                    self.increase_amount_of__connections()
                    self.increase_amount_of_paylaods()
                    self.print_current_status()
            except:
                pass
        # client_socket.send(self.__message.encode())


    def run(self):
        my_thread = Thread(target=self.start_new_instance());
        my_thread.start();
        self.__threads.append(my_thread)
    
    def stop_all_threads(self):
        for t in self.__threads:
            t.stop()

    def send_ping(self):
        ''' Sending ping to client '''
        while True:
            try:
                self.__server_socket.send(self.__ping.encode())
            except:
                pass
            time.sleep(1)


    ''' Simualtion rules '''
    def increase_amount_of__connections(self) -> None:
        self.__amount_of_connections += 1

    def increase_amount_of_paylaods(self) -> None:
        self.__amuont_of_paylaods += 1

    def return_ping(self) -> float:
        ''' Getter for ping '''
        return self.__ping

    def ping_manipulation_dos(self) -> None:
        ''' Manipulation of ping during DoS attack '''
        while True:
            if self.__ping == -2.0:
                break
            if self.__amount_of_connections < 250:
                ''' 1-30ms '''
                self.__ping = self.ping_manipulation_algorithm(250)
            
            elif self.__amount_of_connections < 750:
                # self.__ping = -2.0
                self.__ping = self.ping_manipulation_algorithm(750)
            
            elif self.__amount_of_connections < 1250:
                self.__ping = self.ping_manipulation_algorithm(1250)

            elif self.__amount_of_connections < 2000-self.__the_end:
                self.__ping = self.ping_manipulation_algorithm(2000)
            else:
                ''' Server stopped working '''
                self.__ping = -2.0
            time.sleep(0.1)


    def ping_manipulation_ddos(self) -> None:
        ''' Manipulation of ping during DDoS attack '''
        while True:
            if self.__ping == -2.0:
                break
            if self.__amount_of_connections < 175:
                ''' 1-30ms '''
                self.__ping = self.ping_manipulation_algorithm(250)
            
            elif self.__amount_of_connections < 450:
                # self.__ping = -2.0
                self.__ping = self.ping_manipulation_algorithm(750)
            
            elif self.__amount_of_connections < 750:
                self.__ping = self.ping_manipulation_algorithm(1250)

            elif self.__amount_of_connections < 1500-self.__the_end:
                self.__ping = self.ping_manipulation_algorithm(2000)
            else:
                ''' Server stopped working '''
                self.__ping = -2.0
            time.sleep(0.1)
        

    def ping_manipulation_algorithm(self, limit) -> float:
        ''' Algorithm for ping manipulation '''
        percentage_ping = self.__amount_of_connections/10
        temp_ping = percentage_ping
        temp_ping += random.uniform(-percentage_ping/(2*len(str(self.__amount_of_connections))), percentage_ping/len(str(self.__amount_of_connections)))
        return round(temp_ping, 2)

    def print_current_status(self) -> None:
        if self.__ping != -2.0:
            print(f'Current status:\n\tAmount of connections: {self.__amount_of_connections}\n\tAmount of paylaods: {self.__amuont_of_paylaods}\n\tPing: {self.__ping}ms')

    def send_simulated_ping(self) -> None:
        ''' Sending simulated ping to a status client '''
        while True:
            try:
                self.__client_socket_status.send(str(self.__ping).encode())
            except:
                pass
            time.sleep(1)

    def disconnect_all(self):
        for client in self.__clients_connected:
            client.close()
