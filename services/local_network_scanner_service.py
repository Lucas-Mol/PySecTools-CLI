from scapy.all import ARP, Ether, srp
from manuf import manuf
from validators import lns_arg_validator
from common import helper

def run(args):
    
    if '-h' in args:
        helper.lns_helper()

    lns = lns_arg_validator.validate(args)

    print('---------------------------------------------')
    print('---------------- Scanning... ----------------')
    print('---------------------------------------------')

    devices = []

    arp = ARP(pdst=lns.ir)
    ether = Ether(dst='ff:ff:ff:ff:ff:ff')
    packet = ether/arp
    result = srp(packet, timeout=3, iface=lns.interface, verbose=0)[0]

    for sent, received in result:
        mac_address = received.hwsrc
        vendor = get_vendor(mac_address)
        devices.append({'ip': received.psrc, 'mac': mac_address, 'vendor': vendor})

    print('---------------------------------------------')
    print('------------- Scanner Complete --------------')
    print('---------------------------------------------')

    if devices:
        print(f'All devices: ')
        for device in devices:
            print(device)
    else:
        print('No device found')



def get_vendor(mac_adrress):
    try:
        return manuf.MacParser().get_manuf(mac_adrress)
    except manuf.ManufLookupError:
        return 'Unkown'
