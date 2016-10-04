#!/bin/bash
PLIST_NAME="org.battery_monitor.plist"
INSTALL_PATH="/Library/LaunchDaemons"

echo "Installing launchctl plist: $PLIST_NAME --> $INSTALL_PATH"

python generate_plist.py $PLIST_NAME

sudo chown root $PLIST_NAME
sudo chmod 644 $PLIST_NAME
sudo cp -f $PLIST_NAME $INSTALL_PATH

sudo launchctl unload $PLIST_NAME
sudo launchctl load $PLIST_NAME
sudo rm -f $PLIST_NAME

echo "Installation complete." 
echo "To check running status:"
echo "    sudo launchctl list | grep battery_monitor"
