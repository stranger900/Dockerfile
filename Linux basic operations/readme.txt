Create file with the name script in the homedir.
cd ~
touch script

Rename it to script.sh, add command date into it and make it executable for all, read/write for owner, read for group and others. 
mv script script.sh
        Add #!/bin/bash
ll        
chmod 744 script.sh 
ll

Create directory ~/tools/scripts (single command) and move script.sh into this dir.
cd ~
mkdir -p tools/scripts 
mv script.sh tools/scripts/

Create symlink with the name automation which points to ~/tools/scripts.
ln -s ~/tools/scripts MyLinkToScripts

Create user john and additionally make this user a part of the group devops.
groupadd devops
useradd -m john
usermod -aG devops john
id john

Install Nginx on CentOS, add it to start on boot.
sudo yum install epel-release
sudo yum install nginx
sudo systemctl start nginx
sudo systemctl status nginx

Find the Nginx process in the system and try to kill it.
systemctl status nginx
ps -aux | grep nginx
kill 32625

Try to perform yum install nginx (without sudo) and redirect stdout to install.log and stderr to install_err.log.
apt install nginx 1> install.log 2>install_err.log        # apt install nginx 2>$1 1> both.txt
cat install_err.log 

Allow john to run sudo commands.

