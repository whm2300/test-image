#!/bin/env python3

import requests
import time

def get():
    ret = requests.get("http://106.55.75.134")
    print(ret.text)

if __name__ == "__main__":
    while True:
        get()
        time.sleep(0.1)
