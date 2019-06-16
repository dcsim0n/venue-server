#!/usr/bin/pythin
# -*- coding: utf-8 -*-

import os, sys, socket, random, time

scanstatus = (0,0,0,0,0,0)
vrtype = 'vrwb'

scanoffset = 0
def mainloop():	
	HOST = ''
	PORT = 4080

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.bind((HOST,PORT))
	s.listen(1)
	
	conn, addr = s.accept()
	print('Connected by', addr)
	global scanoffset
	
	
	while 1:
		data = conn.recv(1024)
		if not data:
			break
		print(data)
		if data == 'id ?\r':
			conn.send('OK "VRWB"\r\n')
			conn.close()
			break
		if data == 'rxscan(1) = 1\r':
			startScan()
			print( "Started scan")
			conn.send('OK \r\n')
			conn.close()
			break
		if data == 'rxscan(2) = 1\r':
			startScan()
			print( "Started scan")
			conn.send('OK \r\n')
			conn.close()
			break
		if data == 'rxscan(3) = 1\r':
			startScan()
			print( "Started scan")
			conn.send('OK \r\n')
			conn.close()
			break
		if data == 'rxscan(3) = 1\r':
			startScan()
			print( "Started scan")
			conn.send('OK \r\n')
			conn.close()
			break
		if data == 'rxscan(4) = 1\r':
			startScan()
			print( "Started scan")
			conn.send('OK \r\n')
			conn.close()
			break
		if data == 'rxscan(5) = 1\r':
			startScan()
			print( "Started scan")
			conn.send('OK \r\n')
			conn.close()
			break
		if data == 'rxscan(6) = 1\r':
			startScan()
			print( "Started scan")
			conn.send('OK \r\n')
			conn.close()
			break
		if data == 'pollsd(1) ?\r':
			newoffset, data = generateScanData(scanoffset)
			scanoffset = newoffset
			conn.send(data)
			conn.close()
			break
		if data == 'pollsd(2) ?\r':
			newoffset, data = generateScanData(scanoffset)
			scanoffset = newoffset
			conn.send(data)
			conn.close()
			break
		if data == 'pollsd(3) ?\r':
			newoffset, data = generateScanData(scanoffset)
			scanoffset = newoffset
			conn.send(data)
			conn.close()
			break
		if data == 'pollsd(4) ?\r':
			newoffset, data = generateScanData(scanoffset)
			scanoffset = newoffset
			conn.send(data)
			conn.close()
			break
		if data == 'pollsd(5) ?\r':
			newoffset, data = generateScanData(scanoffset)
			scanoffset = newoffset
			conn.send(data)
			conn.close()
			break
		if data == 'pollsd(6) ?\r':
			newoffset, data = generateScanData(scanoffset)
			scanoffset = newoffset
			conn.send(data)
			conn.close()
			break
		if data == 'serial ?\r':
			print( "serial sent")
			conn.send('OK "1234"\r\n')	
			conn.close()
			break
	
		if data == 'version ?\r':
			conn.send('OK "5.6"\r\n')
			conn.close()
			break
		if data == 'block(*) ?\r':
			conn.send ('OK {23,25,23,26,23,23}\r\n')
			conn.close()
			break
		if data == 'bvolts(*) ?\r':
			batts = [random.randint(100,150),random.randint(110,160),random.randint(110,160),random.randint(110,160),random.randint(700,900),random.randint(700,900)]
			string = "OK {%d,%d,%d,%d,%d,%d}\r\n" % (batts[0],batts[1],batts[2],batts[3],batts[4],batts[5])
			conn.send(string)
			conn.close()
			break
		if data == 'txbatt(*) ?\r': 
			#battery type status
			#time.sleep(2)
			conn.send('OK {4,4,4,0,0,0}\r\n')
			conn.close()
			break
		if data == 'signal(*) ?\r': 
			#signal present status
			conn.send('OK {1,1,1,1,0,1}\r\n')
			conn.close()
			break
		if data == 'rmeter(*) ?\r':
			
			rmeters = [random.randint(100,255),random.randint(100,255),random.randint(100,255),random.randint(100,255),random.randint(100,255),random.randint(100,255)]
			string = "OK {%d,%d,%d,%d,%d,%d}\r\n" % (rmeters[0],rmeters[1],rmeters[2],rmeters[3],rmeters[4],rmeters[5])
			conn.send(string)
			conn.close()
			break			
		
		if data == 'mhz(*) ?\r': #{23,25,23,26,23,23}
			conn.send('OK {600.0,658.0,589.4,672.0,612.2,610.1}\r\n')
			conn.close()
			break	
		else: 
			conn.close()
			break
		#print( 'closed')
		#conn.close()
		#break 
	
def startScan():
	scanstatus = (1,0,0,0,0)
def stopScan():
	scanStatus = (0,0,0,0,0)
	scanoffset = 0
	
def generateScanData(lastoffset):
	data = "OK $"
	data += "0" * 264
	data += "%0.4X" % lastoffset
	offset = 5
	data += randomList(offset)
	data +='\n'
	lastoffset += offset
	if lastoffset > 255:
		lastoffset = lastoffset - 255
	return lastoffset, data
	
def randomList(length):
	data = ""
	for x in range(length):
		newHex = "%0.2X" % random.randint(0,239)
		data += newHex
	return data

while 1:
	mainloop()

