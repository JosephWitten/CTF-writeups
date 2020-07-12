1) 
- nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse IP
- 3
2)
- smbclient //IP/anonymous
- no password
- ls
- log.txt
3)
- cat log.txt
- 21
4) nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount IP