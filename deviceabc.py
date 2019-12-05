
import socketserver
import re


class DeviceABC(socketserver.BaseRequestHandler):
    


    def handle(self):
        # should we assert that the data is terminated with a \r character? 
        req_data = self.request.recv(1024).strip().decode('utf8')
        
        print("Received:", req_data)

        req_parts = re.search(r"([a-z]+)(.+)", req_data )
        
        try:
            cmd = req_parts.group(1)
            args = re.sub("\s+", "", req_parts.group(2))
            print("Calling: " + cmd + ", with: " + args)

            resp = getattr(self, cmd )(args )
            resp = f'OK {resp}\r\n'.encode()
        except Exception as err:
            print(err)
            resp = b'Error\r\n'    

        print(f"Sending: {resp}")
        self.request.sendall(resp)

