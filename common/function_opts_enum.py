from services import http_banner_grabber_service, subdomain_scanner_service, tcp_port_scanner_service, web_scrapper_service, security_header_checker_service, local_network_scanner_service, web_file_discovery_service
from common import helper
from enum import Enum

class FunctionOptions(Enum):
    HTTP_BANNER_GRABBER =       (1, '-hbg', http_banner_grabber_service)
    TCP_PORT_SCANNER =          (2, '-tps', tcp_port_scanner_service)
    SUBDOMAIN_SCANNER =         (3, '-ss',  subdomain_scanner_service)
    WEB_SCRAPPER =              (4, '-ws',  web_scrapper_service)
    SECURITY_HEADER_CHECKER =   (5, '-shc', security_header_checker_service)
    LOCAL_NETWORK_SCANNER =     (6, '-lns', local_network_scanner_service)
    WEB_FILE_DISCOVERY =        (7, '-wfd', web_file_discovery_service)
    HELPER =                    (8, '-h', helper)

    def __init__(self, number, command, _class):
        self.number = number
        self.command = command
        self._class = _class

    @classmethod
    def get_by_number(self, number):
        for option in self:
            if option.number == number:
                return option
        raise ValueError(f"{number} isn't valid")
    
    @classmethod
    def get_by_command(self, command):
        for option in self:
            if option.command == command:
                return option
        raise ValueError(f"{command} isn't valid")  
