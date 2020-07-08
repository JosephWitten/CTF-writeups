1) gobuster dir -u http://10.10.53.240:3333/ -w /usr/share/wordlists/dirb/big.txt 
I didnt have much luck with gobuster, so i used dirb. dirb http://IP:3333/
then i realised the answer wanted it in the form "/answer/"