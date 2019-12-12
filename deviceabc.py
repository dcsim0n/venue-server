#***************************
# Abstract Classes for Venue Server
# 2019 Dana Simmons
#***************************

import re, random, socketserver


class DeviceABC(socketserver.BaseRequestHandler):
    

    @property
    def _data(self):
        return self.server._device_data
    
    def handle(self):
        # should we assert that the data is terminated with a \r character? 
        req_data = self.request.recv(1024).strip().decode('utf8')
        
        print("Received:", req_data)

        req_parts = re.search(r"([a-z]+)(.+)", req_data )
        
        try:
            cmd = req_parts.group(1)
            args = re.sub(r"\s+", "", req_parts.group(2))
            print("Calling: " + cmd + ", with: " + args)
            # incoming data is parsed into two parts
            # a command string and arguments
            # the command string is expexted to match the name of a class method
            # arguments are then passed to the method for more parsing
            resp = getattr(self, cmd )(args )
            resp = f'OK {resp}\r\n'.encode()
        except Exception as err:
            print(err)
            resp = b'Error\r\n'    

        print(f"Sending: {resp}")
        self.request.sendall(resp)

class DeviceServer( socketserver.TCPServer ):
    def __init__(self, *args, **kwargs):

        print("Creating Venue2 device")

        NUMB_OF_BLOCK_STEPS = 674

        socketserver.TCPServer.__init__(self,*args,**kwargs)
        for chan in self._device_data['scan_data']: # intialize scan data
            for x in range(NUMB_OF_BLOCK_STEPS): # create long array of random ints
                chan['data'] += "%0.2X" % random.randint(0,239) # convert random integer into two digit hex

    _device_data = { 
            'scan_data':[ #define empty array of data 
                {'status':0, 'data': []},
                {'status':0, 'data': []},
                {'status':0, 'data': []},
                {'status':0, 'data': []},
                {'status':0, 'data': []},
                {'status':0, 'data': []},
                
            ],
            'channels':[
                {'block': 'A1', 'rx_name': 'RX 1', 'freq': '200100', 'label': 'none', 'bat_type': '4', 'voltage': '128', 'pilot':'1', 'a_level': '0', 'scan_stat': False, 'scan_idx': 0},
                {'block': 'A1', 'rx_name': 'RX 2', 'freq': '200100', 'label': 'none', 'bat_type': '4', 'voltage': '128', 'pilot':'1', 'a_level': '0', 'scan_stat': False, 'scan_idx': 0},
                {'block': 'A1', 'rx_name': 'RX 3', 'freq': '200100', 'label': 'none', 'bat_type': '4', 'voltage': '128', 'pilot':'1', 'a_level': '0', 'scan_stat': False, 'scan_idx': 0},
                {'block': 'A1', 'rx_name': 'RX 4', 'freq': '200100', 'label': 'none', 'bat_type': '0', 'voltage': '128', 'pilot':'1', 'a_level': '0', 'scan_stat': False, 'scan_idx': 0},
                {'block': 'A1', 'rx_name': 'RX 5', 'freq': '210100', 'label': 'none', 'bat_type': '0', 'voltage': '128', 'pilot':'1', 'a_level': '0', 'scan_stat': False, 'scan_idx': 0},
                {'block': 'A1', 'rx_name': 'RX 6', 'freq': '210100', 'label': 'none', 'bat_type': '0', 'voltage': '128', 'pilot':'1', 'a_level': '0', 'scan_stat': False, 'scan_idx': 0},
            ],
            'type': 'VRM2WB',
            'serial': '123456'
        }