import os
import time

__author__ = 'mustafauzun0'

'''
WATCHPORT
'''

def clearConsole():
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')

def runCommand():
    command = os.popen('netstat -tulpn 2>/dev/null | grep "LISTEN"')
    result = command.read().strip()
    command.close()

    print(result)

if __name__ == '__main__':
    try:
        while True:
            clearConsole()
            runCommand()
            time.sleep(1)

    except KeyboardInterrupt:
        pass
