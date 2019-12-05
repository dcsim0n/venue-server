import re
import socketserver
from deviceabc import DeviceABC

class VR2(DeviceABC):
    def __init__(self,*args):
        DeviceABC.__init__(self,*args)

        print("Creating Venue2 device")
        
    _data = { 
            'channels':[
                {'rxblock': 'A1', 'rx_name': 'RX 1', 'freq': '200100', 'label': 'none', 'bat_type': '4', 'voltage': '128', 'pilot':'1', 'a_level': '0', 'scan_stat': False, 'scan_idx': 0},
                {'rxblock': 'A1', 'rx_name': 'RX 2', 'freq': '200100', 'label': 'none', 'bat_type': '4', 'voltage': '128', 'pilot':'1', 'a_level': '0', 'scan_stat': False, 'scan_idx': 0},
                {'rxblock': 'A1', 'rx_name': 'RX 3', 'freq': '200100', 'label': 'none', 'bat_type': '4', 'voltage': '128', 'pilot':'1', 'a_level': '0', 'scan_stat': False, 'scan_idx': 0},
                {'rxblock': 'A1', 'rx_name': 'RX 4', 'freq': '200100', 'label': 'none', 'bat_type': '0', 'voltage': '128', 'pilot':'1', 'a_level': '0', 'scan_stat': False, 'scan_idx': 0},
                {'rxblock': 'A1', 'rx_name': 'RX 5', 'freq': '210100', 'label': 'none', 'bat_type': '0', 'voltage': '128', 'pilot':'1', 'a_level': '0', 'scan_stat': False, 'scan_idx': 0},
                {'rxblock': 'A1', 'rx_name': 'RX 6', 'freq': '210100', 'label': 'none', 'bat_type': '0', 'voltage': '128', 'pilot':'1', 'a_level': '0', 'scan_stat': False, 'scan_idx': 0},
            ],
            'type': 'VRM2WB',
            'serial': '123456'
        }

    def rxblock(self, args):
        blocks = map(lambda chan: chan['block'], self._data['channels']) 
        return '{' + ','.join( blocks ) + '}'
    def rxname(self, args):
        #parse args to get channel
        channel = re.search(r"\((\d)\)\?", args).group(1)
        ch_idx = int( channel ) - 1 #convert to int and subract one for index
        return '"' + self._data['channels'][ ch_idx ].label + '"'
        
    def txblevel(self, args): # battery volts
        volts = map(lambda chan: chan['voltage'], self._data['channels'])
        return '{' + ','.join( volts ) + '}'

    def txbatt(self, args): # battery type
        bat_types = map(lambda chan: chan['bat_type'], self._data['channels'])
        return '{' + ','.join( bat_types ) + '}'

    #def level(self, args): # Audio output status
    #    levels = map(lambda chan: chan['a_level'], self._data['channels'])
    #    return '{' + ','.join( levels ) + '}'
    
    def rxlink(self, args): # Pilot tone status
        pilots = map(lambda chan: chan['pilot'], self._data['channels'])
        return '{' + ','.join( pilots ) + '}'
    
    def rxfreq(self, args): # channel frequency
        freqs = map(lambda chan: chan['freq'], self._data['channels'])
        return '{' + ','.join(freqs) + '}'

    def id(self, args):
        return '"' + self._data['type'] + '"'

    def serial(self, args):
        return '"' + self._data['serial'] + '"'



if __name__ == "__main__":
    server = socketserver.TCPServer(( '0.0.0.0', 4080 ), VRWB)

    server.serve_forever()