#!/usr/bin/pythin
# -*- coding: utf-8 -*-

import os, sys, socket


def mainloop():
	HOST = ''
	PORT = 4081
	

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.bind((HOST,PORT))
	s.listen(1)

	conn, addr = s.accept()
	print(['Connected by', addr])
	
	
	
	while 1:
		data = conn.recv(1024)
		if not data:
			break
		print(data)
		if data == 'id ?\r':
			conn.send('OK "VRM2WB"\r\n')
			conn.close()
			break
			#break
			
		
		if data == 'serial ?\r':
			print("serial sent")
			conn.send('OK "56789"\r\n')	
			#conn.close()
			#break
	
		if data == 'version ?\r':
			conn.send('OK "5.6"\r\n')
			#conn.close()
			#break
		if data == 'portctl(*) ?\r': #port status check
			conn.send('OK "0,0,3,3,3"\r\n')
			
		if data == 'rxblock(*) ?\r':
			conn.send ('OK {A1,A1,B1,C1,C1,B1}\r\n')
			#break
		if data == 'txblevel(*) ?\r':
			conn.send('OK {170,160,160,124,130,140}\r\n')
			#break
		if data == 'txblock(1) ?\r':
			conn.send('OK "21"\r\n')
		if data == 'txblock(2) ?\r':
			conn.send('OK "22"\r\n')
		if data == 'txblock(3) ?\r':
			conn.send('OK "23"\r\n')
		if data == 'txblock(4) ?\r':
			conn.send('OK "24"\r\n') 
		if data == 'txblock(5) ?\r':
			conn.send('OK "25"\r\n')
		if data == 'txblock(6) ?\r':
			conn.send('OK "26"\r\n')
		
		if data == 'chstat(*) ?\r': #LOTS OF DATA
			conn.send ('OK chstat(1)={1,1,2,-3,22,0,1,0,0,97,0,0,0,0}\r\n')
			
		if data == 'rxpresent(*) ?\r':
			conn.send('OK {1,1,1,1,1,0}\r\n')
			#break
		if data == 'rxpwr(*) ?\r':
			conn.send('OK {1,1,1,1,1,0}\r\n')
		
			#break
		if data == 'rxlink(*) ?\r':
			conn.send('OK {1,1,1,1,1,1}\r\n')	
		if data == 'rxrmeter(*) ?\r':
			conn.send('OK {255,255,180,180,120,120}\r\n')	
		if data == 'txbatt(*) ?\r': 
			#battery type status
			conn.send('OK {0,0,0,0,0,0}\r\n')
		if data == 'rxfreq(*) ?\r':
			conn.send('OK {541100,573100,600300,630400,655300,670800}\r\n')
			conn.close()
			print("closed")
			break


		

		#conn.close()
		#break 
	

while 1:
	mainloop()