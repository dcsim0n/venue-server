
import socketserver
from deviceabc import DeviceABC

class VRWB(DeviceABC):
    def __init__(self,*args):
        DeviceABC.__init__(self,*args)

        print("Creating VRWB device")
        
    _data = { 
            'channels':[
                {'block': '23', 'freq': 200, 'label': 'none', 'bat_type': '4', 'voltage': '128' },
                {'block': '25', 'freq': 205, 'label': 'none', 'bat_type': '4', 'voltage': '128' },
                {'block': '23', 'freq': 206, 'label': 'none', 'bat_type': '4', 'voltage': '128' },
                {'block': '26', 'freq': 208, 'label': 'none', 'bat_type': '0', 'voltage': '128' },
                {'block': '23', 'freq': 210, 'label': 'none', 'bat_type': '0', 'voltage': '128' },
                {'block': '23', 'freq': 214, 'label': 'none', 'bat_type': '0', 'voltage': '128' },
            ],
            'type': 'VRWB',
            'serial': '123456'
        }

    def block(self, args):
        print('parsing:' + str(args) )
        blocks = map(lambda chan: chan['block'], self._data['channels']) 

        return '{' + ','.join( blocks ) + '}'
    
    def txbatt(self, args):
        bat_types = map(lambda chan: chan['bat_type'], self._data['channels'])
        return '{' + ','.join( bat_types ) + '}'

    def id(self, args):
        print('pasing:' + str(args))
        return '"' + self._data['type'] + '"'
    
    def serial(self, args):
        return '"620023"'


if __name__ == "__main__":
    server = socketserver.TCPServer(( 'localhost', 4080 ), VRWB)

    server.serve_forever()