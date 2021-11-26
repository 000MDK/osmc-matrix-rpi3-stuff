# osmc-matrix-rpi3-stuff
collection of configs, commands, addons etc. for OSMC (Matrix) on raspi3b+
-X11

-SteamLink

-retroarch (with N64)

-squeezelite

-config optimized for stability

-analogue audio output over jack

-all launcher addons updated to work

-quiet boot

-changed splash

-add custom rootca.cert

using X11 script from https://github.com/zjoasan/
using SteamLink-script from https://github.com/swetoast/steamlink-launcher
using retropie-script from https://github.com/mcobit/retrosmc/

working already, needs some cleanup and testing for release - waiting for a kernel update, because for now CEC is not working in this setup (steamlink needs fkms).

For a raspi 3B+: If you suffer lag in Kodi, you need to set `force_turbo=1` in config (voids warranty!) - I had multiple crashes per day with that though, but that was fixed by setting `core_freq=400`

`
sudo modprobe snd-bcm2835
`

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
#needs serious rework

sudo apt-get install squeezelite alsa-utils wakeuponlan steamlink wireless-tools v4l-utils setxkbmap xinput retroarch cec-utils squeezelite python3-crypto python3-pip python3-pycryptodome python-crypto-dbg python-crypto-doc python-pip-whl python-pip python-crypto build-essential -y

pip install pycryptodomex

pip install setuptools wheel pycryptodome
```

```
wget https://raw.githubusercontent.com/zjoasan/x11-osmc/master/install_x11.sh

chmod +x ./install_x11.sh

sh ./install_x11.sh

wget https://raw.githubusercontent.com/MarkusLange/VNC-Server-install-script-for-OSMC/master/osmc_vnc_install_cli.bash

chmod +x osmc_vnc_install_cli.bash

sudo ./osmc_vnc_install_cli.bash

sudo ./osmc_vnc_install_cli.bash --install-vnc

sudo ./osmc_vnc_install_cli.bash --activate-service

sudo ./osmc_vnc_install_cli.bash --start-vnc

wget https://raw.githubusercontent.com/mcobit/retrosmc/master/install-retrosmc.sh

chmod +x install-retrosmc.sh

./install-retrosmc.sh
#missing: copy n64 from retrosmc build to retroarch dir
```

