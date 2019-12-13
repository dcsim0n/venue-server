#------------------------------------
#Test module for WB Venue
#------------------------------------
import pytest, socket, ast

def sendMsg(msg):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect( ('localhost',4080) )
            s.sendall( msg )
            
            data = b''
            while True:
              chunk = s.recv(1024)
              if not chunk:
                break
              data += chunk
            
            s.close()
            return data


def test_block():
    blocks = sendMsg( b'rxblock(1) ?\r' )
    assert blocks == b'OK "A1"\r\n'
    blocks = sendMsg( b'rxblock(6) ?')
    assert blocks == b'OK "B1"\r\n'

def test_rxname():
    pass
def test_bvolts():
    bvolts = sendMsg( b'txblevel(*) ?\r' )
    assert bvolts == b'OK {128,128,128,128,128,128}\r\n'

def test_bat():
    bat = sendMsg(b'txbatt(*) ?\r') 
    assert bat == b'OK {0,0,0,0,0,1}\r\n'

def test_level():
    levels = sendMsg(b'rxalevel(*) ?\r')
    assert levels == b'OK {0,0,0,0,0,0}\r\n'

def test_rxlink():
    pass
def test_rxfreq():
    pass

def test_id():
    id = sendMsg( b'id ?\r' )
    assert id == b'OK "VRM2WB"\r\n'



def test_rxscan():
    data = sendMsg(b'devicedata?\r')[3:] #send and strip out the first three characters: 'OK '
    device_data = ast.literal_eval( data.decode() )
    assert device_data['channels'][1]['scan_stat'] == 0
    
    data = sendMsg(b'rxscan(2)=1\r')
    assert data == b'OK \r\n'
    
    data = sendMsg(b'devicedata?\r')[3:] #send and strip out the first three characters: 'OK '
    device_data = ast.literal_eval( data.decode() )
    assert device_data['channels'][1]['scan_stat'] == 1


def test_pollsd():
    data = sendMsg(b'pollsd(1)? $\r')
    assert len(data) >= 280
    assert data[0:2] == b'OK'

def test_serial():
    data = sendMsg(b'serial ?\r')
    assert data == b'OK "123456"\r\n'
