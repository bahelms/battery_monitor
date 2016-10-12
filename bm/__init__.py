import yaml
import os

config_file = os.environ.get("CONFIG_FILE") or "config.yml"

with open(config_file) as f:
    config = yaml.load(f.read())
