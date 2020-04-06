#***************************
# Abstract Classes for Venue Server
# 2019 Dana Simmons
#***************************

import re, random, socketserver
from schema import Schema


class DeviceABC(socketserver.BaseRequestHandler):
    

    @property
    def _data(self): #put here to avoid changing references in the Sub Class
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
    def __init__(self, *args, device_data:dict , **kwargs):

        print("Creating Venue2 device")

        self.BLOCK_SIZE = 674
        self.CHUNK_SIZE = 15

        socketserver.TCPServer.__init__(self,*args,**kwargs)
        
        schema = Schema({
            'channels':[{
                'block': str,
                'freq':str, 
                'rx_name': str, 
                'bat_type': str, 
                'voltage': str, 
                'pilot': str, 
                'a_level': str, 
                'data':[], 
                'scan_stat': int, 
                'scan_idx': int
            }],
            'type': str,
            'serial': str
        })
        schema.validate(device_data) # check structure of device data

        self._device_data = device_data
        for chan in self._device_data['channels']: # intialize scan data
            for x in range(self.BLOCK_SIZE): # create long array of random ints
                chan['data'].append( random.randint(0,239) )

    
    def toggle_scan_status(self, channel, status):
        assert type(channel) == int, "channel must be of type: int"
        assert type(status) == int, "status must be of type: int"
        # set the 'scan_status' key of the appropriate channel
        self._device_data['channels'][channel - 1]['scan_stat'] = status

    def get_scan_chunk(self, channel):
        assert type(channel) == int, "channel must be of type: int"

        scan_data = self._device_data['channels'][channel - 1]['data']        
        curr_offset = self._device_data['channels'][channel - 1]['scan_idx']
        next_offset = curr_offset + self.CHUNK_SIZE

        # increment offset index, and wrap around if we reach the end
        self._device_data['channels'][channel - 1]['scan_idx'] = next_offset % self.BLOCK_SIZE

        empty_header = "0" * 264
        offset_chunk = "{0:04X}".format( curr_offset )
        scan_chunk = ''
        for i in range(curr_offset, next_offset):
            idx = i % self.BLOCK_SIZE # calculate circular array index
            scan_chunk += "{0:02X}".format( scan_data[idx] ) # convert into two character hex
        print
        
        return "$" + empty_header + offset_chunk + scan_chunk
             
