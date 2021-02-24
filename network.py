#!/usr/bin/env python3

import requests
import socket

def check_localhost():

        localhost = socket.gethostbyname('localhost')

        if str(localhost) == "127.0.0.1":
                return "true"
        else:
                return "false"

def check_connectivity():

        request = requests.get("http://www.google.com")

        if request == "200":
                return "true"

        else:
                return "false"
