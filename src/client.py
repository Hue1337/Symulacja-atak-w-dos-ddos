import socket
import time

class Client:
    __host = '0.0.0.0'
    __port = 80
    __payload = 'ACK!'
    __client_socket = None

    def __init__(self, host, port, payload=''):
        self.__host = host
        self.__port = port
        self.__payload = payload
        
    def connect_to_host(self):
        self.__client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.__client_socket.connect((self.__host, self.__port))
        except Exception as e:
            print(f'[-] Failed to connect to the host.\n\t{e}')

    def disconnect_from_host(self):
        try:
            self.__client_socket.close()
        except Exception as e:
            print(f'[-] Failed to disconnect from the host.\n\t{e}')

    def send_paylaod(self):
        try:
            self.__client_socket.send(self.__payload.encode())
        except Exception as e:
            print(f'[-] Failed to deliver a payload to the host.\n\t{e}')


    def accept_payload(self) -> str:
        try:
            response = self.__client_socket.recv(4096).decode()
            return response
        except Exception as e:
            # print(f'[-] Error occured during accepting message:\n\t{e}')
            pass
        
    def set_payload(self, payload) -> None:
        self.__payload = payload

    def get_paylaod(self) -> str:
        return self.__payload


    def run(self):
        self.connect_to_host()
        self.send_paylaod()
        self.accept_payload()
        self.disconnect_from_host()

    def return_host(self)->str:
        return self.__host
    
    def return_port_int(self)->int:
        return self.__port

    def return_port_str(self)->str:
        return str(self.__port)