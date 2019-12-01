
import socketserver
import re


class DeviceABC(socketserver.BaseRequestHandler):
    


    def handle(self):
        print("Receiving data..")
        data = self.request.recv(1024).strip().decode('utf8')
        print("Data:", data)
        req_parts = re.search(r"([a-z]+)(.+)",  data )
        print(req_parts.group(1))

        try:
            cmd = req_parts.group(1)
            args = req_parts.group(2)

            resp = getattr(self, cmd )(args )
        except Exception as err:
            print(err)
            resp = b'Error\n'    
        print("Sending: " + resp)
        self.request.sendall(resp)

