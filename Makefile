

GROVE_KIT_FILES := $(wildcard grovekit/*.py)
SSH_CONFIG := $(HOME)/.ssh/config

get:
	#scp -r root@edison.local:grovekit .
	cp -vu ~/Notebooks/High\ School/Links.ipynb .
	cp -vu ~/Notebooks/install_pkgs.txt .

ssh-setup: $(SSH_CONFIG)
	ssh-copy-id edison

to-edison: ssh-setup
	scp -r grovekit edison:.

$(SSH_CONFIG): ssh_config
	ssh-keygen -q -N ""
	cp -vu $< $@

usb-ip:
	sudo ifconfig usb0 inet 192.168.2.10

proxy:
	microproxy -config=Config/microproxy.json

put:
	rsync -ai grovekit IoT root@edison.local:. --rsync-path=/home/root/.local/bin/rsync
