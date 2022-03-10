Configure RSYSLOG
on log-server to store logs from clients into /var/log/remotes/<REMOTE-HOSTNAME>/<PROGRAMNAME>-<DATE>.log



On SERVER:

vi /etc/rsyslog.conf

add:     

$ModLoad imudp
$UDPServerRun 514      # 514 - port number

$ModLoad imtcp
$InputTCPServerRun 514

$template RemoteLogs,"/var/log/remotes/%HOSTNAME%/%PROGRAMNAME%-%$year%-%$month%-%$day%.log"
*.* ?RemoteLogs
& ~

systemctl restart rsyslog



on CLIENT:

vi /etc/rsyslog.d/all.conf

add:

*.* @@192.168.0.170:514    # add IP rsyslog-server and port-number;  *.* - all type log-files

systemctl restart rsyslog

