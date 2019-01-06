#!python3
# multidownloadXkcd.py - Download XKCD comic in multi thread

import requests
import os
import threading

os.makedirs('xkcd', exist_ok=True)  # Save comic in ./xkcd
