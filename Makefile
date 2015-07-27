

GROVE_KIT_FILES := $(wildcard grovekit/*.py)

get:
	#scp -r root@edison.local:grovekit .
	cp -vu ~/Notebooks/High\ School/Links.ipynb .
	cp -vu ~/Notebooks/install_pkgs.txt .


ssh-setup:
	mkdir -p $(HOME)/.ssh
	chmod 700 $(HOME)/.ssh
	cp -vu ssh_config $(HOME)/.ssh/config

to-edison:
	scp -r grovekit edison:.

usb-ip:
	sudo ifconfig usb0 inet 192.168.2.10

proxy:
	microproxy -config=Config/microproxy.json

put:
	rsync -ai grovekit IoT root@edison.local:. --rsync-path=/home/root/.local/bin/rsync
