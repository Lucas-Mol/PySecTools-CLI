import socket
from validators import tps_arg_validator
from common import helper

def run(args):
    
    if '-h' in args:
        helper.tps_helper()

    tps = tps_arg_validator.validate(args)

    print('---------------------------------------------')
    print('---------------- Scanning... ----------------')
    print('---------------------------------------------')
    open_ports = set()

    for port in range(tps.start_port, tps.end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        
        try:
            print(f'Trying {port} port...')
            s.connect((tps.target, port))
            print(f'Port {port} is open!!!')
            open_ports.append(str(port))
            banner = s.recv(1024)
            if banner:
                print(f'Service: {banner.decode("utf-8").strip()}')
            s.close()
        except:
            pass

    print('---------------------------------------------')
    print('------------- Scanner Complete --------------')
    print('---------------------------------------------')
    if open_ports:
        print(f'All open ports: {", ".join(open_ports)}')
    else:
        print('No open port found')
