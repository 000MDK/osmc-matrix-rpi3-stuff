#!/bin/bash
sudo systemctl stop mediacenter &
sleep 5
sudo openvt -c 7 -s -f clear
sudo fbi -T 7 -d /dev/fb0 --noverbose /home/osmc/.kodi/addons/plugin.program.retrosmc-launcher/fanart.jpg &
sleep 3
sudo su osmc -c "/opt/retropie/emulators/retroarch/bin/retroarch &" &
sleep 1
sudo openvt -c 7 -s -f clear
sudo systemctl start mediacenter
exit
