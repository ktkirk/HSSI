

GROVE_KIT_FILES := $(wildcard grovekit/*.py)

get:
	#scp -r root@edison.local:grovekit .
	cp -vu ~/Notebooks/High\ School/Links.ipynb .
	cp -vu ~/Notebooks/install_pkgs.txt .


ssh-setup:
	mkdir $(HOME)/.ssh
	chmod 700 $(HOME)/.ssh
	cat > $(HOME)/.ssh/config << _EOF_
host edison
  StrictHostKeyChecking no
  HostName 192.168.2.15
  User root
_EOF_

to-edison:
	scp -r grovekit edison:.

usb-ip:
	sudo ifconfig usb0 inet 192.168.2.10

proxy:
	microproxy -config=Config/microproxy.json

put:
	rsync -ai grovekit IoT root@edison.local:. --rsync-path=/home/root/.local/bin/rsync
