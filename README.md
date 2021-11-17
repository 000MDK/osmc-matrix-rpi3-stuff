# soon
osmc-matrix-rpi3-stuff
collection of configs, commands, addons etc. for OSMC (Matrix) on rpi2

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

working already, needs some cleanup and testing for release. Meanwhile I'm waiting for a kernel update, because for now CEC is not working in this setup (steamlink needs fkms).

For a raspi 3B+: If you suffer lag in Kodi, you need to set 'force_turbo=1' in config (voids warranty!) - I had multiple crashes per day with that though, but that was fixed by setting core_freq=400
