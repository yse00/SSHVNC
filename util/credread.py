import shutil
import subprocess
from configparser import ConfigParser
import os
import json

def GetAppData():
    return os.environ["LOCALAPPDATA"] + "\\SSHVNCP\\"

def FindKey():
    config = ConfigParser()
    config.read(GetAppData()+"credential.ini")
    a = json.loads(config.get("key","keyfile"))
    return a

def InitUser():
    config = ConfigParser()
    config.read(GetAppData()+"credential.ini")
    a = config.get("user","username")
    return a

def ChangeUser(username):
    config = ConfigParser()
    config.read(GetAppData() + "credential.ini")
    config.set("user","username", username)
    with open(GetAppData()+"credential.ini", 'w') as configfile:
        config.write(configfile)


def CopyPem(pathname,keyname):
    #copy the pem
    newitem = False
    keys = FindKey()
    if keyname not in keys:
        newitem = True
        keys[keyname] = keyname
        CopyPemFile(pathname, keyname)
    config = ConfigParser()
    config.read(GetAppData()+"credential.ini")
    config.set("key","keyfile",json.dumps(keys,ensure_ascii=False))
    with open(GetAppData()+"credential.ini", 'w') as configfile:
        config.write(configfile)
    
    return newitem

def CopyPemFile(pathname,keyname):
    shutil.copyfile(pathname, GetAppData() + keyname + ".pem")