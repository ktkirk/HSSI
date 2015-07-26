

# Update latest mraa and upm on Edison

STD_REPO_URL := http://iotdk.intel.com/repos/1.5/intelgalactic
DEV_REPO_URL := http://iotdk.intel.com/repos/1.5/intelgalactic-dev
MY_REPO_URL  := http://10.232.106.230:8500/ui/files/repos
REPO_FILE    := /etc/opkg/mraa-upm.conf
REPO_URL     := $(DEV_REPO_URL)

all: update-upm

$(REPO_FILE):
	echo "src mraa-upm $(REPO_URL)" > $@
	opkg update

update-mraa: $(REPO_FILE)
	opkg install libmraa0

update-upm: update-mraa
	opkg install upm

time:
	# update system time over the internet
	rdate -s rdate.cpanel.net
