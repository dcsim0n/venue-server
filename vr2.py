import socketserver, random, re
from deviceabc import DeviceABC,DeviceServer

class VR2( DeviceABC ):

    # I Dont recomend adding assertions to these
    # even though they are external functions, they should
    # be called as part of a try/except block 
    def rxblock(self, args):
        blocks = map(lambda chan: chan['block'], self._data['channels']) 
        return '{' + ','.join( blocks ) + '}'
    
    def rxname(self, args):
        #parse args to get channel
        channel = re.search(r"\((\d)\)\?", args).group(1)
        ch_idx = int( channel ) - 1 #convert to int and subract one for index
        return '"' + self._data['channels'][ ch_idx ]['rx_name'] + '"'
        
    def txblevel(self, args): # battery volts
        volts = map(lambda chan: chan['voltage'], self._data['channels'])
        return '{' + ','.join( volts ) + '}'

    def txbatt(self, args): # battery type
        bat_types = map(lambda chan: chan['bat_type'], self._data['channels'])
        return '{' + ','.join( bat_types ) + '}'

    def rxalevel(self, args): # Audio output status
       levels = map(lambda chan: chan['a_level'], self._data['channels'])
       return '{' + ','.join( levels ) + '}'
    
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

    def rxscan(self, args):
        m = re.match(r'\(([1-6])\)=([01])',args) # match the channel 
        channel = int( m.group(1) )
        toggle = int ( m.group(2) )
        self.server.toggle_scan_status(channel,toggle)
        #else:
        #    m = re.match(r'\([1-6\*]\)\?$', args) # match for (1)? and (*)? type requests
        # 
        return ''
    def pollsd(self, args):
        m = re.match(r'\(([1-6])\)\?\$',args)
        channel = int( m.group(1) )
        
        return self.server.get_scan_chunk( channel )



    def devicedata(self,args):
        return self.server._device_data



if __name__ == "__main__":
    server = DeviceServer(( '0.0.0.0', 4080 ), VR2)

    server.serve_forever()