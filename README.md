## PowerShellXFiltration
A PowerShell script to exfiltrate information of a Windows system via HTTP server

### How it works
1. Runs several PS commands to retrieve information about the local system and the domain if any.
2. Sends the outputs to the webserver as GET parameter (and Base64 encoded)
3. The server logs any action in the current folder (`logs.txt`)
4. Create a directory with the system hostname and put all the exfiltrated info into

### Example
1. Change the listening IP/Port in `server.py` (default is `0.0.0.0:8000`).
2. Change the IP/port of your Python server in `client.ps1`.
3. Run:
```
ATTACKER> python3 server.py
VICTIM> powershell -ep bypass -windowstyle hidden -File client.ps1
```
