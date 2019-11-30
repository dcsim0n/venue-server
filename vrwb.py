
import socketserver
from deviceabc import DeviceABC

class VRWB(DeviceABC):
    def __init__(self,*args):
        DeviceABC.__init__(self,*args)

        print("Creating VRWB device")
        self.data = {
            'channels':[
                {'block': 21, 'freq': 200, 'label': 'none'},
                {'block': 21, 'freq': 205, 'label': 'none'},
                {'block': 21, 'freq': 206, 'label': 'none'},
                {'block': 21, 'freq': 208, 'label': 'none'},
                {'block': 21, 'freq': 210, 'label': 'none'},
                {'block': 21, 'freq': 214, 'label': 'none'},
            ],
            'type': 'VRWB',
            'serial': '123456'
        }

    def block(self, args):
        print('parsing:' + str(args) )

    
    def id(self, args):
        print('pasing:' + str(args))
    


if __name__ == "__main__":
    server = socketserver.TCPServer(( 'localhost', 8080 ), VRWB)

    server.serve_forever()