

install:
	cp -v hssi_iot.* /etc/systemd/system/.
	systemctl enable hssi_iot.service
	systemctl enable hssi_iot.timer
	journalctl -u hssi_iot

status:
	systemctl status hssi_iot.service
	systemctl status hssi_iot.timer
	systemctl list-timers

start:
	systemctl start hssi_iot.timer
	systemctl start hssi_iot.service

