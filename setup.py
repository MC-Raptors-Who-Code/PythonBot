#!/usr/bin/env python3
import json

'''
- Code to generate config and do other setup on first run
'''

# default settings file
settings = {
    "token" : "NONE",
    "prefix" : "!",
    "status" : "In a Meeting...",
}

# writes settings to config
with open("./config.json", "w") as file:
    file.write(json.dumps(settings, indent=4))
