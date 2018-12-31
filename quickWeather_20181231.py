#! python3
# quickWeather.py - Display the weather forecast for the place name specified on the command line.
import sys
import requests
import json
from logging import getLogger, StreamHandler, DEBUG
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

# Assemble the place name from the command line argument

# Read into Python variable from JSON data.
