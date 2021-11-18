#!/bin/bash
sudo fbi -T 7 -d /dev/fb0 --noverbose /home/osmc/.kodi/addons/plugin.program.steamlink/resources/fanart.jpg &
sleep 2
sudo openvt -c 7 -s -f clear
sudo su osmc -c "xinit /home/osmc/steamlink.xinitrc --"
sudo openvt -c 7 -s -f clear
sudo systemctl start mediacenter
exit
