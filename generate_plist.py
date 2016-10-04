import os
import sys

with open("plist_template.xml") as f:
    xml_string = f.read()

with open(sys.argv[1], "w") as f:
    f.write(xml_string.format(home=os.environ["HOME"]))
