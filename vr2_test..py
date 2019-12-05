#------------------------------------
#Test module for WB Venue
#------------------------------------
import pytest, socket

def sendMsg(msg):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect( ('localhost',4080) )
            s.sendall( msg )
            data = s.recv(1024)
            s.close()
            return data


def test_block():
    blocks = sendMsg( b'rxblock(*) ?\r' )
    assert blocks == b'OK {A1,A1,A1,A1,A1,A1}\r\n'

def test_rxname():
    pass
def test_bvolts():
    bvolts = sendMsg( b'bvolts(*) ?\r' )
    assert bvolts == b'OK {128,128,128,128,128,128}'

def test_bat():
    bat = sendMsg(b'txbatt(*) ?\r') 
    assert bat == b'OK {4,4,4,0,0,0}\r\n'

def test_level():
    levels = sendMsg(b'level(*) ?\r')
    assert levels == b'OK {0,0,0,0,0,0}'

def test_rxlink():
    pass
def test_rxfreq():
    pass

def test_id():
    id = sendMsg( b'id ?\r' )
    assert id == b'OK "VRWB"\r\n'



def test_rxscan():
    data = sendMsg(b'rxscan(2)=1\r')
    assert data == b'OK \r\n'


def test_pollsd():
    assert True == False


def test_serial():
    data = sendMsg(b'serial ?\r')
    assert data == b'OK "620023"\r\n'
