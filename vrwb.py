
import re
from deviceabc import DeviceABC, DeviceServer

class VRWB(DeviceABC):
    def __init__(self,*args):
        DeviceABC.__init__(self,*args)

        print("Creating VRWB device")
        

    def block(self, args):
        blocks = map(lambda chan: chan['block'], self._data['channels']) 
        return '{' + ','.join( blocks ) + '}'

    def bvolts(self, args): # battery volts
        volts = map(lambda chan: chan['voltage'], self._data['channels'])
        return '{' + ','.join( volts ) + '}'

    def txbatt(self, args): # battery type
        bat_types = map(lambda chan: chan['bat_type'], self._data['channels'])
        return '{' + ','.join( bat_types ) + '}'

    def level(self, args): # Audio output status
        levels = map(lambda chan: chan['a_level'], self._data['channels'])
        return '{' + ','.join( levels ) + '}'
    
    def signal(self, args): # Pilot tone status
        pilots = map(lambda chan: chan['pilot'], self._data['channels'])
        return '{' + ','.join( pilots ) + '}'
    
    def mhz(self, args): # channel frequency
        freqs = map(lambda chan: chan['freq'], self._data['channels'])
        return '{' + ','.join(freqs) + '}'

    def id(self, args):
        return '"' + self._data['type'] + '"'

    def serial(self, args):
        return '"' + self._data['serial'] + '"'

    def pollsd(self, args):
        m = re.match(r'\(([1-6])\)\?\$',args)
        channel = int( m.group(1) )
        
        return self.server.get_scan_chunk( channel )
    
    def rxscan(self, args):
        m = re.match(r'\(([1-6])\)=([01])',args) # match the channel 
        channel = int( m.group(1) )
        toggle = int ( m.group(2) )
        self.server.toggle_scan_status(channel,toggle)
        return ''

if __name__ == "__main__":

    device_data = {
            'channels':[
                {'block': '23', 'freq': '200.0', 'rx_name': 'RX 1', 'bat_type': '4', 'voltage': '128', 'pilot':'1', 'a_level': '0', 'data':[], 'scan_stat': 0, 'scan_idx': 0},
                {'block': '25', 'freq': '205.0', 'rx_name': 'RX 2', 'bat_type': '4', 'voltage': '128', 'pilot':'1', 'a_level': '0', 'data':[], 'scan_stat': 0, 'scan_idx': 0},
                {'block': '23', 'freq': '206.0', 'rx_name': 'RX 3', 'bat_type': '4', 'voltage': '128', 'pilot':'1', 'a_level': '0', 'data':[], 'scan_stat': 0, 'scan_idx': 0},
                {'block': '26', 'freq': '208.0', 'rx_name': 'RX 4', 'bat_type': '0', 'voltage': '128', 'pilot':'1', 'a_level': '0', 'data':[], 'scan_stat': 0, 'scan_idx': 0},
                {'block': '23', 'freq': '210.0', 'rx_name': 'RX 5', 'bat_type': '0', 'voltage': '128', 'pilot':'1', 'a_level': '0', 'data':[], 'scan_stat': 0, 'scan_idx': 0},
                {'block': '23', 'freq': '214.0', 'rx_name': 'RX 6', 'bat_type': '0', 'voltage': '128', 'pilot':'1', 'a_level': '0', 'data':[], 'scan_stat': 0, 'scan_idx': 0},
            ],
            'type': 'VRWB',
            'serial': '620023'
        }
    server = DeviceServer(( '0.0.0.0', 4080 ), VRWB, device_data=device_data )

    server.serve_forever()