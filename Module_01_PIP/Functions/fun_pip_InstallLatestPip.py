
import subprocess
from packaging import version
import json
import requests
from distutils.version import StrictVersion
import os


def F_PipVersionCheck(package_name):
    '''
    Author : Arun Kumar
    Purpose : To install latest version of PIP
    '''

    global ver
    global oldVer
    global subprocessOp
    global subprocess_return

    url = "https://pypi.python.org/pypi/{}/json".format(package_name)
    data = requests.get(url).json()
    ver=sorted(list(data["releases"].keys()), key=StrictVersion, reverse=True)

    subprocessOp = subprocess.Popen("pip --version", shell=True, stdout=subprocess.PIPE)
    subprocess_return = subprocessOp.stdout.read()
    oldVer=str(subprocess_return).split(" ")[1]

    if version.parse(oldVer)<version.parse(ver[0]):
        print("Installing latest version of PIP")
        os.system("python -m pip install {} --upgrade".format(package_name))
    
    else :
        print("You have a already latest version of {}".format(package_name))




# F_PipVersionCheck('pip')