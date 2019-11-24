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
    blocks = sendMsg( b'block(*) ?\r' )
    assert blocks == b'OK {23,25,23,26,23,23}\r\n'

def test_serial():
    id = sendMsg( b'id ?\r' )
    assert id == b'OK "VRWB"\r\n'


def test_bat():
    bat = sendMsg(b'txbatt(*) ?\r') 
    assert bat == b'OK {4,4,4,0,0,0}\r\n'