

# osmc-matrix-rpi3-stuff
collection of configs, commands, addons etc. for OSMC (Matrix) on raspi3b+

# 2Do: make install script and release

- X11

- SteamLink (modified addon from swetoast for x11)

- retroarch (with N64 from retrosmc)

- VNC

- Hyperion.NG

- squeezelite

- config optimized for stability

- analogue audio output over jack

- all launcher addons updated to work

- quiet boot

- changed splash

- add custom rootca.cert

using X11 script from https://github.com/zjoasan/

using SteamLink-script from https://github.com/swetoast/steamlink-launcher

using retropie-script from https://github.com/mcobit/retrosmc/

using netflix-install script from https://github.com/zjoasan/netflix-install-script/

using Hyperion.NG from https://github.com/hyperion-project/hyperion.ng/

using VNC-install script from https://github.com/MarkusLange/VNC-Server-install-script-for-OSMC/


working already, needs some cleanup and testing for release - cec still not working. investingating.

Note:
For a raspi 3B+: If you suffer lag in Kodi, you need to set `force_turbo=1` in config (voids warranty!) - I had multiple crashes per day with that though, but that was fixed by setting `core_freq=400`

`
sudo modprobe snd-bcm2835
`

```
sudo timedatectl set-timezone Your/TZ
sudo dpkg-reconfigure locales
```

```
sudo mkdir /usr/local/share/ca-certificates/extra

sudo cp /home/osmc/cacert.pem /usr/local/share/ca-certificates/extra/root.cert.crt

sudo rm /usr/share/kodi/system/certs/cacert.pem

sudo cp /home/osmc/cacert.pem /usr/share/kodi/system/certs/cacert.pem

sudo chown root:root /usr/share/kodi/system/certs/cacert.pem

sudo chmod 644 /usr/share/kodi/system/certs/cacert.pem

sudo update-ca-certificates
```

```
sudo apt-get install squeezelite alsa-utils wireless-tools v4l-utils xinput retroarch cec-utils git cmake build-essential qtbase5-dev libqt5serialport5-dev libusb-1.0-0-dev libturbojpeg0-dev python3-dev libcec-dev libxcb-util0-dev libxcb-randr0-dev libxrandr-dev libxrender-dev libavahi-core-dev libavahi-compat-libdnssd-dev libssl-dev libqt5sql5-sqlite libqt5svg5-dev zlib1g-dev
```

```
wget https://raw.githubusercontent.com/zjoasan/netflix-install-script/master/netflix_prep_install.sh
chmod +x netflix_prep_install.sh
./netflix_prep_install.sh

wget https://raw.githubusercontent.com/zjoasan/x11-osmc/master/install_x11.sh
chmod +x ./install_x11.sh
./install_x11.sh

wget https://raw.githubusercontent.com/MarkusLange/VNC-Server-install-script-for-OSMC/master/osmc_vnc_install_cli.bash
chmod +x osmc_vnc_install_cli.bash
#sudo ./osmc_vnc_install_cli.bash
sudo ./osmc_vnc_install_cli.bash --install-vnc
sudo ./osmc_vnc_install_cli.bash --activate-service
#sudo ./osmc_vnc_install_cli.bash --start-vnc

#wget -qO- https://raw.githubusercontent.com/hyperion-project/hyperion.ng/master/bin/compile.sh | sh -s hyperion Release install
wget https://github.com/hyperion-project/hyperion.ng/releases/download/2.0.12/Hyperion-2.0.12-Linux-armv7l.deb
sudo dpkg -i ./Hyperion-2.0.12-Linux-armv7l.deb

wget https://raw.githubusercontent.com/mcobit/retrosmc/master/install-retrosmc.sh
chmod +x install-retrosmc.sh
./install-retrosmc.sh

#missing: copy n64 from retrosmc build to retroarch dir
```

