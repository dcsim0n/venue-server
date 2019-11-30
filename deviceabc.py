
import socketserver
import re


class DeviceABC(socketserver.BaseRequestHandler):
    


    def handle(self):
        print("Receiving data..")
        data = self.request.recv(1024).strip().decode('utf8')
        print("Data:", data)
        req_parts = re.search("[a-z]+\b.+",  data )
        print(req_parts)

        try:
            cmd = req_parts.group(0)
            args = req_parts.group(1)

            resp = getattr(self.server, cmd )( args )
        except:
            resp = b'Error\n'    
        self.request.sendall(resp)

