"""
    Plugin for Launching programs
"""

# -*- coding: UTF-8 -*-
# main imports
import sys
import os
import xbmc
import xbmcgui
import xbmcaddon

# plugin constants
__plugin__ = "retroarch-launcher"
__author__ = "jcnventura/mcobit"
__url__ = "http://blog.petrockblock.com/retropie/"
__git_url__ = "https://github.com/mcobit/retrosmc/"
__credits__ = "mcobit"
__version__ = "0.0.1"

dialog = xbmcgui.Dialog()
addon = xbmcaddon.Addon(id='plugin.program.retroarch-launcher')

def main():
    """Main operations of this plugin."""
    create_files()
    output = os.popen("sh /tmp/retroarch-launcher.sh").read()
    dialog.ok("Starting RetroArch...", output)

def create_files():
    """Creates bash files to be used for this plugin."""
    with open('/tmp/retroarch-launcher.sh', 'w') as outfile:
        outfile.write("""#!/bin/bash
chmod 755 /tmp/retroarch-watchdog.sh
sudo openvt -c 7 -s -f clear
sudo su -c "nohup sudo openvt -c 7 -s -f -l /tmp/retroarch-watchdog.sh >/dev/null 2>&1 &"
""")
        outfile.close()
    with open('/tmp/retroarch-watchdog.sh', 'w') as outfile:
        outfile.write("""#!/bin/bash
systemctl stop mediacenter
if [ "$(systemctl is-active hyperion.service)" = "active" ]; then systemctl restart hyperion; fi



sleep 1
sudo openvt -c 7 -s -f clear
#sudo su osmc -c "/opt/retropie/emulators/retroarch/bin/retroarch"
sudo su osmc -c "retroarch"
sudo openvt -c 7 -s -f clear
sudo systemctl start mediacenter

""")
        outfile.close()
main()
