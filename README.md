# Battery Monitor
Get macOS notifications for when your battery percentage hits certain thresholds.

### Setup

    git clone git@github.com:bahelms/battery_monitor.git
    cd battery_monitor && pip install -r requirements.txt
    python monitor.py
    
### To run in background on computer start

    cp battery_monitor/battery_monitor.plist /Library/LaunchDaemons/
    launchctl load /Library/LaunchDaemons/battery_monitor.plist
