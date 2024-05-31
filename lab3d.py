#!/usr/bin/env python3
'''this is samir thapa doing lab 3'''

import subprocess

def free_space():
    command = "df -h | grep '/$' | awk '{print $4}'"
    result = subprocess.run(command, shell=True, capture_output=True, text=True, encoding='utf-8')
    return result.stdout.strip()

if __name__ == '_main_':
    print(free_space())