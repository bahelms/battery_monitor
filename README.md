# Battery Monitor
Get macOS notifications when your battery percentage hits certain thresholds.

### Setup

    git clone git@github.com:bahelms/battery_monitor.git
    cd battery_monitor && pip install -r requirements.txt
    ./install.sh

### Configuration
The upper and lower bounds can be set in the `config.yml` file.

### Tests
Run full suite with: 
  
    python -m unittest discover tests -p "*.py"
